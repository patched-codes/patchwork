from __future__ import annotations

import time

from patchwork.common.client.llm.protocol import LlmClient
from anthropic import Anthropic
from anthropic.types import Message
from openai.types.chat import ChatCompletion, ChatCompletionMessage
from openai.types.chat.chat_completion import Choice, CompletionUsage
from openai.types.completion_usage import CompletionUsage

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
    allowed_model_prefixes = {"claude-3-"}

    def __init__(self, api_key: str):
        self.client = Anthropic(api_key=api_key)

    def get_models(self) -> set[str]:
        return {"claude-2.0", "claude-2.1", "claude-instant-1.2"}

    def contains_pattern_based_model(self) -> bool:
        return True

    def is_model_supported(self, model: str) -> bool:
        return model in self.get_models() or any(model.startswith(prefix) for prefix in self.allowed_model_prefixes)

    def chat_completion(self, model: str, **kwargs) -> ChatCompletion:
        response = self.client.messages.create(model=model, **kwargs)
        return _anthropic_to_openai_response(model, response)
