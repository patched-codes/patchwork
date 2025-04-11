from patchwork.common.client.llm.aio import AioLlmClient
from patchwork.common.multiturn_strategy.agentic_strategy_v2 import (
    AgentConfig,
    AgenticStrategyV2,
)
from patchwork.common.tools.api_tool import APIRequestTool
from patchwork.common.utils.utils import mustache_render
from patchwork.step import Step
import json

from .typed import SlackAgentInputs, SlackAgentOutputs


class SlackAgent(Step, input_class=SlackAgentInputs, output_class=SlackAgentOutputs):
    def __init__(self, inputs: dict):
        super().__init__(inputs)

        if not inputs.get("slack_bot_token"):
            raise ValueError("slack_bot_token is required")
        if not inputs.get("user_prompt"):
            raise ValueError("user_prompt is required")

        self.conversation_limit = int(inputs.get("max_agent_calls", 1))

        system_prompt = inputs.get(
            "system_prompt",
            "Please summarise the conversation given and provide the result in the structure that is asked of you.",
        )

        self.headers = {
            "Authorization": f"Bearer {inputs.get('slack_bot_token')}",
            "Content-Type": "application/json",
        }

        llm_client = AioLlmClient.create_aio_client(inputs)

        model = inputs.get("model", "gemini-2.0-flash")
        
        api_tool = APIRequestTool(
            headers=self.headers,
        )

        self.agentic_strategy = AgenticStrategyV2(
            model=model,
            llm_client=llm_client,
            system_prompt_template=system_prompt,
            template_data={},
            user_prompt_template=mustache_render(inputs.get("user_prompt"), inputs.get("prompt_value")),
            agent_configs=[
                AgentConfig(
                    name="Slack Assistant",
                    model=model,
                    tool_set=dict(
                        make_api_request=api_tool
                    ),
                    system_prompt="""\
You are a senior software developer helping users interact with Slack via the Slack Web API.
Your goal is to retrieve, create, or modify messages, channels, and other Slack resources.
Use the `make_api_request` tool to interact with the Slack API.
Skip the headers for the API requests as they are already provided.

The base URL for the Slack Web API is https://slack.com/api

Common Slack API endpoints:
- POST /chat.postMessage - Send a message to a channel
- GET /conversations.list - List all channels in the workspace
- GET /conversations.history - Get message history from a channel
- POST /conversations.create - Create a new channel
- POST /conversations.join - Join a channel
- POST /conversations.leave - Leave a channel
- GET /users.list - List all users in the workspace
- GET /users.info - Get information about a specific user
- POST /reactions.add - Add a reaction to a message
- POST /reactions.remove - Remove a reaction from a message

IMPORTANT: GET requests the prompt_value will contain the params to pass instead of data
Example: For GET /conversations.history, use params={"channel": "C08..."} instead of appending to the URL.

For modifying or creating data, the data should be a JSON string.
When you have the result of the information user requested, return the response of the final result tool as is.

Note: All API responses include a boolean 'ok' field indicating success/failure.
If 'ok' is false, check the 'error' field for details about what went wrong.
""",
                )
            ],
            example_json=inputs.get("example_json"),
        )

    def run(self) -> dict:
        result = self.agentic_strategy.execute(limit=self.conversation_limit)
            
        return {**result, **self.agentic_strategy.usage()}
        