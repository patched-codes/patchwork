# ManageEngineAgent Code Documentation

## Overview
The ManageEngineAgent code provides a structured way to interact with ManageEngine ServiceDesk by leveraging Large Language Models (LLMs). The agent is configured to facilitate communication with the ManageEngine ServiceDesk API, enabling the retrieval, creation, and modification of service desk tickets, as well as managing conversation records.

## File: `typed.py`

### Description
This file defines the input and output structure for the `ManageEngineAgent` using the Python `TypedDict` mechanism. This provides type safety and clarity for the data being passed into and out of the agent.

### Inputs
`ManageEngineAgentInputs` includes required and optional parameters:
- **Required Fields:**
  - `zoho_access_token`: A string token used for authentication with the Zoho API.
  - `user_prompt`: A string prompt provided by the user.
  - `prompt_value`: A dictionary of additional context for the user prompt.
  
- **Optional Fields:**
  - `max_agent_calls`: An integer specifying the maximum number of calls the agent can make.
  - `openai_api_key`, `anthropic_api_key`, `google_api_key`: Annotated strings potentially used for integrating LLMs.
  - `system_prompt`: An optional string to configure the agent's system prompt.
  - `example_json`: An optional dictionary containing example usage data.

### Outputs
`ManageEngineAgentOutputs` defines the expected output:
- **Fields:**
  - `conversation_history`: A list of dictionaries recording the conversation history.
  - `tool_records`: A list of dictionaries detailing the tools used in operations.
  - `request_tokens`: An integer representing the tokens used in requests.
  - `response_tokens`: An integer representing the tokens received in responses.

## File: `ManageEngineAgent.py`

### Description
This file implements the `ManageEngineAgent` class, a customizable agent utilizing the defined inputs and outputs to handle interactions with the ManageEngine ServiceDesk. It integrates AI strategies for dynamic conversation management.

### Inputs
- **`inputs`**: A dictionary containing configuration settings as defined in `ManageEngineAgentInputs`.

### Outputs
- The `run()` method returns a dictionary combining the execution results and usage statistics for the conversation.

### Key Components

- **Initialization**: 
  - Verifies required inputs (`zoho_access_token` and `user_prompt`).
  - Configures conversation limit and system prompts.
  - Sets headers using the Zoho access token for API requests.
  - Instantiates an LLM client to assist in conversation management.

- **Agentic Strategy**:
  - Uses `AgenticStrategyV2` to define interaction protocols, focusing on service desk operations.
  - Employs a toolset, particularly `APIRequestTool`, for making API requests.

- **Execution**:
  - The `run()` method executes the agentic strategy, retrieving results and token usage information.

### Usage
The ManageEngineAgent is typically used within systems that require automated interactions with the ManageEngine ServiceDesk, supporting operations like ticket management via API calls enhanced by LLM-driven conversation capabilities.
