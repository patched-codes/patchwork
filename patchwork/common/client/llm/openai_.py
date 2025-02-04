from __future__ import annotations

import functools

import tiktoken
from openai import OpenAI
from openai.types.chat import (
    ChatCompletion,
    ChatCompletionMessageParam,
    ChatCompletionToolChoiceOptionParam,
    ChatCompletionToolParam,
    completion_create_params,
)
from typing_extensions import Dict, Iterable, List, Optional, Union

from patchwork.common.client.llm.protocol import NOT_GIVEN, LlmClient, NotGiven


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
        self.api_key = api_key
        self.base_url = base_url
        self.client = OpenAI(api_key=api_key, base_url=base_url, **kwargs)

    def __is_not_openai_url(self):
        # Some providers/apis only implement the chat completion endpoint.
        # We mainly use this to skip using the model endpoints.
        return self.base_url is not None and self.base_url != "https://api.openai.com/v1"

    def get_models(self) -> set[str]:
        if self.__is_not_openai_url():
            return set()

        return _cached_list_models_from_openai(self.api_key)

    def is_model_supported(self, model: str) -> bool:
        # might not implement model endpoint
        if self.__is_not_openai_url():
            return True
        return model in self.get_models()

    def __get_model_limits(self, model: str) -> int:
        return self.__MODEL_LIMITS.get(model, 128_000)

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
        # might not implement model endpoint
        if self.__is_not_openai_url():
            return 1

        model_limit = self.__get_model_limits(model)
        token_count = 0
        try:
            encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            # Fallback to gpt-4 tokenizer if model-specific tokenizer is not found
            encoding = tiktoken.encoding_for_model("gpt-4")

        for message in messages:
            message_token_count = len(encoding.encode(message.get("content")))
            token_count = token_count + message_token_count
            if token_count > model_limit:
                return -1

        return model_limit - token_count

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

        return self.client.chat.completions.create(**NotGiven.remove_not_given(input_kwargs))
