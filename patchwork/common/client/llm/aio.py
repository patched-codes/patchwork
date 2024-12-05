from __future__ import annotations

import os

from openai.types.chat import (
    ChatCompletion,
    ChatCompletionMessageParam,
    ChatCompletionToolChoiceOptionParam,
    ChatCompletionToolParam,
    completion_create_params,
)
from typing_extensions import Dict, Iterable, List, Optional, Union

from patchwork.common.client.llm.anthropic import AnthropicLlmClient
from patchwork.common.client.llm.google import GoogleLlmClient
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
                self.__supported_models.update(client.get_models())
                self.__clients.append(client)
            except Exception:
                pass

    def get_models(self) -> set[str]:
        return self.__supported_models

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
    ) -> int:
        for client in self.__clients:
            if client.is_model_supported(model):
                return client.is_prompt_supported(
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
    ) -> ChatCompletion:
        for client in self.__clients:
            if client.is_model_supported(model):
                logger.debug(f"Using {client.__class__.__name__} for model {model}")
                return client.chat_completion(
                    messages,
                    model,
                    frequency_penalty,
                    logit_bias,
                    logprobs,
                    max_tokens,
                    n,
                    presence_penalty,
                    response_format,
                    stop,
                    temperature,
                    tools,
                    tool_choice,
                    top_logprobs,
                    top_p,
                )
        client_names = [client.__class__.__name__ for client in self.__original_clients]
        raise ValueError(
            f"Model {model} is not supported by {client_names} clients. "
            f"Please ensure that the respective API keys are correct."
        )

    @staticmethod
    def create_aio_client(inputs) -> "AioLlmClient" | None:
        clients = []

        patched_key = inputs.get("patched_api_key")
        if patched_key is not None:
            client = OpenAiLlmClient(patched_key, DEFAULT_PATCH_URL)
            clients.append(client)

        openai_key = inputs.get("openai_api_key") or os.environ.get("OPENAI_API_KEY")
        if openai_key is not None:
            client_args = {key[len("client_") :]: value for key, value in inputs.items() if key.startswith("client_")}
            client = OpenAiLlmClient(openai_key, **client_args)
            clients.append(client)

        google_key = inputs.get("google_api_key")
        if google_key is not None:
            client = GoogleLlmClient(google_key)
            clients.append(client)

        anthropic_key = inputs.get("anthropic_api_key")
        if anthropic_key is not None:
            client = AnthropicLlmClient(anthropic_key)
            clients.append(client)

        if len(clients) == 0:
            return None

        return AioLlmClient(*clients)
