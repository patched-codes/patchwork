from __future__ import annotations

from openai._streaming import Stream
from openai.types.chat import ChatCompletion, ChatCompletionChunk
from typing_extensions import Protocol


class LlmClient(Protocol):
    def get_models(self) -> set[str]:
        ...

    def contains_pattern_based_model(self) -> bool:
        ...

    def is_model_supported(self, model: str) -> bool:
        ...

    def chat_completion(self, model: str, **kwargs) -> ChatCompletion | Stream[ChatCompletionChunk]:
        ...
