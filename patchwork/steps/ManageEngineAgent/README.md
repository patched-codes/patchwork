# ManageEngineAgent Documentation

## Overview

The `ManageEngineAgent` code provides an interface between a chatbot agent and the ManageEngine ServiceDesk API, utilizing various API keys for OpenAI, Anthropic, and Google as alternatives to execute large language model (LLM) interactions. This code is structured to define the required inputs and expected outputs, focusing on facilitating automated interactions with ManageEngine's ServiceDesk, which is especially useful for software developers aiding program managers in managing tickets and service desk tasks programmatically.

## Files and Descriptions

### 1. `typed.py`
This file defines the input and output types for the ManageEngineAgent, ensuring type safety and clarity of required and optional fields.

#### Inputs
- **`zoho_access_token` (str)**: Required for authorization with Zoho.
- **`user_prompt` (str)**: Required prompt for user input to the agent.
- **`prompt_value` (Dict[str, Any])**: Dictionary containing values that may be needed for rendering templated user prompts.
- **Optional Inputs**:
  - `max_agent_calls` (int)
  - `openai_api_key` (str)
  - `anthropic_api_key` (str)
  - `google_api_key` (str)
  - `system_prompt` (str)
  - `example_json` (Dict)

#### Outputs
- **`conversation_history` (List[Dict])**
- **`tool_records` (List[Dict])**
- **`request_tokens` (int)**
- **`response_tokens` (int)**

### 2. `__init__.py`
This init file currently serves as a placeholder and does not contain any code.

### 3. `ManageEngineAgent.py`
This file contains the implementation of the `ManageEngineAgent` class, providing the operational logic to interface with the ManageEngine API using the defined input and output structures.

#### Components
- **Initialization**:
  - Validates required inputs (`zoho_access_token`, `user_prompt`).
  - Sets headers for API requests using the Zoho access token.
  - Configures an AI client (LLM client) and the agent strategy.
  
- **Agent Strategy**:
  - Provides interaction with ManageEngine to retrieve, create, or modify service desk tickets.
  - Uses `AgenticStrategyV2` to define models and tool sets.
  
- **Methods**:
  - **`run()`**: Executes the agent strategy and returns the result along with usage statistics.

## How to Use
1. **Input Configuration**: Populate `ManageEngineAgentInputs` with the required fields like `zoho_access_token` and `user_prompt`.
2. **Run the Agent**: Instantiate the `ManageEngineAgent` with the inputs and call the `run()` method to perform the desired operations.
3. **Extract Results**: Review the output from `ManageEngineAgentOutputs` to analyze the conversation history and API interaction results.

This setup provides automation and intelligent processing for managing service desk operations, making it a valuable tool for software development and support teams.
