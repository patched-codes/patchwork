from __future__ import annotations

from functools import lru_cache

from openai import OpenAI
from openai._streaming import Stream
from openai.types.chat import ChatCompletion, ChatCompletionChunk

from patchwork.common.client.llm.protocol import LlmClient


class OpenAiLlmClient(LlmClient):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = OpenAI(api_key=api_key)

    @lru_cache(maxsize=None)
    def get_models(self) -> set[str]:
        sync_page = self.client.models.list()

        models = set()
        for pages in sync_page.iter_pages():
            models.update(map(lambda x: x.id, pages.data))

        return models

    def contains_pattern_based_model(self) -> bool:
        return False

    def is_model_supported(self, model: str) -> bool:
        return model in self.get_models()

    def chat_completion(self, model: str, **kwargs) -> ChatCompletion | Stream[ChatCompletionChunk]:
        return self.client.chat.completions.create(
            model=model,
            **kwargs,
        )
