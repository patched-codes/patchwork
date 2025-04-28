from __future__ import annotations

import functools
from functools import cached_property
from pathlib import Path

import tiktoken
from openai import OpenAI
from openai.types.chat import (
    ChatCompletion,
    ChatCompletionMessageParam,
    ChatCompletionToolChoiceOptionParam,
    ChatCompletionToolParam,
    completion_create_params,
)
from pydantic_ai.messages import ModelMessage, ModelResponse
from pydantic_ai.models import Model, ModelRequestParameters, StreamedResponse
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.settings import ModelSettings
from pydantic_ai.usage import Usage
from typing_extensions import AsyncIterator, Dict, Iterable, List, Optional, Union

from patchwork.common.client.llm.protocol import NOT_GIVEN, LlmClient, NotGiven
from patchwork.logger import logger


@functools.lru_cache
def _cached_list_models_from_openai(api_key):
    client = OpenAI(api_key=api_key)
    sync_page = client.models.list()

    models = set()
    for pages in sync_page.iter_pages():
        models.update(map(lambda x: x.id, pages.data))

    return models


class OpenAiLlmClient(LlmClient):
    __MODEL_LIMITS = {
        "gpt-3.5-turbo": 16_385,
        "gpt-4": 8_192,
        "gpt-4-turbo": 8_192,
        "o1-mini": 128_000,
        "gpt-4o-mini": 128_000,
        "gpt-4o": 128_000,
        "o3-mini": 128_000,
    }

    def __init__(self, api_key: str, base_url=None, **kwargs):
        self.__api_key = api_key
        self.__base_url = base_url
        self.__kwargs = kwargs

    @cached_property
    def __client(self) -> OpenAI:
        return OpenAI(api_key=self.__api_key, base_url=self.__base_url, **self.__kwargs)

    def __get_pydantic_model(self, model_settings: ModelSettings | None) -> Model:
        if model_settings is None:
            raise ValueError("Model settings cannot be None")
        model_name = model_settings.get("model")
        if model_name is None:
            raise ValueError("Model must be set cannot be None")

        return OpenAIModel(model_name, base_url=self.__base_url, api_key=self.__api_key)

    async def request(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> tuple[ModelResponse, Usage]:
        model = self.__get_pydantic_model(model_settings)
        return await model.request(messages, model_settings, model_request_parameters)

    async def request_stream(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> AsyncIterator[StreamedResponse]:
        model = self.__get_pydantic_model(model_settings)
        yield model.request_stream(messages, model_settings, model_request_parameters)

    @property
    def model_name(self) -> str:
        return "Undetermined"

    @property
    def system(self) -> str | None:
        return "openai"

    def __is_not_openai_url(self):
        # Some providers/apis only implement the chat completion endpoint.
        # We mainly use this to skip using the model endpoints.
        return self.__base_url is not None and self.__base_url != "https://api.openai.com/v1"

    def test(self):
        if self.__is_not_openai_url():
            return

        _cached_list_models_from_openai(self.__api_key)
        return

    def is_model_supported(self, model: str) -> bool:
        # might not implement model endpoint
        if self.__is_not_openai_url():
            return True
        return model in _cached_list_models_from_openai(self.__api_key)

    def __get_model_limits(self, model: str) -> int:
        """Return the token limit for a given model."""
        return self.__MODEL_LIMITS.get(model, 128_000)
        
    def get_model_limit(self, model: str) -> int:
        """
        Public method to get the model's context length limit.
        
        Args:
            model: The model name
            
        Returns:
            The maximum context length in tokens
        """
        return self.__get_model_limits(model)



    def truncate_messages(
        self, messages: Iterable[ChatCompletionMessageParam], model: str
    ) -> Iterable[ChatCompletionMessageParam]:
        return self._truncate_messages(self, messages, model)

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
        input_kwargs = dict(
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

        return self.__client.chat.completions.create(**NotGiven.remove_not_given(input_kwargs))
