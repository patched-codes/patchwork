# Slack Agent

This agent allows you to interact with the Slack Web API to manage messages, channels, and other Slack resources.

## Requirements

- Slack Bot User OAuth Token
- Patchwork framework

## Usage

The SlackAgent can be used to:
- Send messages to channels
- List and manage channels
- Get message history
- Manage user information
- Add/remove reactions to messages
- And more...

## Input Parameters

Required:
- `slack_bot_token`: Your Slack Bot User OAuth Token
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
from patchwork.steps.SlackAgent import SlackAgent

# Initialize the agent
agent = SlackAgent({
    "slack_bot_token": "xoxb-your-bot-token",
    "user_prompt": "Send a message to channel {{channel}} with text {{message}}",
    "prompt_value": {
        "channel": "general",
        "message": "Hello from the Slack Agent!"
    },
    "anthropic_api_key": "your_anthropic_api_key",
    "max_agent_calls": 3
})

# Run the agent
result = agent.run()
print(result)
```

## API Endpoints

The agent can interact with various Slack Web API endpoints, including:

- `POST /chat.postMessage` - Send a message to a channel
- `GET /conversations.list` - List all channels in the workspace
- `GET /conversations.history` - Get message history from a channel
- `POST /conversations.create` - Create a new channel
- `POST /conversations.join` - Join a channel
- `POST /conversations.leave` - Leave a channel
- `GET /users.list` - List all users in the workspace
- `GET /users.info` - Get information about a specific user
- `POST /reactions.add` - Add a reaction to a message
- `POST /reactions.remove` - Remove a reaction from a message

## Response Format

All Slack API responses include:
- `ok`: Boolean indicating success/failure
- `error`: String containing error details if `ok` is false
- Additional data specific to the endpoint called

For more information about the Slack Web API, refer to the [official documentation](https://api.slack.com/web). 
