# ManageEngine Agent Code Documentation

This documentation provides an overview of the code handling the ManageEngine Agent, detailing its structure, inputs, and outputs. The code is split into two primary files which define the types and implement the functionality of the ManageEngine Agent, facilitating integration with the ManageEngine ServiceDesk API.

## File Structure

- **Directory:** `patchwork/steps/ManageEngineAgent/`
  - **Typed Definition:** `typed.py`
  - **Agent Implementation:** `ManageEngineAgent.py`

## File: `typed.py`

### Purpose
Defines the input and output data types for the ManageEngine Agent using Python's `TypedDict`. This file is essential for ensuring type safety and clear expectations when using the ManageEngine Agent.

### Inputs

1. **__ManageEngineAgentInputsRequired ( TypedDict )**
    - `me_access_token`: `str`
    - `user_prompt`: `str`
    - `prompt_value`: `Dict[str, Any]`

2. **ManageEngineAgentInputs (extends __ManageEngineAgentInputsRequired)**
    - `max_agent_calls`: `int` (default is 1)
    - `openai_api_key`: Annotated `str`
    - `anthropic_api_key`: Annotated `str`
    - `google_api_key`: Annotated `str`
    - Optional Fields:
        - `system_prompt`: `Optional[str]`
        - `example_json`: `Optional[Dict]`

### Outputs

- **ManageEngineAgentOutputs (TypedDict)**
  - `conversation_history`: `List[Dict]`
  - `tool_records`: `List[Dict]`
  - `request_tokens`: `int`
  - `response_tokens`: `int`

## File: `ManageEngineAgent.py`

### Purpose
Implements the functionality of the ManageEngine Agent as an extended class of `Step`. The agent is designed to communicate with the ManageEngine ServiceDesk API, performing actions like retrieving, creating, or modifying service desk tickets using a conversational agent strategy.

### Initialization

- **Inputs Validation:** Ensures required keys (`me_access_token`, `user_prompt`) are provided.
- **Configuration:**
  - `conversation_limit` dictates the number of API calls.
  - Configures system and user prompts for interaction.

### Usage

- **HTTP Headers Setup:** Prepares necessary headers for API interaction.
- **Agent Configuration:** 
  - Uses `AioLlmClient` for handling language model interactions.
  - Implements `AgenticStrategyV2` tailored for ManageEngine operations.
  - Incorporates `APIRequestTool` for making authorized requests to ManageEngine.

### Execution

- **Method:** `run()`
  - Executes the agent strategy with the defined limit.
  - Returns interaction results augmented with usage statistics.

This codebase is targeted toward developers or software engineers needing automated interactions with ManageEngine ServiceDesk, making it easier to programmatically manage service desk operations while leveraging AI-powered conversational strategies.
