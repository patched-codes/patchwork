# Documentation: ManageEngine Agent

The `ManageEngine Agent` is a component within the `patchwork` system, designed to interact with the ManageEngine ServiceDesk via the ServiceDeskPlus API. It facilitates operations such as retrieving, creating, or modifying service desk tickets and related information using a conversational interface.

## Inputs

### ManageEngineAgentInputs

This is a `TypedDict` comprising the following fields:

- **Required**:
  - `zoho_access_token`: A string representing the Zoho OAuth token for authorization.
  - `user_prompt`: A string that contains the user's prompt or request.
  - `prompt_value`: A dictionary of key-value pairs used to fill in the user prompt template.

- **Optional**:
  - `max_agent_calls`: An integer setting a limit for the conversation, defaults to `1` if not provided.
  - `openai_api_key`: An API key for OpenAI, annotated for mutual exclusivity with `google_api_key`, and `anthropic_api_key`.
  - `anthropic_api_key`: An API key for Anthropic, annotated similarly for mutual exclusivity.
  - `google_api_key`: An API key for Google, also mutually exclusive.
  - `system_prompt`: An optional string to configure the system prompt for ManageEngine context.
  - `example_json`: An optional dictionary to provide example JSON data for formatting purposes.

## Outputs

### ManageEngineAgentOutputs

This `TypedDict` includes:

- `conversation_history`: A list of dictionaries storing the history of the conversation.
- `tool_records`: A list of dictionaries logging the records of tool interactions.
- `request_tokens`: An integer representing the number of tokens used for requests.
- `response_tokens`: An integer for the number of tokens in responses.

## Usage

The `ManageEngineAgent` class is initialized with input parameters encapsulated within `ManageEngineAgentInputs`. It creates an instance of `AioLlmClient` and configures an `AgenticStrategyV2` to handle interactions through predefined API tools. The primary goal is to streamline communication with ManageEngine's ServiceDesk, using structured prompts and agent configurations.

### Key Operations:

1. **Initialization**:
   - Validates required inputs for OAuth token and user prompt.
   - Establishes authorization headers.

2. **Agent Configuration**:
   - Integrates with an LLM client using a system prompt tailored for ManageEngine interactions.
   - Defines an agent strategy equipped with an API request tool for service desk operations.

3. **Execution**:
   - Runs the agentic strategy with a conversation limit.
   - Returns processed results alongside usage statistics.

The primary file `ManageEngineAgent.py` handles agent setup and execution, while `typed.py` defines the structured input and output typing. This system is best suited for developers seeking to automate and enhance their interaction with ManageEngine's ServiceDesk functionalities programmatically.
