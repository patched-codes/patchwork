from __future__ import annotations

import time
from functools import lru_cache

from anthropic import Anthropic
from anthropic.types import Message, TextBlockParam
from openai.types.chat import (
    ChatCompletion,
    ChatCompletionMessage,
    ChatCompletionMessageParam,
    completion_create_params,
)
from openai.types.chat.chat_completion import Choice, CompletionUsage
from openai.types.completion_usage import CompletionUsage
from typing_extensions import Dict, Iterable, List, Optional, Union

from patchwork.common.client.llm.protocol import NOT_GIVEN, LlmClient, NotGiven


def _anthropic_to_openai_response(model: str, anthropic_response: Message) -> ChatCompletion:
    choices = []
    for i, content_block in enumerate(anthropic_response.content):
        choice = Choice(
            index=i,
            finish_reason=anthropic_response.stop_reason,
            message=ChatCompletionMessage(
                role="assistant",
                content=content_block.text,
            ),
        )
        choices.append(choice)

    return ChatCompletion(
        id=anthropic_response.id,
        choices=choices,
        created=int(time.time()),
        model=model,
        object="chat.completion",
        usage=CompletionUsage(
            completion_tokens=anthropic_response.usage.output_tokens,
            prompt_tokens=anthropic_response.usage.input_tokens,
            total_tokens=anthropic_response.usage.output_tokens + anthropic_response.usage.input_tokens,
        ),
    )


class AnthropicLlmClient(LlmClient):
    __allowed_model_prefix = "claude-3-"
    __definitely_allowed_models = {"claude-2.0", "claude-2.1", "claude-instant-1.2"}

    def __init__(self, api_key: str):
        self.client = Anthropic(api_key=api_key)

    @lru_cache(maxsize=None)
    def get_models(self) -> set[str]:
        return self.__definitely_allowed_models.union(set(f"{self.__allowed_model_prefix}*"))

    def is_model_supported(self, model: str) -> bool:
        return model in self.__definitely_allowed_models or model.startswith(self.__allowed_model_prefix)

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
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion:
        system: Union[str, Iterable[TextBlockParam]] | NotGiven = NOT_GIVEN
        other_messages = []
        for message in messages:
            if message.role == "system":
                if system is NOT_GIVEN:
                    system = list()
                system.append(TextBlockParam(text=message.content, type="text"))
            else:
                other_messages.append(TextBlockParam(text=message.content, type="text"))

        input_kwargs = dict(
            messages=other_messages,
            system=system,
            max_tokens=max_tokens,
            model=model,
            stop_sequences=[stop] if isinstance(stop, str) else stop,
            temperature=temperature,
            top_k=top_logprobs if logprobs else NOT_GIVEN,
            top_p=top_p,
        )

        response = self.client.messages.create(**NotGiven.remove_not_given(input_kwargs))
        return _anthropic_to_openai_response(model, response)
