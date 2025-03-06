# Documentation: ManageEngineAgent Module

This module provides an interface to interact with the ManageEngine ServiceDesk via ServiceDeskPlus API, leveraging OpenAI's AI capabilities. It is implemented in two Python files: `typed.py` for type definitions and `ManageEngineAgent.py` for the main class implementation.

## File: `typed.py`

### Description
This file defines the input and output data structures using TypedDict for the `ManageEngineAgent` class.

### Inputs

- **ManageEngineAgentInputs**: 
  - `me_access_token` (str): The access token for ManageEngine API authentication. *(Required)*
  - `max_agent_calls` (int): The max number of calls the agent is allowed to make. Default is 1.
  - `openai_api_key`, `anthropic_api_key`, `google_api_key` (Annotated[str]): One of these API keys is needed for the LLM client configuration.
  - `system_prompt` (Optional[str]): A prompt template for initial system configuration.
  - `user_prompt` (str): A prompt that initializes user interaction. *(Required)*
  - `example_json` (Optional[Dict]): Example JSON data used for configuration.

### Outputs

- **ManageEngineAgentOutputs**: 
  - `conversation_history` (List[Dict]): The list of conversation records.
  - `tool_records` (List[Dict]): The list of tool usage records.
  - `request_tokens` (int): The number of tokens requested.
  - `response_tokens` (int): The number of tokens in the response.

## File: `ManageEngineAgent.py`

### Description
This file implements the `ManageEngineAgent` class, which extends the `Step` class, incorporating the input and output definitions from `typed.py`.

### Inputs

- **Initialization**: 
  - The constructor takes a dictionary `inputs` adhering to `ManageEngineAgentInputs`.
  - Raises `ValueError` if either `me_access_token` or `user_prompt` are missing.

### Outputs

- **Run Method**: 
  - The `run` method executes the agentic strategy and returns results from the API interaction along with usage information encapsulated as a dictionary.

### Features
- **AI Integration**: Uses `AioLlmClient` to handle AI-driven interaction and `AgenticStrategyV2` to manage conversation strategy.
- **API Communication**: Utilizes the `APIRequestTool` for making requests to the ManageEngine API.
- **Prompt Configuration**: Includes both system-level and user-level prompts for conversation guidance.
- **Agent Configuration**: Pre-configured agent setup specific to ManageEngine's requirements.

## Usage

A developer or integrator can use the `ManageEngineAgent` class to streamline interactions with the ManageEngine ServiceDesk through AI-enhanced strategies. To make it operational, valid API tokens must be provided along with prompts that guide the tasks to be performed within the ManageEngine ecosystem.

This module is suitable for tasks like retrieving, creating, or modifying service desk tickets by interacting through an AI agent configured with the ManageEngine-specific API context.
