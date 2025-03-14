from __future__ import annotations

import os
from pathlib import Path

from openai.types.chat import (
    ChatCompletion,
    ChatCompletionMessageParam,
    ChatCompletionToolChoiceOptionParam,
    ChatCompletionToolParam,
    completion_create_params,
)
from pydantic_ai.messages import ModelMessage, ModelResponse
from pydantic_ai.models import ModelRequestParameters, StreamedResponse
from pydantic_ai.settings import ModelSettings
from pydantic_ai.usage import Usage
from typing_extensions import AsyncIterator, Dict, Iterable, List, Optional, Union

from patchwork.common.client.llm.anthropic import AnthropicLlmClient
from patchwork.common.client.llm.google_ import GoogleLlmClient
from patchwork.common.client.llm.openai_ import OpenAiLlmClient
from patchwork.common.client.llm.protocol import NOT_GIVEN, LlmClient, NotGiven
from patchwork.common.constants import DEFAULT_PATCH_URL
from patchwork.logger import logger


class AioLlmClient(LlmClient):
    def __init__(self, *clients: LlmClient):
        self.__original_clients = clients
        self.__clients = []
        self.__supported_models = set()
        for client in clients:
            try:
                client.test()
                self.__clients.append(client)
            except Exception as e:
                logger.error(f"{client.__class__.__name__} Failed with exception: {e}")

    def __get_model(self, model_settings: ModelSettings | None) -> Optional[str]:
        if model_settings is None:
            raise ValueError("Model settings cannot be None")
        model_name = model_settings.get("model")
        if model_name is None:
            raise ValueError("Model must be set cannot be None")

        return model_name

    def test(self) -> None:
        pass

    async def request(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> tuple[ModelResponse, Usage]:
        model = self.__get_model(model_settings)
        if model is None:
            raise ValueError("Model cannot be unset")

        for client in self.__clients:
            if client.is_model_supported(model):
                return await client.request(messages, model_settings, model_request_parameters)

        client_names = [client.__class__.__name__ for client in self.__original_clients]
        raise ValueError(
            f"Model {model} is not supported by {client_names} clients. "
            f"Please ensure that the respective API keys are correct."
        )

    async def request_stream(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> AsyncIterator[StreamedResponse]:
        model = self.__get_model(model_settings)
        if model is None:
            raise ValueError("Model cannot be unset")

        for client in self.__clients:
            if client.is_model_supported(model):
                yield client.request(messages, model_settings, model_request_parameters)
                return

        client_names = [client.__class__.__name__ for client in self.__original_clients]
        raise ValueError(
            f"Model {model} is not supported by {client_names} clients. "
            f"Please ensure that the respective API keys are correct."
        )

    @property
    def model_name(self) -> str:
        return "Undetermined"

    @property
    def system(self) -> str:
        return next(iter(self.__clients)).system

    def is_model_supported(self, model: str) -> bool:
        return any(client.is_model_supported(model) for client in self.__clients)

    def is_prompt_supported(
        self,
        messages: Iterable[ChatCompletionMessageParam],
        model: str,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: dict | completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        file: Path | NotGiven = NOT_GIVEN,
    ) -> int:
        for client in self.__clients:
            if client.is_model_supported(model):
                inputs = dict(
                    messages=messages,
                    model=model,
                    frequency_penalty=frequency_penalty,
                    logit_bias=logit_bias,
                    logprobs=logprobs,
                    max_tokens=max_tokens,
                    n=n,
                    presence_penalty=presence_penalty,
                    response_format=response_format,
                    stop=stop,
                    temperature=temperature,
                    tools=tools,
                    tool_choice=tool_choice,
                    top_logprobs=top_logprobs,
                    top_p=top_p,
                )
                if file is not NotGiven:
                    inputs["file"] = file
                return client.is_prompt_supported(**inputs)
        return -1

    def truncate_messages(
        self, messages: Iterable[ChatCompletionMessageParam], model: str
    ) -> Iterable[ChatCompletionMessageParam]:
        for client in self.__clients:
            if client.is_model_supported(model):
                return client.truncate_messages(messages, model)
        return messages

    def chat_completion(
        self,
        messages: Iterable[ChatCompletionMessageParam],
        model: str,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: dict | completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        file: Path | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion:
        for client in self.__clients:
            if client.is_model_supported(model):
                logger.debug(f"Using {client.__class__.__name__} for model {model}")
                inputs = dict(
                    messages=messages,
                    model=model,
                    frequency_penalty=frequency_penalty,
                    logit_bias=logit_bias,
                    logprobs=logprobs,
                    max_tokens=max_tokens,
                    n=n,
                    presence_penalty=presence_penalty,
                    response_format=response_format,
                    stop=stop,
                    temperature=temperature,
                    tools=tools,
                    tool_choice=tool_choice,
                    top_logprobs=top_logprobs,
                    top_p=top_p,
                )
                if file is not NotGiven:
                    inputs["file"] = file
                return client.chat_completion(**inputs)
        client_names = [client.__class__.__name__ for client in self.__original_clients]
        raise ValueError(
            f"Model {model} is not supported by {client_names} clients. "
            f"Please ensure that the respective API keys are correct."
        )

    @staticmethod
    def create_aio_client(inputs) -> "AioLlmClient" | None:
        clients = []

        client_args = {key[len("client_") :]: value for key, value in inputs.items() if key.startswith("client_")}

        patched_key = inputs.get("patched_api_key")
        if patched_key is not None:
            client = OpenAiLlmClient(patched_key, DEFAULT_PATCH_URL)
            clients.append(client)

        openai_key = inputs.get("openai_api_key") or os.environ.get("OPENAI_API_KEY")
        if openai_key is not None:
            client = OpenAiLlmClient(openai_key, **client_args)
            clients.append(client)

        google_key = inputs.get("google_api_key")
        is_gcp = bool(client_args.get("is_gcp") or os.environ.get("GOOGLE_GENAI_USE_VERTEXAI") or False)
        if google_key is not None or is_gcp:
            client = GoogleLlmClient(api_key=google_key, is_gcp=is_gcp)
            clients.append(client)

        anthropic_key = inputs.get("anthropic_api_key")
        if anthropic_key is not None:
            client = AnthropicLlmClient(anthropic_key)
            clients.append(client)

        if len(clients) == 0:
            return None

        return AioLlmClient(*clients)
