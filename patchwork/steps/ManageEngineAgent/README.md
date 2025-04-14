# ManageEngine Agent 

The `ManageEngineAgent` module provides methods and strategies to interact with the ManageEngine ServiceDesk via the ServiceDeskPlus API. It is designed for extraction, creation, or modification of service desk tickets and related information. This is particularly useful for automating interactions with ManageEngine services using natural language processing capabilities.

## Primary Components

1. **ManageEngineAgentInputs**: The input class that specifies the required and optional parameters needed for the agent.
2. **ManageEngineAgentOutputs**: The output class that defines the structure of the data returned after the execution.
3. **ManageEngineAgent Class**: Implements a step for interacting with ManageEngine ServiceDesk.

## Inputs

### Required Inputs

- `zoho_access_token` (`str`): OAuth token required for authorization with the ManageEngine API.
- `user_prompt` (`str`): The prompt to guide the system in understanding user requests.
- `prompt_value` (`Dict[str, Any]`): Dictionary of values to be inserted into the `user_prompt`.

### Optional Inputs

- `max_agent_calls` (`int`): Limit for the number of API calls the agent can perform, default is 1.
- `openai_api_key`, `anthropic_api_key`, `google_api_key` (Annotated `str`): Keys for third-party language model services. Using a key is interchangeable with the other two.
- `system_prompt` (`Optional[str]`): A prompt for the language model to configure the context for ManageEngine interactions.
- `example_json` (`Optional[Dict]`): An example JSON structure for prompting context.

## Outputs

- `conversation_history` (`List[Dict]`): A log of the conversation history for debugging or review.
- `tool_records` (`List[Dict]`): A record of tool activities during the session.
- `request_tokens` (`int`): Count of tokens used in making requests.
- `response_tokens` (`int`): Count of tokens used in responses.

## Usage

This agent is configured to assist a software developer and the program manager in easily managing service desk tickets using conversational AI models. The interaction is automated by applying an agentic strategy with a language model having pre-defined prompts. Typically, this is used within larger frameworks or systems looking to incorporate automated service management solutions with ManageEngine.

## Remarks

- The system prompts are designed to engage with a specific model `claude-3-7-sonnet-latest` and use predefined API request tools.
- It's built with an extendable strategy capable of executing a dialogue and managing service requests, enhancing productivity and efficiency in service management.
