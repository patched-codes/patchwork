from pathlib import Path

from patchwork.common.client.llm.aio import AioLlmClient
from patchwork.common.multiturn_strategy.agentic_strategy import AgenticStrategy
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
            llm_client=AioLlmClient.create_aio_client(inputs),
            tool_set=Tool.get_tools(path=base_path),
            template_data=inputs.get("prompt_value"),
            system_prompt_template=inputs.get("system_prompt"),
            user_prompt_template=inputs.get("user_prompt"),
        )

    def run(self) -> dict:
        self.agentic_strategy.execute(limit=self.conversation_limit)
        return dict(
            conversation_history=self.agentic_strategy.history,
            tool_records=self.agentic_strategy.tool_records,
            **self.agentic_strategy.usage(),
        )
