from __future__ import annotations

import random
import string
from abc import abstractmethod
from collections import namedtuple
from typing import Any

import chevron
from openai.types.chat import ChatCompletionMessageParam

from patchwork.common.multiturn_strategy.multiturn_strategy import MultiturnStrategy
from patchwork.common.tools import Tool

StageConfig = namedtuple("StageConfig", ["id", "prompt_template"])


class MultiStageStrategy(MultiturnStrategy):
    def __init__(
        self,
        tool_set: dict[str, Tool],
        initial_template_data: dict[str, str],
        stage_configs: list[StageConfig],
        **kwargs,
    ):
        super().__init__(tool_set=tool_set, **kwargs)
        self.template_data = initial_template_data
        assert isinstance(stage_configs, list), "Stage configs must be in a list"
        assert len(stage_configs) > 0, "Stage configs cannot be empty"
        self.__stage_prompt_templates = [stage_config.prompt_template for stage_config in stage_configs]
        self.__stages = [stage_config.id for stage_config in stage_configs]
        self._stage = self.__stages[0]

    def __render_prompt(self, prompt: str) -> str:
        chevron.render.__globals__["_html_escape"] = lambda string: string
        return chevron.render(
            template=prompt,
            data=self.template_data,
            partials_path=None,
            partials_ext="".join(random.choices(string.ascii_uppercase + string.digits, k=32)),
            partials_dict=dict(),
        )

    def __get_stage_idx(self, stage=None) -> int:
        if stage is None:
            stage = self._stage

        try:
            return self.__stages.index(stage)
        except ValueError:
            raise ValueError(f"Invalid stage: {stage}")

    def run_initial_prompt(self) -> list[ChatCompletionMessageParam]:
        stage_idx = self.__get_stage_idx()
        prompt_template = self.__stage_prompt_templates[stage_idx]
        initial_prompt = self.__render_prompt(prompt_template)
        messages = [dict(role="user", content=initial_prompt)]
        return self._run_prompt(messages)

    @abstractmethod
    def _run_prompt(self, messages: list[ChatCompletionMessageParam]) -> list[ChatCompletionMessageParam]:
        pass

    def run_subsequent_prompt(self, messages: list[ChatCompletionMessageParam]) -> list[ChatCompletionMessageParam]:
        is_stage_completed = self._is_stage_completed(messages)
        if is_stage_completed:
            current_stage_idx = self.__get_stage_idx()
            next_stage_idx = current_stage_idx + 1
            return self._stage_change(self._stage, self.__stages[next_stage_idx], messages)

        last_message = messages[-1]
        if last_message.get("tool_calls") is not None:
            tool_messages = self.execute_tools(last_message)
            messages.extend(tool_messages)
        messages.append(dict(role="user", content=f"Continue with the {self._stage.name.upper()} stage."))
        return self._run_prompt(messages)

    @abstractmethod
    def _is_stage_completed(self, messages: list[ChatCompletionMessageParam]) -> bool:
        pass

    @abstractmethod
    def _stage_change(
        self, current_stage: Any, next_stage: Any, messages: list[ChatCompletionMessageParam]
    ) -> list[ChatCompletionMessageParam]:
        pass
