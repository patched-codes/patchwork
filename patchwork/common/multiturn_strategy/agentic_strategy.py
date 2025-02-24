from __future__ import annotations

import abc
import json
import logging
import random
import string
import sys
from json import JSONDecodeError
from pathlib import Path

import chevron
from openai.types.chat import ChatCompletionMessageParam
from openai.types.chat.chat_completion_tool_param import ChatCompletionToolParam

from patchwork.common.client.llm.protocol import LlmClient
from patchwork.common.tools import CodeEditTool, Tool
from patchwork.common.tools.agentic_tools import EndTool


class Role(abc.ABC):
    def __init__(self, llm_client: LlmClient, tool_set: dict[str, Tool]):
        self.llm_client = llm_client
        self.tool_set = tool_set
        self.history: list[ChatCompletionMessageParam] = []
        self.request_tokens = 0
        self.response_tokens = 0

    def generate_reply(self, message: str) -> str:
        self.history.append(dict(role="user", content=message))
        input_kwargs = dict(
            messages=self.history,
            model="claude-3-5-sonnet-latest",
            tools=self.__get_tools_spec(),
            max_tokens=8096,
        )
        is_prompt_safe = self.llm_client.is_prompt_supported(**input_kwargs)
        if is_prompt_safe < 0:
            raise ValueError("The subsequent prompt is not supported, due to large size.")
        response = self.llm_client.chat_completion(**input_kwargs)
        self.response_tokens = response.usage.completion_tokens
        self.request_tokens = response.usage.prompt_tokens

        choices = response.choices or []

        message_content = ""
        for choice in choices:
            new_message = choice.message.to_dict()
            self.history.append(new_message)
            if new_message.get("tool_calls") is not None:
                self.history.extend(self.__execute_tools(new_message))
            else:
                message_content = new_message["content"]

        return message_content

    def __execute_tools(self, last_message: ChatCompletionMessageParam) -> list[ChatCompletionMessageParam]:
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

    def __get_tools_spec(self) -> list[ChatCompletionToolParam]:
        return [
            dict(
                type="function",
                function={"name": k, **v.json_schema},
            )
            for k, v in self.tool_set.items()
        ]


class UserProxy(Role):
    def __init__(
        self, llm_client: LlmClient, tool_set: dict[str, Tool], system_prompt: str = None, reply_message: str = ""
    ):
        super().__init__(llm_client, tool_set)
        if system_prompt is not None:
            self.history.append(dict(role="system", content=system_prompt))

        self.__reply_message = reply_message

    def generate_reply(self, message: str) -> str:
        if self.__reply_message is not None:
            self.history.append(dict(role="user", content=message))
            self.history.append(dict(role="assistant", content=self.__reply_message))
            return self.__reply_message
        else:
            return super().generate_reply(message)


class Assistant(Role):
    def __init__(self, llm_client: LlmClient, tool_set: dict[str, Tool], system_prompt: str = None):
        super().__init__(llm_client, tool_set)
        if system_prompt is not None:
            self.history.append(dict(role="system", content=system_prompt))


class AgenticStrategy:
    def __init__(
        self,
        llm_client: LlmClient,
        tool_set: dict[str, Tool],
        template_data: dict[str, str],
        system_prompt_template: str,
        user_prompt_template: str,
        *args,
        **kwargs,
    ):
        self.tool_set = dict(end=EndTool(), **tool_set)
        self.__template_data = template_data
        self.__user_prompt_template = user_prompt_template
        self.__assistant_role = Assistant(llm_client, self.tool_set, self.__render_prompt(system_prompt_template))
        self.__user_role = UserProxy(llm_client, dict())

    def __render_prompt(self, prompt_template: str) -> str:
        chevron.render.__globals__["_html_escape"] = lambda x: x
        return chevron.render(
            template=prompt_template,
            data=self.__template_data,
            partials_path=None,
            partials_ext="".join(random.choices(string.ascii_uppercase + string.digits, k=32)),
            partials_dict=dict(),
        )

    def __get_initial_prompt(self) -> list[ChatCompletionMessageParam]:
        return [dict(role="user", content=self.__render_prompt(self.__user_prompt_template))]

    def __is_session_completed(self) -> bool:
        for message in reversed(self.__assistant_role.history):
            if message.get("tool") is not None:
                continue
            if message.get("content") == EndTool.MESSAGE:
                return True

        return False

    def usage(self):
        request_tokens = 0
        response_tokens = 0
        for role in [self.__assistant_role, self.__user_role]:
            request_tokens += role.request_tokens
            response_tokens += role.response_tokens
        return {
            "request_tokens": request_tokens,
            "response_tokens": response_tokens,
        }

    def execute(self, limit: int | None = None) -> None:
        message = self.__render_prompt(self.__user_prompt_template)
        try:
            for i in range(limit or self.__limit or sys.maxsize):
                self.run_count = i + 1
                for role in [self.__assistant_role, self.__user_role]:
                    message = role.generate_reply(message)
                if self.__is_session_completed():
                    break
        except Exception as e:
            logging.error(e)
        finally:
            self.run_count = 0

    @property
    def history(self):
        return self.__user_role.history

    @property
    def tool_records(self):
        for tool in self.tool_set.values():
            if isinstance(tool, CodeEditTool):
                cwd = Path.cwd()
                modified_files = [file_path.relative_to(cwd) for file_path in tool.tool_records["modified_files"]]
                return [dict(path=str(file)) for file in modified_files]
        return []
