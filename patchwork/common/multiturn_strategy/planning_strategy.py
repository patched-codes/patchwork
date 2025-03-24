import asyncio
from functools import partial
from typing import Any, Optional, Union

from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.agent import AgentRunResult

from patchwork.common.client.llm.protocol import LlmClient
from patchwork.common.client.llm.utils import example_json_to_base_model
from patchwork.common.tools import Tool


class StepCompletedResult(BaseModel):
    is_step_completed: bool


class PlanCompletedResult(BaseModel):
    is_plan_completed: bool


class ExecutionResult(BaseModel):
    json_data: str
    message: str
    is_completed: bool


class _Plan:
    def __init__(self, initial_plan: Optional[list[str]] = None):
        self.__plan = initial_plan or []
        self.__cursor = 0

    def advance(self) -> bool:
        self.__cursor += 1
        return self.__cursor < len(self.__plan)

    def is_empty(self) -> bool:
        return len(self.__plan) == 0

    def register_steps(self, agent: Agent):
        agent.tool_plain(self.get_current_plan)
        agent.tool_plain(self.get_current_step)
        agent.tool_plain(self.get_current_step_index)
        agent.tool_plain(self.add_step)
        agent.tool_plain(self.delete_step)

    def get_current_plan(self) -> str:
        return "\n".join([f"{i}. {step}" for i, step in enumerate(self.__plan)])

    def get_current_step(self) -> str:
        if len(self.__plan) == 0:
            return "There is currently no plan"

        return self.__plan[self.__cursor]

    def get_current_step_index(self) -> int:
        return self.__cursor

    def add_step(self, index: int, step: str) -> str:
        if index < 0:
            return "index cannot be a negative number"

        if index >= len(self.__plan):
            insertion_func = self.__plan.append
        else:
            insertion_func = partial(self.__plan.insert, index)

        insertion_func(step)
        return "Added step\nCurrent plan:\n" + self.get_current_plan()

    def delete_step(self, step: str) -> str:
        try:
            i = self.__plan.index(step)
            self.__plan.pop(i)
            return self.get_current_plan()
        except ValueError:
            return "Step not found in plan\nCurrent plan:\n" + self.get_current_plan()


class PlanningStrategy:
    def __init__(
        self,
        llm_client: LlmClient,
        planner_system_prompt: str,
        executor_system_prompt: str,
        executor_tool_set: dict[str, Tool],
        example_json: Union[str, dict[str, Any]] = '{"output":"output text"}',
    ):
        self.planner = Agent(
            llm_client,
            name="Planner",
            system_prompt=planner_system_prompt,
            model_settings=dict(
                parallel_tool_calls=False,
                model="gemini-2.0-flash",
            ),
        )

        self.plan = _Plan()
        self.plan.register_steps(self.planner)

        self.executor = Agent(
            llm_client,
            name="Executor",
            system_prompt=executor_system_prompt,
            result_type=ExecutionResult,
            tools=[tool.to_pydantic_ai_function_tool() for tool in executor_tool_set.values()],
            model_settings=dict(
                parallel_tool_calls=False,
                model="gemini-2.0-flash",
            ),
        )

        self.__summariser = Agent(
            llm_client,
            result_retries=5,
            system_prompt="""\
Please summarise the conversation given and provide the result in the structure that is asked of you.
""",
            result_type=example_json_to_base_model(example_json),
            model_settings=dict(
                parallel_tool_calls=False,
                model="gemini-2.0-flash",
            ),
        )

        self.reset()

    def reset(self):
        self.__request_tokens = 0
        self.__response_tokens = 0

    def usage(self):
        return {
            "request_tokens": self.__request_tokens,
            "response_tokens": self.__response_tokens,
        }

    def __agent_run(self, agent: Agent, prompt: str, **kwargs) -> AgentRunResult[Any]:
        loop = asyncio.new_event_loop()
        planner_response = loop.run_until_complete(agent.run(prompt, **kwargs))
        loop.close()
        self.__request_tokens += planner_response.usage().request_tokens
        self.__response_tokens += planner_response.usage().response_tokens

        return planner_response

    def run(self, task: str, conversation_limit: int = 10) -> dict:

        planner_response = self.__agent_run(self.planner, f"Produce the initial plan for {task}")
        planner_history = planner_response.all_messages()
        if self.plan.is_empty():
            planner_response = self.__agent_run(
                self.planner, f"Please use the tools provided to setup the plan", message_history=planner_history
            )
            planner_history = planner_response.all_messages()

        for i in range(conversation_limit):
            step = self.plan.get_current_step()
            executor_prompt = f"Please execute the following task: {step}"
            response = self.__agent_run(self.executor, executor_prompt)

            plan_str = self.plan.get_current_plan()
            step_index = self.plan.get_current_step_index()
            planner_prompt = f"""\
The current plan is:
{plan_str}

We are current at {step_index}.
If the current step is not completed, edit the current step.

The execution result for the step {step_index} is: 
{response.data}

"""
            planner_response = self.__agent_run(
                self.planner,
                planner_prompt,
                message_history=planner_history,
                result_type=StepCompletedResult,
            )
            planner_history = planner_response.all_messages()
            if not planner_response.data.is_step_completed:
                continue

            if self.plan.advance():
                continue

            planner_response = self.__agent_run(
                self.planner,
                "Is the task completed? If the task is not completed please add more steps using the tools provided.",
                message_history=planner_history,
                result_type=PlanCompletedResult,
            )
            if planner_response.data.is_plan_completed:
                break

        final_result = self.__agent_run(
            self.__summariser,
            "From the actions taken by the assistant. Please give me the result.",
            message_history=planner_history,
        )

        return final_result.data.dict()
