from __future__ import annotations

from abc import abstractmethod
from pathlib import Path

from openai.types.chat import (
    ChatCompletion,
    ChatCompletionMessageParam,
    ChatCompletionToolChoiceOptionParam,
    ChatCompletionToolParam,
    completion_create_params,
)
from pydantic_ai.models import Model
from typing_extensions import Any, Dict, Iterable, List, Optional, Union


class NotGiven:
    ...

    @staticmethod
    def remove_not_given(obj: Any) -> Union[None, dict[Any, Any], list[Any], Any]:
        if isinstance(obj, NotGiven):
            return None
        if isinstance(obj, dict):
            return {k: NotGiven.remove_not_given(v) for k, v in obj.items() if v is not NOT_GIVEN}
        if isinstance(obj, list):
            return [NotGiven.remove_not_given(v) for v in obj if v is not NOT_GIVEN]
        return obj


NOT_GIVEN = NotGiven()


class LlmClient(Model):
    @abstractmethod
    def test(self) -> None:
        ...

    @abstractmethod
    def is_model_supported(self, model: str) -> bool:
        ...

    @abstractmethod
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
        ...

    @abstractmethod
    def truncate_messages(
        self, messages: Iterable[ChatCompletionMessageParam], model: str
    ) -> Iterable[ChatCompletionMessageParam]:
        ...

    @staticmethod
    def _truncate_messages(
        client: "LlmClient", messages: Iterable[ChatCompletionMessageParam], model: str
    ) -> Iterable[ChatCompletionMessageParam]:
        safety_margin = 500

        last_message = None
        truncated_messages = []
        for message in messages:
            future_truncated_messages = truncated_messages.copy()
            future_truncated_messages.append(message)
            if client.is_prompt_supported(future_truncated_messages, model) - safety_margin < 0:
                last_message = message
                break
            truncated_messages.append(message)

        if last_message is not None:

            def direction_callback(message_to_test: str) -> int:
                current_messages = truncated_messages.copy()
                current_messages.append({"content": message_to_test})
                # add 500 as a safety margin
                return client.is_prompt_supported(current_messages, model) - safety_margin

            last_message["content"] = LlmClient.__truncate_message(
                message=last_message["content"],
                direction_callback=direction_callback,
                min_guess=1,
                max_guess=len(last_message["content"]),
            )
            truncated_messages.append(last_message)

        return truncated_messages

    @staticmethod
    def __truncate_message(message, direction_callback, min_guess, max_guess):
        # TODO: Add tests for truncate_message
        # if __name__ == "__main__":
        # import random
        # import string
        # for i in range(1, 1000):
        #     text = "".join(random.choices(string.ascii_lowercase, k=random.choice(range(i, i + 20))))
        #     print(f"Truncating {text} to {text[:i]}")
        #     new = truncate_message(text, lambda x: i - len(x))
        #     assert text[:i] == new
        #     print(f"Truncated {text} to {new}")
        change = int((max_guess - min_guess) / 2)
        guess = min_guess + change
        vector = direction_callback(message[:guess])
        if vector == 0:
            return message[:guess]

        if vector > 0:
            min_guess = guess
        else:
            max_guess = guess

        return LlmClient.__truncate_message(message, direction_callback, min_guess, max_guess)

    @abstractmethod
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
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        file: Path | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion:
        ...
