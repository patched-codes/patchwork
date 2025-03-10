# ManageEngine Agent Documentation

This documentation provides an overview of the `ManageEngineAgent` implementation and its functionality. It includes allocated sections discussing the inputs and outputs necessary for utilizing this agent within the `patchwork` application.

## Overview

The `ManageEngineAgent` is designed to facilitate interactions with the ManageEngine ServiceDesk via the ServiceDeskPlus API. It allows for retrieval, creation, or modification of service desk tickets and related information by leveraging a multi-turn conversational strategy. This code is split into two main files: `typed.py` and `ManageEngineAgent.py`.

## File: `typed.py`

### Inputs

The inputs are defined using the `ManageEngineAgentInputs` class, which is a `TypedDict`. It includes both required and optional input parameters:

- **Required Inputs:**
  - `me_access_token` (str): Access token for authenticating with ManageEngine API.
  - `user_prompt` (str): User prompt for the agent.
  - `prompt_value` (Dict[str, Any]): Values to render in the prompt.

- **Optional Inputs:**
  - `max_agent_calls` (int): Maximum number of conversational turns allowed.
  - `openai_api_key` (str): API key for OpenAI, used as an alternative authentication.
  - `anthropic_api_key` (str): API key for Anthropic, used as an alternative authentication.
  - `google_api_key` (str): API key for Google, used as an alternative authentication.
  - `system_prompt` (Optional[str]): System prompt configuration.
  - `example_json` (Optional[Dict]): Example JSON data used in prompts.

### Outputs

The outputs are defined using the `ManageEngineAgentOutputs` class, another `TypedDict`:

- **Outputs:**
  - `conversation_history` (List[Dict]): A log of the conversation's history.
  - `tool_records` (List[Dict]): A record of tool interactions during the session.
  - `request_tokens` (int): Count of tokens processed in requests.
  - `response_tokens` (int): Count of tokens processed in responses.

## File: `ManageEngineAgent.py`

### Functionality

The `ManageEngineAgent` class inherits from `Step` and uses both input and output classes defined in `typed.py`. Its main duties include:

1. **Initialization:** 
   - Checks for required inputs (`me_access_token`, `user_prompt`).
   - Configures headers for API interaction and prepares system prompts.

2. **Configuration:**
   - Sets up the agent using the `AgenticStrategyV2` strategy for multi-turn conversations.
   - Utilizes the `AioLlmClient` to establish a client for large language model interactions.

3. **Execution:**
   - `run()` method executes the agent strategy, limits to defined conversation turns, and returns the result along with usage data.

### How To Use

To use the `ManageEngineAgent`, instantiate it with a dictionary of inputs and call `run()` to execute the interaction process. This will result in interactions with the ManageEngine API, processing outputs which include data retrieval, report generation, or modifications based on conversational prompts and user inputs.

This setup is suitable for developers aiming to integrate detailed support ticket operations within a conversational AI framework they control or extend.
