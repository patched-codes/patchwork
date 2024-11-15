from __future__ import annotations

import functools

import tiktoken
from openai import OpenAI
from openai.types.chat import (
    ChatCompletion,
    ChatCompletionMessageParam,
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
        "gpt-4	": 8_192,
        "gpt-4-turbo": 8_192,
        "o1-preview": 128_000,
        "o1-mini": 128_000,
        "gpt-4o-mini": 128_000,
        "gpt-4o": 128_000,
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

    def is_prompt_supported(self, messages: Iterable[ChatCompletionMessageParam], model: str) -> int:
        # might not implement model endpoint
        if self.__is_not_openai_url():
            return 1

        model_limit = self.__get_model_limits(model)
        token_count = 0
        encoding = tiktoken.encoding_for_model(model)
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
            top_logprobs=top_logprobs,
            top_p=top_p,
        )

        is_json_output_required = response_format is not NOT_GIVEN and response_format.get("type") in [
            "json_object",
            "json_schema",
        ]
        if model.startswith("o1") and is_json_output_required:
            return self.__o1_chat_completion(**input_kwargs)

        return self.client.chat.completions.create(**NotGiven.remove_not_given(input_kwargs))

    def __o1_chat_completion(
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
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
    ):
        o1_messages = list(messages)
        if response_format.get("type") == "json_schema":
            last_msg_idx = len(o1_messages) - 1
            last_msg = o1_messages[last_msg_idx]
            last_msg["content"] = (
                last_msg["content"]
                + f"""
Respond with the following json schema in mind:
{response_format.get('json_schema')}
"""
            )
        o1_input_kwargs = dict(
            messages=o1_messages,
            model=model,
            frequency_penalty=frequency_penalty,
            logit_bias=logit_bias,
            logprobs=logprobs,
            max_tokens=max_tokens,
            n=n,
            presence_penalty=presence_penalty,
            stop=stop,
            temperature=temperature,
            top_logprobs=top_logprobs,
            top_p=top_p,
        )

        o1_response = self.client.chat.completions.create(**NotGiven.remove_not_given(o1_input_kwargs))

        o1_choices_parser_responses = []
        for o1_choice in o1_response.choices:
            parser_input_kwargs = dict(
                messages=[
                    {
                        "role": "user",
                        "content": f"Given the following data, format it with the given response format: {o1_choice.message.content}",
                    }
                ],
                model="gpt-4o-mini",
                max_tokens=max_tokens,
                n=1,
                response_format=response_format,
            )
            parser_response = self.client.beta.chat.completions.parse(**NotGiven.remove_not_given(parser_input_kwargs))
            o1_choices_parser_responses.append(parser_response)

        reconstructed_response = o1_response.model_copy()
        for i, o1_choices_parser_response in enumerate(o1_choices_parser_responses):
            if reconstructed_response.usage is not None:
                reconstructed_response.usage.completion_tokens += o1_choices_parser_response.usage.completion_tokens
                reconstructed_response.usage.prompt_tokens += o1_choices_parser_response.usage.prompt_tokens
                reconstructed_response.usage.total_tokens += o1_choices_parser_response.usage.total_tokens
            reconstructed_response.choices[i].message.content = o1_choices_parser_response.choices[0].message.content

        return reconstructed_response
