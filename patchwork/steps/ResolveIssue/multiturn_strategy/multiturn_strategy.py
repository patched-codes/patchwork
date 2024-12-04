from __future__ import annotations

import json
import logging
import sys
from abc import ABC, abstractmethod
from json import JSONDecodeError

from openai.types.chat.chat_completion_message import ChatCompletionMessage
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam
from openai.types.chat.chat_completion_tool_param import ChatCompletionToolParam

from patchwork.steps.ResolveIssue.tools.tool import Tool

logger = logging.getLogger("patched")


class MultiturnStrategy(ABC):
    def __init__(self, tool_set: dict[str, Tool], limit: int | None = None, *args, **kwargs):
        self.tool_set = tool_set
        self.limit = limit
        self.run_count = 0

    def get_tools_spec(self) -> list[ChatCompletionToolParam]:
        return [
            dict(
                type="function",
                function=dict(name=k, **v.json_schema),
            )
            for k, v in self.tool_set.items()
        ]

    @abstractmethod
    def run_initial_prompt(self) -> list[ChatCompletionMessageParam]:
        pass

    @abstractmethod
    def run_subsequent_prompt(self, messages: list[ChatCompletionMessageParam]) -> ChatCompletionMessage:
        pass

    def is_stop(self, messages: list[ChatCompletionMessageParam]) -> bool:
        return False

    def execute_tools(self, chat_completion_message: ChatCompletionMessageParam) -> list[ChatCompletionMessageParam]:
        rv = []
        for tool_call in chat_completion_message.tool_calls:
            tooling_to_use = self.tooling.get(tool_call.function.name, None)
            if tooling_to_use is None:
                logging.info("LLM just used an non-existent tool!")
                continue

            logging.info(f"Running tool: {tool_call.function.name}")
            try:
                tool_kwargs = json.loads(tool_call.function.arguments)
                tooling_output = tooling_to_use.execute(**tool_kwargs)
            except JSONDecodeError:
                tooling_output = "Arguments must be passed through a valid JSON object"

            rv.append({"tool_call_id": tool_call.id, "role": "tool", "content": tooling_output})

        return rv

    def execute(self, limit: int | None = None) -> None:
        messages = self.run_initial_prompt()
        try:
            for i in range(limit or self.limit or sys.maxsize):
                self.run_count = i + 1
                if self.is_stop(messages):
                    break
                messages = self.run_subsequent_prompt(messages)
        except Exception as e:
            logging.error(e)
        finally:
            self.run_count = 0
