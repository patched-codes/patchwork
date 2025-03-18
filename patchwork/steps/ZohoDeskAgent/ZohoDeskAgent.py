from patchwork.common.client.llm.aio import AioLlmClient
from patchwork.common.multiturn_strategy.agentic_strategy_v2 import (
    AgentConfig,
    AgenticStrategyV2,
)
from patchwork.common.tools.api_tool import APIRequestTool
from patchwork.common.utils.utils import mustache_render
from patchwork.step import Step

from .typed import ZohoDeskAgentInputs, ZohoDeskAgentOutputs


class ZohoDeskAgent(Step, input_class=ZohoDeskAgentInputs, output_class=ZohoDeskAgentOutputs):
    def __init__(self, inputs: dict):
        super().__init__(inputs)

        if not inputs.get("zoho_access_token"):
            raise ValueError("zoho_access_token is required")
        if not inputs.get("user_prompt"):
            raise ValueError("user_prompt is required")
        if not inputs.get("org_id"):
            raise ValueError("org_id is required for Zoho Desk API calls")

        # Configure conversation limit
        self.conversation_limit = int(inputs.get("max_agent_calls", 1))

        # Prepare system prompt with Zoho Desk context
        system_prompt = inputs.get(
            "system_prompt",
            "Please summarise the conversation given and provide the result in the structure that is asked of you.",
        )

        # Set up headers for Zoho Desk API
        self.headers = {
            "Authorization": f"Zoho-oauthtoken {inputs.get('zoho_access_token')}",
            "orgId": inputs.get("org_id"),
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        llm_client = AioLlmClient.create_aio_client(inputs)

        # Configure agentic strategy with Zoho Desk-specific context
        self.agentic_strategy = AgenticStrategyV2(
            model="claude-3-7-sonnet-latest",
            llm_client=llm_client,
            system_prompt_template=system_prompt,
            template_data={},
            user_prompt_template=mustache_render(inputs.get("user_prompt"), inputs.get("prompt_value")),
            agent_configs=[
                AgentConfig(
                    name="Zoho Desk Assistant",
                    model="claude-3-7-sonnet-latest",
                    tool_set=dict(
                        make_api_request=APIRequestTool(
                            headers=self.headers,
                        )
                    ),
                    system_prompt="""\
You are a senior software developer helping users interact with Zoho Desk via the Zoho Desk API.
Your goal is to retrieve, create, or modify tickets, contacts, and other Zoho Desk resources.
Use the `make_api_request` tool to interact with the Zoho Desk API.
Skip the headers for the API requests as they are already provided.

The base URL for the Zoho Desk API is https://desk.zoho.com/api/v1

For modifying or creating data, the data should be a JSON string.
When you have the result of the information user requested, return the response of the final result tool as is.

Here are some common Zoho Desk API endpoints:
- GET /tickets - List tickets
- GET /tickets/{ticketId} - Get ticket details
- POST /tickets - Create a ticket
- PUT /tickets/{ticketId} - Update a ticket
- GET /departments - List departments
- GET /contacts - List contacts
- GET /contacts/{contactId} - Get contact details
- POST /contacts - Create a contact
- GET /contacts/{contactId}/tickets - List tickets by contact

Additional query parameters:
- include: Additional information related to tickets. Values allowed are: 'products', 'departments', 'team', 'isRead', and 'assignee'. Multiple values can be comma-separated.
- from: Index number to start fetching from
- limit: Number of items to fetch (range: 1-100)
- sortBy: Sort by a specific attribute like 'createdTime' or 'modifiedTime'. Prefix with '-' for descending order.

The orgId is already included in the headers for all API calls.
""",
                )
            ],
            example_json=inputs.get("example_json", '{"summary":"summary of actions"}'),
        )

    def run(self) -> dict:
        # Execute the agentic strategy
        result = self.agentic_strategy.execute(limit=self.conversation_limit)

        # Return results with usage information
        return {**result, **self.agentic_strategy.usage()}
