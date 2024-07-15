from __future__ import annotations

import time
from functools import lru_cache

from google.ai.generativelanguage_v1.services import model_service, generative_service
from google.ai.generativelanguage_v1 import GenerateContentRequest, ListModelsRequest, GenerateContentResponse
from patchwork.common.client.llm.protocol import LlmClient
from openai.types.chat import ChatCompletionMessage
from openai.types.chat.chat_completion import ChatCompletion, Choice
from openai.types import CompletionUsage


def _google_response_to_openai_response(google_response: GenerateContentResponse, model: str) -> ChatCompletion:
    choices = []
    for candidate in google_response.candidates:
        # note that instead of system, from openai, its model, from google.
        role = candidate.content.role
        parts = [part.text or part.inline_data for part in candidate.content.parts]

        choice = Choice(
            finish_reason=candidate.finish_reason,
            index=candidate.index,
            message=ChatCompletionMessage(
                content="\n".join(parts),
                role=role,
            ),
        )
        choices.append(choice)

    completion_usage = CompletionUsage(
        completion_tokens=google_response.usage_metadata.candidates_token_count,
        prompt_tokens=google_response.usage_metadata.prompt_token_count,
        total_tokens=google_response.usage_metadata.total_token_count,
    )

    return ChatCompletion(
        id=-1,
        choices=choices,
        created=int(time.time()),
        model=model,
        object="chat.completion",
        usage=completion_usage,
    )


class GoogleLlmClient(LlmClient):
    __SAFETY_SETTINGS = [
        dict(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),
        dict(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
        dict(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),
        dict(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),
    ]

    def __init__(self, api_key: str):
        self.model_client = model_service.ModelServiceClient(client_options=dict(
            api_key=api_key,
            # quota_project_id="",
        ))
        self.generative_client = generative_service.GenerativeServiceClient(client_options=dict(
            api_key=api_key,
            # quota_project_id="",
        ))

    @lru_cache(maxsize=None)
    def get_models(self) -> set[str]:
        request = ListModelsRequest()
        response = self.model_client.list_models(request)

        models = set()
        for page in response.pages:
            models.update(map(lambda x: x.name, page.models))

        return models

    def contains_pattern_based_model(self) -> bool:
        return False

    def is_model_supported(self, model: str) -> bool:
        return model in self.get_models()

    def chat_completion(self, model: str, **kwargs) -> ChatCompletion:
        request_kwargs = dict(model=model, safety_settings=self.__SAFETY_SETTINGS, **kwargs)
        request = GenerateContentRequest(**request_kwargs)

        response = self.generative_client.generate_content(request)
        return _google_response_to_openai_response(response, model)
