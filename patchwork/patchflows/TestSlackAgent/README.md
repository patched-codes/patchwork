# TestSlackAgent

This patchflow is designed to test the SlackAgent step by executing a single Slack API operation.

## How to run?

You can run it as follows:

```bash
patchwork TestSlackAgent slack_bot_token=<Your_Slack_Bot_Token> user_prompt="<Your_Prompt>" prompt_value='{"key": "value"}'
```

## Required Parameters

- `slack_bot_token`: Your Slack Bot User OAuth Token
- `user_prompt`: The prompt template to use for the agent
- `prompt_value`: Dictionary of values to render in the user prompt template

## Optional Parameters

- `max_agent_calls`: Maximum number of agent calls (default: 1)
- `system_prompt`: Custom system prompt
- `example_json`: Example JSON for the agent
- LLM API keys (one of the following):
  - `openai_api_key`
  - `anthropic_api_key`
  - `google_api_key`

## Example

```bash
# Send a message to a channel using Google's API
patchwork TestSlackAgent \
  slack_bot_token="xoxb-your-bot-token" \
  user_prompt="Send a message to channel {{channel}} with text {{message}}" \
  prompt_value='{"channel": "general", "message": "Hello from the Slack Agent!"}' \
  google_api_key="your_google_api_key"

# List all channels using Google's API
patchwork TestSlackAgent \
  slack_bot_token="xoxb-your-bot-token" \
  user_prompt="List all channels in the workspace" \
  prompt_value='{}' \
  google_api_key="your_google_api_key"

# Alternative examples with other API keys:
# Using Anthropic's API
patchwork TestSlackAgent \
  slack_bot_token="xoxb-your-bot-token" \
  user_prompt="Send a message to channel {{channel}} with text {{message}}" \
  prompt_value='{"channel": "general", "message": "Hello from the Slack Agent!"}' \
  anthropic_api_key="your_anthropic_api_key"

# Using OpenAI's API
patchwork TestSlackAgent \
  slack_bot_token="xoxb-your-bot-token" \
  user_prompt="Send a message to channel {{channel}} with text {{message}}" \
  prompt_value='{"channel": "general", "message": "Hello from the Slack Agent!"}' \
  openai_api_key="your_openai_api_key"
```

## What it does?

This patchflow:
1. Validates the required inputs
2. Executes the SlackAgent step with the provided configuration
3. Returns the results of the Slack API operation

The SlackAgent can perform various operations like:
- Sending messages to channels
- Listing and managing channels
- Getting message history
- Managing user information
- Adding/removing reactions to messages 