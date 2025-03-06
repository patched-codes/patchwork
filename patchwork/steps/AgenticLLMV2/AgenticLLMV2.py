from pathlib import Path

from patchwork.common.client.llm.aio import AioLlmClient
from patchwork.common.multiturn_strategy.agentic_strategy_v2 import (
    AgentConfig,
    AgenticStrategyV2,
)
from patchwork.common.tools import Tool
from patchwork.step import Step
from patchwork.steps.AgenticLLMV2.typed import AgenticLLMV2Inputs, AgenticLLMV2Outputs


class AgenticLLMV2(Step, input_class=AgenticLLMV2Inputs, output_class=AgenticLLMV2Outputs):
    def __init__(self, inputs):
        super().__init__(inputs)
        base_path = inputs.get("base_path")
        if base_path is None:
            base_path = str(Path.cwd())
        self.conversation_limit = int(inputs.get("max_agent_calls", 1))
        self.agentic_strategy = AgenticStrategyV2(
            model="claude-3-5-sonnet-latest",
            llm_client=AioLlmClient.create_aio_client(inputs),
            template_data=inputs.get("prompt_value", {}),
            system_prompt_template=inputs.get("system_prompt", "Summarise from our previous conversation"),
            user_prompt_template=inputs.get("user_prompt"),
            agent_configs=[
                AgentConfig(
                    name="Assistant",
                    model="claude-3-7-sonnet-latest",
                    tool_set=Tool.get_tools(path=base_path),
                    system_prompt=inputs.get("agent_system_prompt"),
                )
            ],
            example_json=inputs.get("example_json"),
        )

    def run(self) -> dict:
        result = self.agentic_strategy.execute(limit=self.conversation_limit)
        return {**result, **self.agentic_strategy.usage()}
