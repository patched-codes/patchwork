from __future__ import annotations

import time
from functools import lru_cache

from google.ai.generativelanguage_v1 import GenerateContentResponse
from google.ai.generativelanguage_v1.services import generative_service, model_service
from google.ai.generativelanguage_v1.types import (
    GenerateContentRequest,
    GenerationConfig,
    ListModelsRequest,
)
from openai.types import CompletionUsage
from openai.types.chat import (
    ChatCompletion,
    ChatCompletionMessage,
    ChatCompletionMessageParam,
    completion_create_params,
)
from openai.types.chat.chat_completion import ChatCompletion, Choice
from typing_extensions import Dict, Iterable, List, Optional, Union

from patchwork.common.client.llm.protocol import NOT_GIVEN, LlmClient, NotGiven


class GoogleLlmClient(LlmClient):
    __SAFETY_SETTINGS = [
        dict(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),
        dict(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
        dict(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),
        dict(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),
    ]

    def __init__(self, api_key: str):
        self.model_client = model_service.ModelServiceClient(
            client_options=dict(
                api_key=api_key,
                # quota_project_id="",
            )
        )
        self.generative_client = generative_service.GenerativeServiceClient(
            client_options=dict(
                api_key=api_key,
                # quota_project_id="",
            )
        )

    @lru_cache(maxsize=None)
    def __get_true_model_names(self) -> set[str]:
        request = ListModelsRequest()
        response = self.model_client.list_models(request)

        models = set()
        for page in response.pages:
            models.update(map(lambda x: x.name, page.models))

        return models

    @staticmethod
    def __handle_model_name(model_name) -> str:
        _, _, model = model_name.rpartition("/")
        return model

    @lru_cache(maxsize=None)
    def get_models(self) -> set[str]:
        models = self.__get_true_model_names()
        return set(map(self.__handle_model_name, models))

    def __get_true_model_name(self, model: str) -> str | None:
        true_model_names = self.__get_true_model_names()
        for true_model_name in true_model_names:
            if true_model_name.endswith(model):
                return true_model_name
        return None

    def is_model_supported(self, model: str) -> bool:
        return self.__get_true_model_name(model) is not None

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
        generation_config = GenerationConfig(
            NotGiven.remove_not_given(
                dict(
                    stop_sequences=[stop] if isinstance(stop, str) else stop,
                    max_output_tokens=max_tokens,
                    temperature=temperature,
                    top_p=top_p,
                )
            )
        )

        contents = []
        for message in messages:
            role = "model" if message.get("role") in {"system", "assistant"} else "user"
            parts = [dict(text=message.get("content"))]
            contents.append(dict(role=role, parts=parts))

        request_kwargs = dict(
            contents=contents,
            model=self.__get_true_model_name(model),
            safety_settings=self.__SAFETY_SETTINGS,
            generation_config=generation_config,
        )
        request = GenerateContentRequest(request_kwargs)

        response = self.generative_client.generate_content(request)
        return self.__google_response_to_openai_response(response, model)

    @staticmethod
    def __google_response_to_openai_response(google_response: GenerateContentResponse, model: str) -> ChatCompletion:
        choices = []
        for candidate in google_response.candidates:
            # note that instead of system, from openai, its model, from google.
            parts = [part.text or part.inline_data for part in candidate.content.parts]

            # google reasons by index = [FINISH_REASON_UNSPECIFIED, STOP, MAX_TOKENS, SAFETY, RECITATION, OTHER]
            # openai allowed reasons: 'stop', 'length', 'tool_calls', 'content_filter', 'function_call'
            finish_reason_map = {
                2: "length",
                3: "content_filter",
            }

            choice = Choice(
                finish_reason=finish_reason_map.get(candidate.finish_reason, "stop"),
                index=candidate.index,
                message=ChatCompletionMessage(
                    content="\n".join(parts),
                    role="assistant",
                ),
            )
            choices.append(choice)

        completion_usage = CompletionUsage(
            completion_tokens=google_response.usage_metadata.candidates_token_count,
            prompt_tokens=google_response.usage_metadata.prompt_token_count,
            total_tokens=google_response.usage_metadata.total_token_count,
        )

        return ChatCompletion(
            id="-1",
            choices=choices,
            created=int(time.time()),
            model=model,
            object="chat.completion",
            usage=completion_usage,
        )
