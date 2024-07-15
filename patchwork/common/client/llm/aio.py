from __future__ import annotations
from functools import lru_cache

from patchwork.common.client.llm.protocol import LlmClient
from openai._streaming import Stream
from openai.types.chat import ChatCompletion, ChatCompletionChunk


class AioLlmClient(LlmClient):
    def __init__(self, *clients: LlmClient):
        self.clients = clients

    @lru_cache(maxsize=None)
    def get_models(self) -> set[str]:
        return set().union(*[client.get_models() for client in self.clients])

    def contains_pattern_based_model(self) -> bool:
        return any(client.contains_pattern_based_model() for client in self.clients)

    def is_model_supported(self, model: str) -> bool:
        return any(client.is_model_supported(model) for client in self.clients)

    def chat_completion(self, model: str, **kwargs) -> ChatCompletion | Stream[ChatCompletionChunk]:
        for client in self.clients:
            if client.is_model_supported(model):
                return client.chat_completion(model, **kwargs)
        raise ValueError(f"Model {model} is not supported by any client")
