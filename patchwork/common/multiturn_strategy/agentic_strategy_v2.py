from __future__ import annotations

import logging
import sys

from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.anthropic import AnthropicModel
from typing_extensions import Any, Dict, Optional, Union

from patchwork.common.client.llm.utils import example_json_to_base_model
from patchwork.common.tools import Tool
from patchwork.common.utils.utils import mustache_render

_COMPLETION_FLAG_ATTRIBUTE = "is_task_completed"
_MESSAGE_ATTRIBUTE = "message"


class AgentConfig(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    name: str
    tool_set: Dict[str, Tool]
    system_prompt: str = ""
    example_json: Union[
        str, Dict[str, Any]
    ] = f'{{"{_MESSAGE_ATTRIBUTE}":"message", "{_COMPLETION_FLAG_ATTRIBUTE}": false}}'


class AgenticStrategyV2:
    def __init__(
        self,
        api_key: str,
        template_data: dict[str, str],
        system_prompt_template: str,
        user_prompt_template: str,
        agent_configs: list[AgentConfig],
        example_json: Union[str, dict[str, Any]] = '{"output":"output text"}',
        limit: Optional[int] = None,
    ):
        self.__limit = limit
        self.__template_data = template_data
        self.__user_prompt_template = user_prompt_template
        model = AnthropicModel("claude-3-5-sonnet-latest", api_key=api_key)
        self.__summariser = Agent(
            model,
            system_prompt=mustache_render(system_prompt_template, self.__template_data),
            result_type=example_json_to_base_model(example_json),
            model_settings=dict(parallel_tool_calls=False),
        )
        self.__agents = []
        for agent_config in agent_configs:
            tools = []
            for tool in agent_config.tool_set.values():
                tools.append(tool.to_pydantic_ai_function_tool())
            agent = Agent(
                model,
                name=agent_config.name,
                system_prompt=mustache_render(agent_config.system_prompt, self.__template_data),
                tools=tools,
                result_type=example_json_to_base_model(agent_config.example_json),
                model_settings=dict(parallel_tool_calls=False),
            )

            self.__agents.append(agent)

    def execute(self, limit: Optional[int] = None) -> dict:
        agents_result = dict()
        try:
            for index, agent in enumerate(self.__agents):
                user_message = mustache_render(self.__user_prompt_template, self.__template_data)
                message_history = None
                agent_output = None
                for i in range(limit or self.__limit or sys.maxsize):
                    agent_output = agent.run_sync(user_message, message_history=message_history)
                    message_history = agent_output.all_messages()
                    if getattr(agent_output.data, _COMPLETION_FLAG_ATTRIBUTE, False):
                        break
                    user_message = "Please continue"
                agents_result[index] = agent_output
        except Exception as e:
            logging.error(e)

        if len(agents_result) == 0:
            return dict()

        if len(agents_result) == 1:
            final_result = self.__summariser.run_sync(
                "From the actions taken by the assistant. Please give me the result.",
                message_history=next(v for _, v in agents_result.items()).all_messages(),
            )
        else:
            agent_summaries = []
            for agent_result in agents_result.values():
                agent_summary_result = self.__summariser.run_sync(
                    "From the actions taken by the assistant. Please give me the result.",
                    message_history=agent_result.all_messages(),
                )
                agent_summary = getattr(agent_summary_result.data, _MESSAGE_ATTRIBUTE, None)
                if agent_summary is None:
                    continue

                agent_summaries.append(agent_summary)
            agent_summary_list = "\n* " + "\n* ".join(agent_summaries)
            final_result = self.__summariser.run_sync(
                "Please give me the result from the following summary of what the assistants have done."
                + agent_summary_list,
            )

        return final_result.data.dict()
