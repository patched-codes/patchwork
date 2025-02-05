from pathlib import Path

from patchwork.common.client.llm.aio import AioLlmClient
from patchwork.common.multiturn_strategy.agentic_strategy import AgenticStrategy, AgentConfig
from patchwork.common.tools import Tool
from patchwork.step import Step
from patchwork.steps.AgenticLLM.typed import AgenticLLMInputs, AgenticLLMOutputs


class AgenticLLM(Step, input_class=AgenticLLMInputs, output_class=AgenticLLMOutputs):
    def __init__(self, inputs):
        super().__init__(inputs)
        base_path = inputs.get("base_path")
        if base_path is None:
            base_path = str(Path.cwd())
        self.conversation_limit = int(int(inputs.get("max_llm_calls", 2)) / 2)
        self.agentic_strategy = AgenticStrategy(
            api_key=inputs.get("anthropic_api_key"),
            template_data=inputs.get("prompt_value"),
            system_prompt_template="",
            user_prompt_template=inputs.get("user_prompt"),
            agent_configs=[
                AgentConfig(name="", tool_set=Tool.get_tools(path=base_path), system_prompt=inputs.get("system_prompt"))
            ]
        )


    def run(self) -> dict:
        self.agentic_strategy.execute(limit=self.conversation_limit)
        return dict(
            conversation_history=self.agentic_strategy.history,
            tool_records=self.agentic_strategy.tool_records,
        )
