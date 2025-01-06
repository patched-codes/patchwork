from __future__ import annotations

from abc import abstractmethod
from collections import defaultdict
from enum import Enum, auto

from openai.types.chat import ChatCompletionMessageParam

from patchwork.common.client.llm.protocol import LlmClient
from patchwork.common.multiturn_strategy.multistage_strategy import (
    MultiStageStrategy,
    StageConfig,
)
from patchwork.common.tools import Tool


class _STAGE(Enum):
    ANALYSIS = auto()
    IMPLEMENT = auto()


class AnalyzeImplementStrategy(MultiStageStrategy):
    def __init__(
        self,
        tool_set: dict[str, Tool],
        llm_client: LlmClient,
        initial_template_data: dict[str, str],
        analysis_prompt_template: str,
        implementation_prompt_template: str,
        **kwargs,
    ):
        super().__init__(
            tool_set=tool_set,
            initial_template_data=initial_template_data,
            stage_configs=[
                StageConfig(id=_STAGE.ANALYSIS, prompt_template=analysis_prompt_template),
                StageConfig(id=_STAGE.IMPLEMENT, prompt_template=implementation_prompt_template),
            ],
            **kwargs,
        )
        self.llm_client = llm_client
        self._reset()

    def _reset(self):
        self.run_count = 0
        self.stage_run_counts = defaultdict(int)
        self.stage_messages = []

    def _run_prompt(self, messages: list[ChatCompletionMessageParam]) -> list[ChatCompletionMessageParam]:
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
        new_messages = [choice.message.to_dict() for choice in response.choices]
        messages.extend(new_messages)
        return messages

    def _is_stage_completed(self, messages: list[ChatCompletionMessageParam]) -> bool:
        possible_analysis_message = self.extract_analysis_message(messages[-1])
        self.template_data["analysis_results"] = possible_analysis_message
        return possible_analysis_message is not None

    def _stage_change(
        self, current_stage: _STAGE, next_stage: _STAGE, messages: list[ChatCompletionMessageParam]
    ) -> list[ChatCompletionMessageParam]:
        self._stage = next_stage
        self.stage_messages.append(messages)
        return self.run_initial_prompt()

    @abstractmethod
    def extract_analysis_message(self, message: ChatCompletionMessageParam) -> dict[str, str]:
        pass
