from __future__ import annotations

from functools import lru_cache

from openai.types.chat import (
    ChatCompletion,
    ChatCompletionMessageParam,
    completion_create_params,
)
from typing_extensions import Dict, Iterable, List, Optional, Union

from patchwork.common.client.llm.protocol import NOT_GIVEN, LlmClient, NotGiven


class AioLlmClient(LlmClient):
    def __init__(self, *clients: LlmClient):
        self.clients = clients

    @lru_cache(maxsize=None)
    def get_models(self) -> set[str]:
        return set().union(*[client.get_models() for client in self.clients])

    def is_model_supported(self, model: str) -> bool:
        return any(client.is_model_supported(model) for client in self.clients)

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
        for client in self.clients:
            if client.is_model_supported(model):
                return client.chat_completion(
                    messages,
                    model,
                    frequency_penalty,
                    logit_bias,
                    logprobs,
                    max_tokens,
                    n,
                    presence_penalty,
                    response_format,
                    stop,
                    temperature,
                    top_logprobs,
                    top_p,
                )
        raise ValueError(f"Model {model} is not supported by {[client.__class__.__name__ for client in self.clients]} clients")
