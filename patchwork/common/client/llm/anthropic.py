from __future__ import annotations

import json
import time
from functools import cached_property
from pathlib import Path

from anthropic import Anthropic
from anthropic.types import Message, MessageParam, TextBlockParam
from openai.types.chat import (
    ChatCompletion,
    ChatCompletionMessage,
    ChatCompletionMessageParam,
    ChatCompletionToolChoiceOptionParam,
    ChatCompletionToolParam,
    completion_create_params,
)
from openai.types.chat.chat_completion import Choice
from openai.types.chat.chat_completion_message_tool_call import (
    ChatCompletionMessageToolCall,
    Function,
)
from openai.types.completion_usage import CompletionUsage
from pydantic_ai.messages import ModelMessage, ModelResponse
from pydantic_ai.models import Model, ModelRequestParameters, StreamedResponse
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.settings import ModelSettings
from pydantic_ai.usage import Usage
from typing_extensions import AsyncIterator, Dict, Iterable, List, Optional, Union

from patchwork.common.client.llm.protocol import NOT_GIVEN, LlmClient, NotGiven


def _anthropic_to_openai_response(model: str, anthropic_response: Message) -> ChatCompletion:
    stop_reason_map = {"end_turn": "stop", "max_tokens": "length", "stop_sequence": "stop", "tool_use": "tool_calls"}

    choices = []
    for i, content_block in enumerate(anthropic_response.content):
        if content_block.type == "text":
            chat_completion_message = ChatCompletionMessage(
                role="assistant",
                content=content_block.text,
            )
        else:
            text = json.dumps(content_block.input)
            chat_completion_message = ChatCompletionMessage(
                role="assistant",
                content=text,
                tool_calls=[
                    ChatCompletionMessageToolCall(
                        id=content_block.id, type="function", function=Function(name=content_block.name, arguments=text)
                    )
                ],
            )
        choice = Choice(
            index=i,
            finish_reason=stop_reason_map.get(anthropic_response.stop_reason, "stop"),
            message=chat_completion_message,
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
    __allowed_model_prefix = "claude-3-"
    __definitely_allowed_models = {"claude-2.0", "claude-2.1", "claude-instant-1.2"}
    __100k_models = {"claude-2.0", "claude-instant-1.2"}

    def __init__(self, api_key: str):
        self.__api_key = api_key

    @cached_property
    def __client(self):
        return Anthropic(api_key=self.__api_key)

    def __get_pydantic_model(self, model_settings: ModelSettings | None) -> Model:
        if model_settings is None:
            raise ValueError("Model settings cannot be None")
        model_name = model_settings.get("model")
        if model_name is None:
            raise ValueError("Model must be set cannot be None")

        return AnthropicModel(model_name, api_key=self.__api_key)

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
        return "anthropic"

    def __get_model_limit(self, model: str) -> int:
        # it is observed that the count tokens is not accurate, so we are using a safety margin
        # we usually see 40k tokens overestimation on large prompts
        safety_margin = 40_000
        if model in self.__100k_models:
            return 100_000 - safety_margin
        return 200_000 - safety_margin

    def __adapt_input_messages(self, messages: Iterable[ChatCompletionMessageParam]) -> list[MessageParam]:
        system = NOT_GIVEN
        new_messages = []
        for message in messages:
            if message.get("role") == "system":
                if system is NOT_GIVEN:
                    system = list()
                system.append(TextBlockParam(text=message.get("content"), type="text"))
            elif message.get("role") == "tool":
                new_messages.append(
                    dict(
                        role="user",
                        content=[
                            dict(
                                type="tool_result",
                                tool_use_id=message.get("tool_call_id"),
                                content=message.get("content"),
                            )
                        ],
                    )
                )
            elif message.get("role") == "assistant" and len(message.get("tool_calls", [])) > 0:
                tool_calls = message["tool_calls"]
                tool_calls_as_content = [
                    dict(
                        type="tool_use",
                        id=tool_call["id"],
                        name=tool_call["function"]["name"],
                        input=json.loads(tool_call["function"]["arguments"]),
                    )
                    for tool_call in tool_calls
                ]
                new_messages.append(
                    dict(
                        role="assistant",
                        content=[
                            *tool_calls_as_content,
                        ],
                    )
                )
            else:
                new_messages.append(message)

        return new_messages

    def __adapt_chat_completion_request(
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
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
    ):
        system: Union[str, Iterable[TextBlockParam]] | NotGiven = NOT_GIVEN
        adapted_messages = self.__adapt_input_messages(messages)
        default_max_token = 1000

        if tool_choice is not NOT_GIVEN:
            # openai tool choice to anthropic tool choice mapping:
            # openai   : none, auto, required , required
            # anthropic: NA  , auto, any      , tool
            if isinstance(tool_choice, str):
                if tool_choice == "required":
                    tool_choice = dict(type="any")
                elif tool_choice == "none":
                    tool_choice = NOT_GIVEN
                else:
                    tool_choice = dict(type=tool_choice)
            else:
                tool_choice_type = tool_choice.get("type")
                if tool_choice_type == "required":
                    if tool_choice.get("function") is not None:
                        tool_choice["type"] = "tool"
                        tool_choice["name"] = tool_choice["function"]["name"]
                    else:
                        tool_choice["type"] = "any"
                elif tool_choice_type == "none":
                    tool_choice = NOT_GIVEN

        anthropic_tools = NOT_GIVEN
        if tools is not None and tools is not NOT_GIVEN:
            anthropic_tools = [tool.get("function") for tool in tools if tool.get("function") is not None]
        input_kwargs = dict(
            messages=adapted_messages,
            system=system,
            max_tokens=default_max_token if max_tokens is None or max_tokens is NOT_GIVEN else max_tokens,
            model=model,
            stop_sequences=[stop] if isinstance(stop, str) else stop,
            temperature=temperature,
            tools=anthropic_tools,
            tool_choice=tool_choice,
            top_p=top_p,
        )

        if response_format is not NOT_GIVEN and response_format.get("type") == "json_schema":
            input_kwargs["tool_choice"] = dict(type="tool", name="response_format")
            if input_kwargs.get("tools") is NOT_GIVEN:
                input_kwargs["tools"] = list()
            response_format_tool = dict(
                name="response_format",
                description="The response format to use",
                input_schema=response_format["json_schema"]["schema"],
            )
            input_kwargs["tools"] = [*input_kwargs["tools"], response_format_tool]

        return NotGiven.remove_not_given(input_kwargs)

    def test(self):
        return

    def is_model_supported(self, model: str) -> bool:
        return model in self.__definitely_allowed_models or model.startswith(self.__allowed_model_prefix)

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
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        file: Path | NotGiven = NOT_GIVEN,
    ) -> int:
        model_limit = self.__get_model_limit(model)
        input_kwargs = self.__adapt_chat_completion_request(
            messages=messages,
            model=model,
            frequency_penalty=frequency_penalty,
            logit_bias=logit_bias,
            logprobs=logprobs,
            max_tokens=max_tokens,
            n=n,
            presence_penalty=presence_penalty,
            response_format=response_format,
            stop=stop,
            temperature=temperature,
            tools=tools,
            tool_choice=tool_choice,
            top_logprobs=top_logprobs,
            top_p=top_p,
        )
        count_token_input_kwargs = {
            k: v
            for k, v in input_kwargs.items()
            if k in {"messages", "model", "system", "tool_choice", "tools", "beta"}
        }
        message_token_count = self.__client.beta.messages.count_tokens(**count_token_input_kwargs)
        return model_limit - message_token_count.input_tokens

    def truncate_messages(
        self, messages: Iterable[ChatCompletionMessageParam], model: str
    ) -> Iterable[ChatCompletionMessageParam]:
        return self._truncate_messages(self, messages, model)

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
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        file: Path | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion:
        input_kwargs = self.__adapt_chat_completion_request(
            messages=messages,
            model=model,
            frequency_penalty=frequency_penalty,
            logit_bias=logit_bias,
            logprobs=logprobs,
            max_tokens=max_tokens,
            n=n,
            presence_penalty=presence_penalty,
            response_format=response_format,
            stop=stop,
            temperature=temperature,
            tools=tools,
            tool_choice=tool_choice,
            top_logprobs=top_logprobs,
            top_p=top_p,
        )

        response = self.__client.messages.create(**input_kwargs)
        return _anthropic_to_openai_response(model, response)
