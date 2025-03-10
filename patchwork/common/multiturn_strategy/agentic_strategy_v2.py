from __future__ import annotations

import asyncio
import json
import logging
import sys

from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.agent import AgentRunResult
from typing_extensions import Any, Dict, Optional, Union

from patchwork.common.client.llm.protocol import LlmClient
from patchwork.common.client.llm.utils import example_json_to_base_model
from patchwork.common.tools import Tool
from patchwork.common.utils.utils import mustache_render

_COMPLETION_FLAG_ATTRIBUTE = "is_task_completed"
_MESSAGE_ATTRIBUTE = "message"
DEFAULT_AGENT_EXAMPLE_JSON = f'{{"{_MESSAGE_ATTRIBUTE}":"message", "{_COMPLETION_FLAG_ATTRIBUTE}": false}}'


class AgentConfig(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    name: str
    model: str
    tool_set: Dict[str, Tool]
    system_prompt: str = ""
    example_json: Union[str, Dict[str, Any]] = DEFAULT_AGENT_EXAMPLE_JSON

    def model_post_init(self, __context: Any) -> None:
        if self.example_json == DEFAULT_AGENT_EXAMPLE_JSON:
            return

        wanted = json.loads(self.example_json)
        default_wanted = json.loads(DEFAULT_AGENT_EXAMPLE_JSON)
        default_wanted.update(wanted)
        self.example_json = json.dumps(default_wanted)


class AgenticStrategyV2:
    def __init__(
        self,
        model: str,
        llm_client: LlmClient,
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
        self.__summariser = Agent(
            llm_client,
            result_retries=5,
            system_prompt=mustache_render(system_prompt_template, self.__template_data),
            result_type=example_json_to_base_model(example_json),
            model_settings=dict(
                parallel_tool_calls=False,
                model=model,
            ),
        )
        self.__agents = []
        for agent_config in agent_configs:
            tools = []
            for tool in agent_config.tool_set.values():
                tools.append(tool.to_pydantic_ai_function_tool())
            agent = Agent(
                llm_client,
                name=agent_config.name,
                system_prompt=mustache_render(agent_config.system_prompt, self.__template_data),
                tools=tools,
                result_type=example_json_to_base_model(agent_config.example_json),
                model_settings=dict(
                    parallel_tool_calls=False,
                    model=agent_config.model,
                ),
            )

            self.__agents.append(agent)

        self.__request_tokens = 0
        self.__response_tokens = 0

    def reset(self):
        self.__request_tokens = 0
        self.__response_tokens = 0

    def usage(self):
        return {
            "request_tokens": self.__request_tokens,
            "response_tokens": self.__response_tokens,
        }

    def execute(self, limit: Optional[int] = None) -> dict:
        agents_result = dict()
        loop = asyncio.new_event_loop()
        try:
            for index, agent in enumerate(self.__agents):
                user_message = mustache_render(self.__user_prompt_template, self.__template_data)
                message_history = None
                agent_output = None
                for i in range(limit or self.__limit or sys.maxsize):
                    agent_output: AgentRunResult[Any] = loop.run_until_complete(
                        agent.run(user_message, message_history=message_history)
                    )
                    message_history = agent_output.all_messages()
                    self.__request_tokens += agent_output.usage().request_tokens or 0
                    self.__response_tokens += agent_output.usage().response_tokens or 0

                    if getattr(agent_output.data, _COMPLETION_FLAG_ATTRIBUTE, False):
                        break
                    user_message = "Please continue"
                agents_result[index] = agent_output
        except Exception as e:
            logging.error(e)

        if len(agents_result) == 0:
            return dict()

        if len(agents_result) == 1:
            history = next(v for _, v in agents_result.items()).all_messages()
            final_result = loop.run_until_complete(
                self.__summariser.run(
                    "From the actions taken by the assistant. Please give me the result.",
                    message_history=history,
                )
            )
        else:
            agent_summaries = []
            for agent_result in agents_result.values():
                agent_summary_result = loop.run_until_complete(
                    self.__summariser.run(
                        "From the actions taken by the assistant. Please give me the result.",
                        message_history=agent_result.all_messages(),
                    )
                )
                self.__request_token += agent_summary_result.usage().request_tokens or 0
                self.__response_token += agent_summary_result.usage().response_tokens or 0

                agent_summary = getattr(agent_summary_result.data, _MESSAGE_ATTRIBUTE, None)
                if agent_summary is None:
                    continue

                agent_summaries.append(agent_summary)
            agent_summary_list = "\n* " + "\n* ".join(agent_summaries)
            final_result = loop.run_until_complete(
                self.__summariser.run(
                    "Please give me the result from the following summary of what the assistants have done."
                    + agent_summary_list,
                )
            )
        self.__request_tokens += final_result.usage().request_tokens or 0
        self.__response_tokens += final_result.usage().response_tokens or 0

        loop.close()
        return final_result.data.dict()
