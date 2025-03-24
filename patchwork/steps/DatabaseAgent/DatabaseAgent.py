from patchwork.common.client.llm.aio import AioLlmClient
from patchwork.common.multiturn_strategy.agentic_strategy_v2 import (
    AgentConfig,
    AgenticStrategyV2,
)
from patchwork.common.tools.db_query_tool import DatabaseQueryTool
from patchwork.common.utils.utils import mustache_render
from patchwork.step import Step
from patchwork.steps.DatabaseAgent.typed import (
    DatabaseAgentInputs,
    DatabaseAgentOutputs,
)


class DatabaseAgent(Step, input_class=DatabaseAgentInputs, output_class=DatabaseAgentOutputs):
    def __init__(self, inputs):
        super().__init__(inputs)
        data = inputs.get("prompt_value", {})
        task = mustache_render(inputs["task"], data)
        db_dialect = inputs["db_dialect"]
        self.agentic_strategy = AgenticStrategyV2(
            model="gemini-2.0-flash",
            llm_client=AioLlmClient.create_aio_client(inputs),
            template_data=dict(),
            system_prompt_template=f"""\
Please summarise the conversation given and provide the result in the structure that is asked of you.
""",
            user_prompt_template=f"""\
Please take note of any requirements to the data required to fetch.

{task}
""",
            agent_configs=[
                AgentConfig(
                    model="gemini-2.0-flash",
                    name="Assistant",
                    tool_set=dict(db_tool=DatabaseQueryTool(inputs)),
                    system_prompt=f"""\
You are a {db_dialect} database query execution assistant. Assist me in completing a task.
Before you begin you should first try to know all tables currently available.
Then find out what data is held in the relevant tables.
""",
                )
            ],
            example_json=inputs.get("example_json"),
        )

    def run(self) -> dict:
        result = self.agentic_strategy.execute(limit=10)
        return {**result, **self.agentic_strategy.usage()}


# class DatabaseAgent(Step, input_class=DatabaseAgentInputs, output_class=DatabaseAgentOutputs):
#     def __init__(self, inputs):
#         super().__init__(inputs)
#
#         llm_client = AioLlmClient.create_aio_client(inputs)
#
#         data = inputs.get("prompt_value", {})
#         self.task = mustache_render(inputs["task"], data)
#
#         db_dialect = inputs["db_dialect"]
#         self.planner = PlanningStrategy(
#             llm_client,
#             planner_system_prompt=f"""\
# You are a {db_dialect} database query planning assistant. You are tasked to plan the steps to assist with the provided task.
# You will not execute the steps in the plan. The user will do that instead.
# The first step of the plan should be as follows:
# 1. Tell me all tables currently available.
#
# After the list of table names is provided, get the DDL of the tables that is relevant.
#
# Your steps should be clear and concise like the following example:
# 1. Tell me the column descriptions of the table `orders`.
# 2. Execute the SQL Query: `SELECT * FROM orders`
#
# After every step, you will be asked to edit the plan so feel free to plan 1 step at a time.
# """,
#             executor_system_prompt=f"""\
# You are a {db_dialect} database query execution assistant. You will be provided instructions on what to do.
# """,
#         )
#
#     def run(self) -> dict:
#         planner_response = self.planner.run(self.task, 10)
#         return {**planner_response, **self.planner.usage()}
