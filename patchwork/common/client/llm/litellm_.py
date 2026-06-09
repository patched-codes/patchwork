from __future__ import annotations

from pathlib import Path

import litellm
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


class LiteLLMClient(LlmClient):
    """LLM client backed by the LiteLLM AI gateway.

    Supports 100+ providers (OpenAI, Anthropic, Google, Azure,
    AWS Bedrock, Ollama, Groq, Mistral, and more) through a unified
    interface. Model strings follow the LiteLLM format, e.g.
    ``anthropic/claude-sonnet-4-6`` or ``openai/gpt-4o``.
    """

    def __init__(self, api_key: str, **kwargs):
        self.__api_key = api_key
        self.__kwargs = kwargs

    def __get_pydantic_model(self, model_settings: ModelSettings | None) -> Model:
        if model_settings is None:
            raise ValueError("Model settings cannot be None")
        model_name = model_settings.get("model")
        if model_name is None:
            raise ValueError("Model must be set cannot be None")
        return OpenAIModel(model_name, api_key=self.__api_key)

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
        return "litellm"

    def test(self):
        return

    def is_model_supported(self, model: str) -> bool:
        return True

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
        return 1

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
            drop_params=True,
        )

        cleaned = NotGiven.remove_not_given(input_kwargs)
        if self.__api_key:
            cleaned["api_key"] = self.__api_key

        return litellm.completion(**cleaned)
