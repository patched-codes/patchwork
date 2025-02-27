from __future__ import annotations

import random
import string
from abc import abstractmethod
from collections import defaultdict
from enum import Enum, auto

import chevron
from openai.types.chat import ChatCompletionMessageParam

from patchwork.common.client.llm.protocol import LlmClient
from patchwork.common.multiturn_strategy.multiturn_strategy import MultiturnStrategy
from patchwork.common.tools import Tool


class STAGE(Enum):
    ANALYSIS = auto()
    IMPLEMENT = auto()


class AnalyzeImplementStrategy(MultiturnStrategy):
    def __init__(
        self,
        tool_set: dict[str, Tool],
        llm_client: LlmClient,
        initial_template_data: dict[str, str],
        analysis_prompt_template: str,
        implementation_prompt_template: str,
        **kwargs,
    ):
        super().__init__(tool_set=tool_set, **kwargs)
        self.llm_client = llm_client
        self.template_data = initial_template_data
        self.analysis_prompt_template = analysis_prompt_template
        self.implementation_prompt_template = implementation_prompt_template
        self._reset()

    def _reset(self):
        self._stage = STAGE.ANALYSIS
        self.run_count = 0
        self.stage_run_counts = defaultdict(int)
        self.__request_tokens = 0
        self.__response_tokens = 0

    def usage(self):
        return dict(
            request_tokens=self.__request_tokens,
            response_tokens=self.__response_tokens,
        )

    def __run_prompt(self, messages: list[ChatCompletionMessageParam]) -> list[ChatCompletionMessageParam]:
        input_kwargs = dict(
            messages=messages,
            model="claude-3-5-sonnet-latest",
            tools=self.get_tools_spec(),
            max_tokens=8096,
        )
        is_prompt_safe = self.llm_client.is_prompt_supported(**input_kwargs)
        if is_prompt_safe < 0:
            raise ValueError("The subsequent prompt is not supported, due to large size.")
        response = self.llm_client.chat_completion(**input_kwargs)
        self.__request_tokens += response.usage.prompt_tokens
        self.__response_tokens += response.usage.completion_tokens
        new_messages = [choice.message.to_dict() for choice in response.choices]
        messages.extend(new_messages)
        return messages

    def __render_prompt(self, prompt: str) -> str:
        chevron.render.__globals__["_html_escape"] = lambda string: string
        return chevron.render(
            template=prompt,
            data=self.template_data,
            partials_path=None,
            partials_ext="".join(random.choices(string.ascii_uppercase + string.digits, k=32)),
            partials_dict=dict(),
        )

    def run_initial_prompt(self) -> list[ChatCompletionMessageParam]:
        initial_prompt = self.__render_prompt(self.analysis_prompt_template)
        messages = [dict(role="user", content=initial_prompt)]
        return self.__run_prompt(messages)

    def run_subsequent_prompt(self, messages: list[ChatCompletionMessageParam]) -> list[ChatCompletionMessageParam]:
        last_message = messages[-1]
        if self._stage == STAGE.ANALYSIS:
            possible_analysis_message = self.extract_analysis_message(last_message)
            if possible_analysis_message is not None:
                self._stage = STAGE.IMPLEMENT
                self.template_data["analysis_results"] = possible_analysis_message
                implement_prompt = self.__render_prompt(self.implementation_prompt_template)
                messages = [dict(role="user", content=implement_prompt)]
                return self.__run_prompt(messages)

        if last_message.get("tool_calls") is not None:
            tool_messages = self.execute_tools(last_message)
            messages.extend(tool_messages)
        messages.append(dict(role="user", content=f"Continue with the {self._stage.name.upper()} stage."))
        return self.__run_prompt(messages)

    @abstractmethod
    def extract_analysis_message(self, message: ChatCompletionMessageParam) -> dict[str, str]:
        pass
