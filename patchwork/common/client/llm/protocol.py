from __future__ import annotations

from openai.types.chat import (
    ChatCompletion,
    ChatCompletionMessageParam,
    completion_create_params,
)
from typing_extensions import Any, Dict, Iterable, List, Optional, Protocol, Union

from patchwork.common.client.llm.utils import truncate_message


class NotGiven:
    ...

    @staticmethod
    def remove_not_given(obj: Any) -> Any:
        if isinstance(obj, NotGiven):
            return None
        if isinstance(obj, dict):
            return {k: NotGiven.remove_not_given(v) for k, v in obj.items() if v is not NOT_GIVEN}
        if isinstance(obj, list):
            return [NotGiven.remove_not_given(v) for v in obj if v is not NOT_GIVEN]
        return obj


NOT_GIVEN = NotGiven()


class LlmClient(Protocol):
    def get_models(self) -> set[str]:
        ...

    def is_model_supported(self, model: str) -> bool:
        ...

    def is_prompt_supported(self, messages: Iterable[ChatCompletionMessageParam], model: str) -> int:
        ...

    def truncate_messages(
        self, messages: Iterable[ChatCompletionMessageParam], model: str
    ) -> Iterable[ChatCompletionMessageParam]:
        ...

    @staticmethod
    def _truncate_messages(
        client: "LlmClient", messages: Iterable[ChatCompletionMessageParam], model: str
    ) -> Iterable[ChatCompletionMessageParam]:
        last_message = None
        truncated_messages = []
        for message in messages:
            future_truncated_messages = truncated_messages.copy()
            future_truncated_messages.append(message)
            if client.is_prompt_supported(future_truncated_messages, model) < 0:
                last_message = message
                break
            truncated_messages.append(message)

        def direction_callback(message: str) -> int:
            return client.is_prompt_supported([{"content": message}], model)

        if last_message is not None:
            last_message["content"] = truncate_message(last_message["content"], direction_callback)
            truncated_messages.append(last_message)

        return truncated_messages

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
        response_format: str | completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion:
        ...
