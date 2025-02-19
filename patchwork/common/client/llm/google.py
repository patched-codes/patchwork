from __future__ import annotations

import functools
import time

from google import generativeai
from google.generativeai.types.content_types import (
    add_object_type,
    convert_to_nullable,
    strip_titles,
    unpack_defs,
)
from google.generativeai.types.generation_types import GenerateContentResponse
from google.generativeai.types.model_types import Model
from openai.types import CompletionUsage
from openai.types.chat import (
    ChatCompletionMessage,
    ChatCompletionMessageParam,
    ChatCompletionToolChoiceOptionParam,
    ChatCompletionToolParam,
    completion_create_params,
)
from openai.types.chat.chat_completion import ChatCompletion, Choice
from pydantic_ai.messages import ModelMessage, ModelResponse
from pydantic_ai.models import Model, ModelRequestParameters, StreamedResponse
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai.settings import ModelSettings
from pydantic_ai.usage import Usage
from typing_extensions import Any, AsyncIterator, Dict, Iterable, List, Optional, Union

from patchwork.common.client.llm.protocol import NOT_GIVEN, LlmClient, NotGiven
from patchwork.common.client.llm.utils import json_schema_to_model


@functools.lru_cache
def _cached_list_model_from_google() -> list[Model]:
    return list(generativeai.list_models())


class GoogleLlmClient(LlmClient):
    __SAFETY_SETTINGS = [
        dict(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),
        dict(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
        dict(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),
        dict(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),
    ]
    __MODEL_PREFIX = "models/"

    def __init__(self, api_key: str):
        self.__api_key = api_key
        generativeai.configure(api_key=api_key)

    def __get_pydantic_model(self, model_settings: ModelSettings | None) -> Model:
        if model_settings is None:
            raise ValueError("Model settings cannot be None")
        model_name = model_settings.get("model")
        if model_name is None:
            raise ValueError("Model must be set cannot be None")

        return GeminiModel(model_name, api_key=self.__api_key)

    async def request(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> tuple[ModelResponse, Usage]:
        model = self.__get_pydantic_model(model_settings)
        return await model.request(messages, model_settings, model_request_parameters)

    async def request_stream(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> AsyncIterator[StreamedResponse]:
        model = self.__get_pydantic_model(model_settings)
        yield model.request_stream(messages, model_settings, model_request_parameters)

    @property
    def model_name(self) -> str:
        return "Undetermined"

    @property
    def system(self) -> str:
        return "google-gla"

    def __get_model_limits(self, model: str) -> int:
        for model_info in _cached_list_model_from_google():
            if model_info.name == f"{self.__MODEL_PREFIX}{model}":
                return model_info.input_token_limit
        return 1_000_000

    def get_models(self) -> set[str]:
        return {model.name.removeprefix(self.__MODEL_PREFIX) for model in _cached_list_model_from_google()}

    def is_model_supported(self, model: str) -> bool:
        return model in self.get_models()

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
    ) -> int:
        system, chat = self.__openai_messages_to_google_messages(messages)
        gen_model = generativeai.GenerativeModel(model_name=model, system_instruction=system)
        try:
            token_count = gen_model.count_tokens(chat).total_tokens
        except Exception as e:
            return -1
        model_limit = self.__get_model_limits(model)
        return model_limit - token_count

    def truncate_messages(
        self, messages: Iterable[ChatCompletionMessageParam], model: str
    ) -> Iterable[ChatCompletionMessageParam]:
        return self._truncate_messages(self, messages, model)

    @staticmethod
    def __openai_messages_to_google_messages(
        messages: Iterable[ChatCompletionMessageParam],
    ) -> tuple[str, list[dict[str, Any]]]:
        system_content = None
        contents = []
        for message in messages:
            if message.get("role") == "system":
                system_content = message.get("content")
                continue
            role = "model" if message.get("role") == "assistant" else "user"
            parts = [dict(text=message.get("content"))]
            contents.append(dict(role=role, parts=parts))

        return system_content, contents

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
    ) -> ChatCompletion:
        generation_dict = dict(
            stop_sequences=[stop] if isinstance(stop, str) else stop,
            max_output_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
        )

        is_response_format_given = response_format is not NotGiven and isinstance(response_format, dict)
        is_json_object = is_response_format_given and response_format.get("type") == "json_object"
        is_json_schema = is_response_format_given and response_format.get("type") == "json_schema"
        if is_json_object or is_json_schema:
            generation_dict["response_mime_type"] = "application/json"
        if is_json_schema:
            generation_dict["response_schema"] = self.json_schema_to_google_schema(
                response_format.get("json_schema", {}).get("schema")
            )

        system_content, contents = self.__openai_messages_to_google_messages(messages)

        model_client = generativeai.GenerativeModel(
            model_name=model,
            safety_settings=self.__SAFETY_SETTINGS,
            generation_config=NOT_GIVEN.remove_not_given(generation_dict),
            system_instruction=system_content,
        )
        response = model_client.generate_content(contents=contents)
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

    @staticmethod
    def json_schema_to_google_schema(json_schema: dict[str, Any] | None) -> dict[str, Any] | None:
        if json_schema is None:
            return None

        model = json_schema_to_model(json_schema)
        parameters = model.model_json_schema()
        defs = parameters.pop("$defs", {})

        for name, value in defs.items():
            unpack_defs(value, defs)
        unpack_defs(parameters, defs)
        convert_to_nullable(parameters)
        add_object_type(parameters)
        strip_titles(parameters)
        return parameters
