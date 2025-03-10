import tempfile
from pathlib import Path

from patchwork.common.client.llm.aio import AioLlmClient
from patchwork.common.multiturn_strategy.agentic_strategy_v2 import (
    AgentConfig,
    AgenticStrategyV2,
)
from patchwork.common.tools import FileViewTool, FindTextTool
from patchwork.common.tools.csvkit_tool import CSVSQLTool, In2CSVTool
from patchwork.common.utils.utils import mustache_render
from patchwork.step import Step
from patchwork.steps.FileAgent.typed import FileAgentInputs, FileAgentOutputs


class FileAgent(Step, input_class=FileAgentInputs, output_class=FileAgentOutputs):
    def __init__(self, inputs):
        super().__init__(inputs)
        self.base_path = inputs.get("base_path", str(Path.cwd()))
        data = inputs.get("prompt_value", {})
        task = mustache_render(inputs["task"], data)

        self.strat_kwargs = dict(
            model="claude-3-5-sonnet-latest",
            llm_client=AioLlmClient.create_aio_client(inputs),
            template_data=dict(),
            system_prompt_template=f"""\
Please summarise the conversation given and provide the result in the structure that is asked of you.
""",
            user_prompt_template=f"""\
Please help me with this task:

{task}
""",
            agent_configs=[
                AgentConfig(
                    name="Assistant",
                    model="claude-3-7-sonnet-latest",
                    tool_set=dict(),
                    system_prompt="""\
You are a assistant that is supposed to help me with a set of files. These files are commonly tabular formatted like csv, xls or xlsx.
If you find a tabular formatted file you should use the `in2csv_tool` tool to convert the files into CSV.

After that is done, then run other tools to assist me.
""",
                )
            ],
            example_json=inputs.get("example_json"),
        )

    def run(self) -> dict:
        kwargs = self.strat_kwargs
        with tempfile.TemporaryDirectory() as tmpdir:
            agent_config = next(iter(kwargs.get("agent_configs", [])), None)
            agent_config.tool_set = dict(
                find_text=FindTextTool(self.base_path),
                file_view=FileViewTool(self.base_path),
                in2csv_tool=In2CSVTool(self.base_path),
                csvsql_tool=CSVSQLTool(self.base_path, tmpdir),
            )
            agentic_strategy = AgenticStrategyV2(**kwargs)
            result = agentic_strategy.execute(limit=10)
            return {**result, **agentic_strategy.usage()}
