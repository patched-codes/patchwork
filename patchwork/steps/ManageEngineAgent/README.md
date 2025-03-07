# ManageEngineAgent Module Documentation

This module comprises two Python files designed to manage the interaction with the ManageEngine ServiceDesk through the ServiceDeskPlus API. It utilizes an agentic strategy to perform tasks such as retrieving, creating, or modifying service desk tickets. The files included in this module are:

- `typed.py`: Defines the input and output types for the ManageEngineAgent.
- `ManageEngineAgent.py`: Implements the `ManageEngineAgent` class, which executes tasks using an agentic strategy.

## File: `typed.py`

### Inputs

The `ManageEngineAgentInputs` class defines the input parameters required by the ManageEngineAgent, which include:

- **Required Inputs**:
  - `me_access_token`: A string containing the access token for ManageEngine.
  - `user_prompt`: A string for the user prompt.
  - `prompt_value`: A dictionary containing additional data necessary for prompt processing.

- **Optional Inputs**:
  - `max_agent_calls`: An integer specifying the maximum number of agent calls allowed.
  - `openai_api_key`, `anthropic_api_key`, `google_api_key`: Strings for relevant API keys, supporting logical OR operations with each other.
  - `system_prompt`: An optional custom system prompt string.
  - `example_json`: Optional dictionary for example JSON data.

### Outputs

The `ManageEngineAgentOutputs` class specifies the output structure:

- `conversation_history`: A list of dictionaries documenting the conversation history.
- `tool_records`: A list of dictionary records maintained by the tools used.
- `request_tokens`: An integer counting the request tokens used.
- `response_tokens`: An integer counting the response tokens used.

## File: `ManageEngineAgent.py`

The `ManageEngineAgent` class extends the `Step` class, involved in executing an agentic strategy tailored for interacting with the ManageEngine ServiceDesk. 

### Inputs

- `inputs`: A dictionary matching the `ManageEngineAgentInputs` specifications.

### Attributes

- `conversation_limit`: Configures conversation constraints based on the `max_agent_calls`.
- `headers`: Sets HTTP headers required for API interaction.
- `llm_client`: Utilizes the `AioLlmClient` for language model interactions.
- `agentic_strategy`: Implements the `AgenticStrategyV2` for executing agentic operations using the "claude-3-7-sonnet-latest" model.

### Method: `run`

This method executes the agentic strategy:

- **Execution**: Calls `self.agentic_strategy.execute()` with a limit on the conversation cycles.
- **Return**: Outputs results combined with usage statistics from the agentic strategy.

## Usage

This module is best suited for developers who need to automate task management in ManageEngine ServiceDesk via its API. Inputs are configured to accept customization options, allowing users to specify API tokens, prompts, and agent configuration dynamically. The outputs facilitate tracking of usage metrics and retaining conversation history, thus offering insights into agent interactions.
