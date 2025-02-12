from pathlib import Path

from patchwork.common.multiturn_strategy.agentic_strategy import (
    AgentConfig,
    AgenticStrategy,
)
from patchwork.common.tools import Tool
from patchwork.step import Step
from patchwork.steps.AgenticLLM.typed import AgenticLLMInputs, AgenticLLMOutputs


class AgenticLLM(Step, input_class=AgenticLLMInputs, output_class=AgenticLLMOutputs):
    def __init__(self, inputs):
        super().__init__(inputs)
        base_path = inputs.get("base_path")
        if base_path is None:
            base_path = str(Path.cwd())
        self.conversation_limit = int(inputs.get("max_agent_calls", 1))
        self.agentic_strategy = AgenticStrategy(
            api_key=inputs.get("anthropic_api_key"),
            template_data=inputs.get("prompt_value", {}),
            system_prompt_template=inputs.get("system_prompt", "Summarise from our previous conversation"),
            user_prompt_template=inputs.get("user_prompt"),
            agent_configs=[
                AgentConfig(
                    name="Assistant",
                    tool_set=Tool.get_tools(path=base_path),
                    system_prompt=inputs.get("agent_system_prompt"),
                )
            ],
            example_json=inputs.get("example_json"),
        )

    def run(self) -> dict:
        return self.agentic_strategy.execute(limit=self.conversation_limit)
