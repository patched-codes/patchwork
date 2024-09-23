from __future__ import annotations

from openai.types.chat import (
    ChatCompletion,
    ChatCompletionMessageParam,
    completion_create_params,
)
from typing_extensions import Dict, Iterable, List, Optional, Union

from patchwork.common.client.llm.protocol import NOT_GIVEN, LlmClient, NotGiven
from patchwork.logger import logger


class AioLlmClient(LlmClient):
    def __init__(self, *clients: LlmClient):
        self.__original_clients = clients
        self.__clients = []
        self.__supported_models = set()
        for client in clients:
            try:
                self.__supported_models.update(client.get_models())
                self.__clients.append(client)
            except Exception:
                pass

    def get_models(self) -> set[str]:
        return self.__supported_models

    def is_model_supported(self, model: str) -> bool:
        return any(client.is_model_supported(model) for client in self.__clients)

    def is_prompt_supported(self, messages: Iterable[ChatCompletionMessageParam], model: str) -> bool:
        for client in self.__clients:
            if client.is_model_supported(model):
                return client.is_prompt_supported(messages, model)
        return False

    def truncate_messages(
        self, messages: Iterable[ChatCompletionMessageParam], model: str
    ) -> Iterable[ChatCompletionMessageParam]:
        for client in self.__clients:
            if client.is_model_supported(model):
                return client.truncate_messages(messages, model)
        return messages

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
        for client in self.__clients:
            if client.is_model_supported(model):
                logger.debug(f"Using {client.__class__.__name__} for model {model}")
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
        client_names = [client.__class__.__name__ for client in self.__original_clients]
        raise ValueError(
            f"Model {model} is not supported by {client_names} clients. "
            f"Please ensure that the respective API keys are correct."
        )
