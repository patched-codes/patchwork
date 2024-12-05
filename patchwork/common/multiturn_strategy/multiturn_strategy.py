from __future__ import annotations

import json
import logging
import sys
from abc import ABC, abstractmethod
from json import JSONDecodeError

from openai.types.chat.chat_completion_message import ChatCompletionMessage
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam
from openai.types.chat.chat_completion_tool_param import ChatCompletionToolParam

from patchwork.common.tools import Tool


class MultiturnStrategy(ABC):
    def __init__(self, tool_set: dict[str, Tool], limit: int | None = None, *args, **kwargs):
        self.tool_set = tool_set
        self.limit = limit
        self.run_count = 0

    def get_tools_spec(self) -> list[ChatCompletionToolParam]:
        return [
            dict(
                type="function",
                function={"name": k, **v.json_schema},
            )
            for k, v in self.tool_set.items()
        ]

    @abstractmethod
    def run_initial_prompt(self) -> tuple[ChatCompletionMessage, list[ChatCompletionMessageParam]]:
        pass

    @abstractmethod
    def run_subsequent_prompt(self, messages: list[ChatCompletionMessageParam]) -> list[ChatCompletionMessageParam]:
        pass

    def is_stop(self, messages: list[ChatCompletionMessageParam]) -> bool:
        return False

    def execute_tools(self, last_message: ChatCompletionMessageParam) -> list[ChatCompletionMessageParam]:
        rv = []
        for tool_call in last_message.get("tool_calls", []):
            tool_name_to_use = tool_call.get("function", {}).get("name")
            tool_to_use = self.tool_set.get(tool_name_to_use, None)
            if tool_to_use is None:
                logging.info("LLM just used an non-existent tool!")
                continue

            logging.info(f"Running tool: {tool_name_to_use}")
            try:
                tool_arguments = tool_call.get("function", {}).get("arguments", "{}")
                tool_kwargs = json.loads(tool_arguments)
                tool_output = tool_to_use.execute(**tool_kwargs)
            except JSONDecodeError:
                tool_output = "Arguments must be passed through a valid JSON object"

            rv.append({"tool_call_id": tool_call.get("id", ""), "role": "tool", "content": tool_output})

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
