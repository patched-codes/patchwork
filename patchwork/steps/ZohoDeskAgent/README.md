# Zoho Desk Agent

This agent allows you to interact with the Zoho Desk API to manage tickets, contacts, and other Zoho Desk resources.

## Requirements

- Zoho Desk API access token
- Zoho Desk organization ID
- Patchwork framework

## Usage

The ZohoDeskAgent can be used to:
- Retrieve ticket information
- Create new tickets
- Update existing tickets
- Manage contacts
- Query departments and other Zoho Desk resources

## Input Parameters

Required:
- `zoho_access_token`: Your Zoho Desk API access token
- `org_id`: Zoho Desk organization ID (required for all API calls)
- `user_prompt`: The prompt template to use for the agent
- `prompt_value`: Dictionary of values to render in the user prompt template

Optional:
- `max_agent_calls`: Maximum number of agent calls (default: 1)
- `system_prompt`: Custom system prompt
- `example_json`: Example JSON for the agent
- LLM API keys (one of the following):
  - `openai_api_key`
  - `anthropic_api_key`
  - `google_api_key`

## Example

```python
from patchwork.steps.ZohoDeskAgent import ZohoDeskAgent

# Initialize the agent
agent = ZohoDeskAgent({
    "zoho_access_token": "your_zoho_access_token",
    "org_id": "your_organization_id",
    "user_prompt": "Get information about ticket {{ticket_id}}",
    "prompt_value": {"ticket_id": "12345"},
    "anthropic_api_key": "your_anthropic_api_key",
    "max_agent_calls": 3
})

# Run the agent
result = agent.run()
print(result)
```

## API Endpoints

The agent can interact with various Zoho Desk API endpoints, including:

- `GET /tickets` - List tickets
- `GET /tickets/{ticketId}` - Get ticket details
- `POST /tickets` - Create a ticket
- `PUT /tickets/{ticketId}` - Update a ticket
- `GET /departments` - List departments
- `GET /contacts` - List contacts
- `GET /contacts/{contactId}` - Get contact details
- `POST /contacts` - Create a contact
- `GET /contacts/{contactId}/tickets` - List tickets by contact

## Query Parameters

Common query parameters for listing resources:
- `include`: Additional information to include (e.g., 'products', 'departments', 'team', 'isRead', 'assignee')
- `from`: Index number to start fetching from
- `limit`: Number of items to fetch (range: 1-100)
- `sortBy`: Sort by a specific attribute (e.g., 'createdTime', 'modifiedTime')

For more information about the Zoho Desk API, refer to the [official documentation](https://desk.zoho.com/DeskAPIDocument).
