from __future__ import annotations

import json
import os
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from pprint import pformat
from textwrap import indent

from rich.markup import escape

from patchwork.common.client.llm.aio import AioLlmClient
from patchwork.common.constants import TOKEN_URL
from patchwork.logger import logger
from patchwork.step import Step, StepStatus
from patchwork.steps.CallLLM.typed import CallLLMInputs, CallLLMOutputs


@dataclass
class _InnerCallLLMResponse:
    prompts: list[dict]
    response: str
    request_token: int
    response_token: int


class CallLLM(Step, input_class=CallLLMInputs, output_class=CallLLMOutputs):
    def __init__(self, inputs: dict):
        super().__init__(inputs)
        # Set 'openai_key' from inputs or environment if not already set
        inputs.setdefault("openai_api_key", os.environ.get("OPENAI_API_KEY"))

        prompt_file = inputs.get("prompt_file")
        if prompt_file is not None:
            prompt_file_path = Path(prompt_file)
            if not prompt_file_path.is_file():
                raise ValueError(f'Unable to find Prompt file: "{prompt_file}"')
            try:
                with open(prompt_file_path, "r") as fp:
                    self.prompts = json.load(fp)
            except json.JSONDecodeError as e:
                raise ValueError(f'Invalid Json Prompt file "{prompt_file}": {e}')
        elif "prompts" in inputs.keys():
            self.prompts = inputs["prompts"]
        else:
            raise ValueError('Missing required data: "prompt_file" or "prompts"')

        self.call_limit = int(inputs.get("max_llm_calls", -1))
        self.model_args = {key[len("model_") :]: value for key, value in inputs.items() if key.startswith("model_")}
        self.save_responses_to_file = inputs.get("save_responses_to_file", None)
        self.model = inputs.get("model", "gpt-4o-mini")
        self.allow_truncated = inputs.get("allow_truncated", False)
        self.file = inputs.get("file", None)
        self.client = AioLlmClient.create_aio_client(inputs)
        if self.client is None:
            raise ValueError(
                f"Model API key not found.\n"
                f'Please login at: "{TOKEN_URL}",\n'
                "Please go to the Integration's tab and generate an API key.\n"
                "Please copy the access token that is generated, "
                "and add `--patched_api_key=<token>` to the command line.\n"
                "\n"
                "If you are using an OpenAI API Key, please set `--openai_api_key=<token>`.\n"
            )

    def __persist_to_file(self, contents):
        # Convert relative path to absolute path
        file_path = os.path.abspath(self.save_responses_to_file)

        mode = "a" if os.path.exists(file_path) else "w"
        logger.debug(f"Writing responses to file with mode '{mode}': {file_path}")
        with open(file_path, mode) as f:
            for prompt, response in zip(self.prompts, contents):
                data = {
                    "model": self.model,
                    "model_args": self.model_args,
                    "request": prompt,
                    "response": response,
                }
                f.write(json.dumps(data) + "\n")

    def run(self) -> dict:
        prompt_length = len(self.prompts)
        if prompt_length == 0:
            self.set_status(StepStatus.SKIPPED, "No prompts to process")
            return dict(openai_responses=[])

        if -1 < self.call_limit < prompt_length:
            logger.debug(
                f"Number of prompts ({prompt_length}) exceeds the call limit ({self.call_limit}). "
                f"Only the first {self.call_limit} prompts will be processed."
            )
            prompts = list(islice(self.prompts, self.call_limit))
        else:
            prompts = self.prompts

        contents = self.__call(prompts)

        openai_responses = []
        request_tokens = []
        response_tokens = []
        for content in contents:
            openai_responses.append(content.response)
            request_tokens.append(content.request_token)
            response_tokens.append(content.response_token)

        if self.save_responses_to_file:
            self.__persist_to_file(openai_responses)

        return dict(openai_responses=openai_responses, request_tokens=request_tokens, response_tokens=response_tokens)

    def __call(self, prompts: list[list[dict]]) -> list[_InnerCallLLMResponse]:
        contents: list[_InnerCallLLMResponse] = []

        # Parse model arguments
        parsed_model_args = self.__parse_model_args()

        kwargs = dict(parsed_model_args)
        if self.file is not None:
            kwargs["file"] = Path(self.file)

        for prompt in prompts:
            is_input_accepted = self.client.is_prompt_supported(model=self.model, messages=prompt, **kwargs) > 0
            if not is_input_accepted:
                self.set_status(StepStatus.WARNING, "Input token limit exceeded.")
                prompt = self.client.truncate_messages(prompt, self.model)

            logger.trace(f"Message sent: \n{escape(indent(pformat(prompt), '  '))}")
            try:
                completion = self.client.chat_completion(model=self.model, messages=prompt, **kwargs)
            except Exception as e:
                logger.error(e)
                completion = None

            if completion is None or len(completion.choices) < 1:
                self.set_status(StepStatus.FAILED, "Model did not return a response.")
                content = ""
                request_token = 0
                response_token = 0
            elif completion.choices[0].finish_reason == "length":
                self.set_status(StepStatus.WARNING, "Response truncated because of finish reason = length.")
                content = completion.choices[0].message.content
                request_token = completion.usage.prompt_tokens
                response_token = completion.usage.completion_tokens
            else:
                content = completion.choices[0].message.content
                request_token = completion.usage.prompt_tokens
                response_token = completion.usage.completion_tokens

            logger.trace(f"Response received: \n{escape(indent(content, '  '))}")
            contents.append(
                _InnerCallLLMResponse(
                    prompts=prompt,
                    response=content,
                    request_token=request_token,
                    response_token=response_token,
                )
            )

        return contents

    def __parse_model_args(self) -> dict:
        model_args = self.model_args
        # List of arguments in their respective types
        int_args = {"max_tokens", "n", "top_logprobs"}
        float_args = {"temperature", "top_p", "presence_penalty", "frequency_penalty"}
        bool_args = {"logprobs"}

        new_model_args = dict()
        for key, arg in model_args.items():
            if key in int_args and isinstance(arg, str):
                try:
                    new_model_args[key] = int(arg)
                except ValueError:
                    logger.warning(f"Failed to parse {key} as integer. Removing from arguments.")
            elif key in float_args and isinstance(arg, str):
                try:
                    new_model_args[key] = float(arg)
                except ValueError:
                    logger.warning(f"Failed to parse {key} as float. Removing from arguments.")
            elif key in bool_args and isinstance(arg, str):
                new_model_args[key] = arg.lower() == "true"
            else:
                new_model_args[key] = arg

        return new_model_args
