from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
import uvicorn
from patchwork.common.client.llm.aio import AioLlmClient
from patchwork.common.client.llm.openai import OpenAiLlmClient
from patchwork.common.client.llm.google import GoogleLlmClient
from patchwork.common.client.llm.anthropic import AnthropicLlmClient
from patchwork.step import Step
from openai.types.chat import ChatCompletion

_DEFAULT_INPUT_FILE = Path(__file__).parent / "defaults.yml"
_DEFAULT_PROMPT_JSON = Path(__file__).parent / "prompt.json"


class LLMProxyEndpoint(Step):
    def __init__(self, inputs: dict):
        final_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text())

        if final_inputs is None:
            final_inputs = {}
        final_inputs.update(inputs)

        self.host = final_inputs.get("host", "127.0.0.1")
        self.port = int(final_inputs.get("port", 8080))
        self.aio_client = AioLlmClient(
            self.__create_openai_client(final_inputs),
            self.__create_google_ai_client(final_inputs),
            self.__create_anthropic_client(final_inputs),
        )

    @staticmethod
    def __create_openai_client(inputs: dict) -> OpenAiLlmClient | None:
        if "openai_api_key" not in inputs.keys():
            return None
        return OpenAiLlmClient(api_key=inputs["openai_api_key"])

    @staticmethod
    def __create_google_ai_client(inputs: dict) -> GoogleLlmClient | None:
        if "google_api_key" not in inputs.keys():
            return None
        return GoogleLlmClient(api_key=inputs["google_api_key"])

    @staticmethod
    def __create_anthropic_client(inputs: dict) -> AnthropicLlmClient | None:
        if "anthropic_api_key" not in inputs.keys():
            return None
        return AnthropicLlmClient(api_key=inputs["anthropic_api_key"])

    def run(self) -> dict:
        app = FastAPI()

        @app.post("/v1/chat/completions")
        def handle_openai(request_json: dict) -> ChatCompletion:
            if all(key in request_json.keys() for key in ["model", "messages"]):
                raise RequestValidationError([
                    {
                        "loc": ["model", "messages"],
                        "msg": "Invalid request, missing required fields: model, messages",
                        "type": "value_error"
                    }
                ])

            return self.aio_client.chat_completion(**request_json)

        try:
            uvicorn.run(app, host=self.host, port=self.port)
        finally:
            return dict()
