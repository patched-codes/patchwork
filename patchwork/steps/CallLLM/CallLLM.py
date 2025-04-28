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
            available_tokens = self.client.is_prompt_supported(model=self.model, messages=prompt, **kwargs)
            is_input_accepted = available_tokens > 0
            
            if not is_input_accepted:
                self.set_status(StepStatus.WARNING, "Input token limit exceeded.")
                prompt = self.client.truncate_messages(prompt, self.model)
            
            # Handle the case where model_max_tokens was set to -1
            # Calculate max_tokens based on available tokens from the model after prompt
            if hasattr(self, '_use_max_tokens') and self._use_max_tokens:
                if available_tokens > 0:
                    kwargs['max_tokens'] = available_tokens
                    logger.info(f"Setting max_tokens to {available_tokens} based on available model context")
                else:
                    # If we can't determine available tokens, set a reasonable default
                    logger.warning("Could not determine available tokens. Using model default.")

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

        # Handle special case for max_tokens = -1 (use maximum available tokens)
        if 'max_tokens' in new_model_args and new_model_args['max_tokens'] == -1:
            # Will be handled during the chat completion call
            logger.info("Using maximum available tokens for the model")
            del new_model_args['max_tokens']  # Remove it for now, we'll calculate it later
            self._use_max_tokens = True
        else:
            self._use_max_tokens = False

        return new_model_args
