# ManageEngine Agent Documentation

This documentation covers the two Python files located in the `patchwork/steps/ManageEngineAgent/` directory: `typed.py` and `ManageEngineAgent.py`. These files are integral to the functioning of the ManageEngine Agent, which interacts with ManageEngine ServiceDesk to perform various operations using API calls.

## File: `typed.py`

### Purpose

The `typed.py` file defines the input and output data structures for the ManageEngine Agent. These data structures dictate the required and optional fields necessary for successfully executing the agent's tasks.

### Inputs

- **`me_access_token` (str)**: Required. A token for authenticating with the ManageEngine API.
- **`user_prompt` (str)**: Required. A prompt that describes the user's request or intent.
- **`prompt_value` (Dict[str, Any])**: Required. A dictionary of placeholder values for the user prompt.
- **`max_agent_calls` (int)**: Optional. The maximum number of API calls the agent can make in a conversation.
- **`openai_api_key` (str)**: Annotated. Optional key with alternates for OpenAI services.
- **`anthropic_api_key` (str)**: Annotated. Optional key with alternates for Anthropic services.
- **`google_api_key` (str)**: Annotated. Optional key with alternates for Google services.
- **`system_prompt` (Optional[str])**: An optional system-level prompt for guiding the agent behavior.
- **`example_json` (Optional[Dict])**: An optional dictionary of example inputs for reference.

### Outputs

- **`conversation_history` (List[Dict])**: A list of dictionaries representing the conversation.
- **`tool_records` (List[Dict])**: A list of records concerning tool interactions.
- **`request_tokens` (int)**: The number of tokens used in API requests.
- **`response_tokens` (int)**: The number of tokens received in API responses.

## File: `ManageEngineAgent.py`

### Purpose

The `ManageEngineAgent.py` file implements the ManageEngine Agent, which leverages the defined data structures to interact programmatically with the ManageEngine ServiceDesk via its API. The agent parses inputs to configure API headers, prompts, and tools for service desk operations.

### Inputs

- The constructor accepts a dictionary following the `ManageEngineAgentInputs` structure.

### Outputs

- The `run()` method returns a dictionary combining the results of the agentic strategy execution and associated usage data following the `ManageEngineAgentOutputs` structure.

### Functionality

- **Initialization**: Initializes with required inputs, setting conversation limits and preparing prompts.
- **Authentication and Headers**: Sets up API authentication using the provided `me_access_token`.
- **Client Creation**: Utilizes `AioLlmClient` to create an asynchronous LLM client with the given API keys.
- **Strategy Configuration**: Configures an `AgenticStrategyV2` to interact with the API using specified tools and prompts.
- **Execution**: The `run` method executes the agentic strategy to interact with the ManageEngine API and returns the results along with token usage data.

### Usage

This agent is likely used by developers or IT admins who want to automate interactions with ManageEngine ServiceDesk for tasks like retrieving, creating, or modifying service desk tickets. Users must provide authentication tokens and relevant prompts to ensure correct API interactions.
