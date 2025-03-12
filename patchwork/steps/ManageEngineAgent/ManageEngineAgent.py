from patchwork.common.client.llm.aio import AioLlmClient
from patchwork.common.multiturn_strategy.agentic_strategy_v2 import (
    AgentConfig,
    AgenticStrategyV2,
)
from patchwork.common.tools.api_tool import APIRequestTool
from patchwork.common.utils.utils import mustache_render
from patchwork.step import Step

from .typed import ManageEngineAgentInputs, ManageEngineAgentOutputs


class ManageEngineAgent(Step, input_class=ManageEngineAgentInputs, output_class=ManageEngineAgentOutputs):
    def __init__(self, inputs: dict):
        super().__init__(inputs)

        if not inputs.get("zoho_access_token"):
            raise ValueError("zoho_access_token is required")
        if not inputs.get("user_prompt"):
            raise ValueError("user_prompt is required")

        # Configure conversation limit
        self.conversation_limit = int(inputs.get("max_agent_calls", 1))

        # Prepare system prompt with ManageEngine context
        system_prompt = inputs.get(
            "system_prompt",
            "Please summarise the conversation given and provide the result in the structure that is asked of you.",
        )

        self.headers = {
            "Authorization": f"Zoho-oauthtoken {inputs.get('zoho_access_token')}",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/vnd.manageengine.sdp.v3+json",
        }

        llm_client = AioLlmClient.create_aio_client(inputs)

        # Configure agentic strategy with ManageEngine-specific context
        self.agentic_strategy = AgenticStrategyV2(
            model="claude-3-7-sonnet-latest",
            llm_client=llm_client,
            system_prompt_template=system_prompt,
            template_data={},
            user_prompt_template=mustache_render(inputs.get("user_prompt"), inputs.get("prompt_value")),
            agent_configs=[
                AgentConfig(
                    name="ManageEngine Assistant",
                    model="claude-3-7-sonnet-latest",
                    tool_set=dict(
                        make_api_request=APIRequestTool(
                            headers=self.headers,
                            preprocess_data=lambda x: f"input_data={x}",
                        )
                    ),
                    system_prompt="""\
You are an senior software developer helping the program manager to interact with ManageEngine ServiceDesk via the ServiceDeskPlus API.
Your goal is to retrieve, create, or modify service desk tickets and related information.
Use the `make_api_request` tool to interact with the ManageEngine API.
Skip the headers for the api requests as they are already provided.
The base url for the ServiceDeskPlus API is https://sdpondemand.manageengine.com/app/itdesk/api/v3

For modifying or creating data, the data should be a json string.
When you have the result of the information user requested, return the response of the final result tool as is.
""",
                )
            ],
            example_json=inputs.get("example_json"),
        )

    def run(self) -> dict:
        # Execute the agentic strategy
        result = self.agentic_strategy.execute(limit=self.conversation_limit)

        # Return results with usage information
        return {**result, **self.agentic_strategy.usage()}
