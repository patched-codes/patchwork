from __future__ import annotations

import json
import os
from pathlib import Path
from pprint import pformat
from textwrap import indent

import requests
from openai import OpenAI
from typing_extensions import Any, Protocol

from patchwork.logger import logger
from patchwork.step import Step

_TOKEN_URL = "https://app.patched.codes/signin"
_DEFAULT_PATCH_URL = "https://patchwork.patched.codes/v1"


class LLMModel(Protocol):
    def call(self, prompts) -> list[str]:
        pass


class CallGemini(LLMModel):
    _SAFETY_SETTINGS = [
        dict(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),
        dict(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
        dict(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),
        dict(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),
    ]

    def __init__(
        self, model: str, model_args: dict[str, Any], client_args: dict[str, Any], key: str, allow_truncated: bool
    ):
        client_values = client_args.copy()

        self.model = model
        self.base_url = client_values.pop("base_url", "https://generativelanguage.googleapis.com/v1")
        self.model_args = model_args
        self.api_key = key
        self.allow_truncated = allow_truncated

    def call(self, prompts):
        contents = []
        for prompt in prompts:
            texts = [dict(text=subprompt.get("content", "")) for subprompt in prompt]

            try:
                response = requests.post(
                    f"{self.base_url}/models/{self.model}:generateContent",
                    params=dict(key=self.api_key),
                    json=dict(
                        generationConfig=self.model_args,
                        contents=[dict(parts=texts)],
                        safetySettings=self._SAFETY_SETTINGS,
                    ),
                )
                response.raise_for_status()
                response_dict = response.json()
            except Exception as e:
                logger.error(e)
                response_dict = {}

            candidate = response_dict.get("candidates", [{}])[0]
            text_response = candidate.get("content", {}).get("parts", [{}])[0].get("text", "")
            if text_response == "":
                logger.error(f"No response choice given")
                content = ""
            elif candidate.get("finishReason", "").upper() == "MAX_TOKENS":
                if self.allow_truncated:
                    content = text_response
                else:
                    logger.error(
                        f"Response truncated because of finish reason = length."
                        f" Use --allow_truncated option to process truncated responses."
                    )
                    content = ""
            else:
                content = text_response
                logger.debug(f"Response received: \n{indent(content, '  ')}")

            contents.append(content)

        return contents


class CallOpenAI(LLMModel):
    def __init__(
        self, model: str, model_args: dict[str, Any], client_args: dict[str, Any], key: str, allow_truncated: bool
    ):
        self.model = model
        self.model_args = model_args
        self.allow_truncated = allow_truncated
        self.client = OpenAI(api_key=key, **client_args)

    def call(self, prompts) -> list[str]:
        contents = []
        for prompt in prompts:
            logger.debug(f"Message sent: \n{indent(pformat(prompt), '  ')}")
            try:
                completion = self.client.chat.completions.create(model=self.model, messages=prompt, **self.model_args)
            except Exception as e:
                logger.error(e)
                completion = None

            if completion is None or len(completion.choices) < 1:
                logger.error(f"No response choice given")
                content = ""
            elif completion.choices[0].finish_reason == "length":
                if self.allow_truncated:
                    content = completion.choices[0].message.content
                else:
                    logger.error(
                        f"Response truncated because of finish reason = length."
                        f" Use --allow_truncated option to process truncated responses."
                    )
                    content = ""
            else:
                content = completion.choices[0].message.content
                logger.debug(f"Response received: \n{indent(content, '  ')}")

            contents.append(content)

        return contents


class CallLLM(Step):
    def __init__(self, inputs: dict):
        logger.info(f"Run started {self.__class__.__name__}")

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

        self.model_args = {key[len("model_") :]: value for key, value in inputs.items() if key.startswith("model_")}
        self.client_args = {key[len("client_") :]: value for key, value in inputs.items() if key.startswith("client_")}

        llm_key = inputs.get("openai_api_key") or os.environ.get("OPENAI_API_KEY")

        patched_key = inputs.get("patched_api_key")
        if patched_key is not None:
            llm_key = patched_key
            self.client_args["base_url"] = _DEFAULT_PATCH_URL

        if llm_key is not None:
            self.llm = CallOpenAI(
                model=inputs.get("model", "gpt-3.5-turbo"),
                model_args=self.model_args,
                client_args=self.client_args,
                key=llm_key,
                allow_truncated=inputs.get("allow_truncated", False),
            )
            return

        llm_key = inputs.get("google_api_key")
        if llm_key is not None:
            self.llm = CallGemini(
                model=inputs.get("model", "gemini-1.0-pro"),
                model_args=self.model_args,
                client_args=self.client_args,
                key=llm_key,
                allow_truncated=inputs.get("allow_truncated", False),
            )
            return

        raise ValueError(
            f"Model API key not found.\n"
            f'Please login at: "{_TOKEN_URL}",\n'
            "Please go to the Integration's tab and generate an API key.\n"
            "Please copy the access token that is generated, "
            "and add `--patched_api_key=<token>` to the command line.\n"
            "\n"
            "If you are using a OpenAI API Key, please set `--openai_api_key=<token>`.\n"
        )

    def run(self) -> dict:
        contents = self.llm.call(self.prompts)

        logger.info(f"Run completed {self.__class__.__name__}")
        return dict(openai_responses=contents)
