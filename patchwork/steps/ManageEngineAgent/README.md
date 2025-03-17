# ManageEngineAgent Module Documentation

This documentation covers the functionality and usage of the `ManageEngineAgent` module, consisting of two main files: `typed.py` and `ManageEngineAgent.py`. These files define input and output specifications and implement a class for interacting with the ManageEngine ServiceDesk via an API.

## File: typed.py

### Purpose
Defines typed data structures for inputs and outputs used in the `ManageEngineAgent` class.

### Input Definitions

- `ManageEngineAgentInputs`: 
  - **Required Fields**:
    - `zoho_access_token (str)`: Access token for Zoho.
    - `user_prompt (str)`: User-specific prompt.
    - `prompt_value (Dict[str, Any])`: Dynamic values to be inserted into the prompt.
  - **Optional Fields**:
    - `max_agent_calls (int)`: Maximum number of agent interactions.
    - `openai_api_key, anthropic_api_key, google_api_key (str)`: API keys for various LLM services.
    - `system_prompt (Optional[str])`: Custom system prompt for the agent.
    - `example_json (Optional[Dict])`: Example data for interactions.

### Output Definitions

- `ManageEngineAgentOutputs`: 
  - `conversation_history (List[Dict])`: Records of the conversation.
  - `tool_records (List[Dict])`: Records of tool usage.
  - `request_tokens (int)`: Count of tokens used in requests.
  - `response_tokens (int)`: Count of tokens used in responses.

## File: ManageEngineAgent.py

### Purpose
Implements the `ManageEngineAgent` class that provides a means to interact with ManageEngine ServiceDesk via a structured agentic strategy.

### Class: `ManageEngineAgent`

#### Initialization
- **Parameters**: `inputs (dict)`
  - Validates `zoho_access_token` and `user_prompt`.
  - Configures conversation limits and system prompts.
  - Initializes HTTP headers for API interaction.
  - Sets up an LLM client and an agentic strategy for handling requests with specific configurations.

#### Methods

- **`run() -> dict`**
  - Executes the defined `agentic_strategy`.
  - Returns results, including conversation history and token usage statistics.

### Usage

The `ManageEngineAgent` class would typically be instantiated with a dictionary containing the required input fields. The primary use case involves interacting with a ManageEngine ServiceDesk by utilizing the class's `run` method to execute API interactions and retrieve service desk information.

This module is essential for software developers and IT managers looking to automate interactions with the ManageEngine ServiceDesk platform, enabling efficient ticket management through programmatic means.
