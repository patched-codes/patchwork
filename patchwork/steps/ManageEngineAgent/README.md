# ManageEngineAgent Module Documentation

This documentation provides an overview of the `ManageEngineAgent` module designed for interaction with ManageEngine ServiceDesk via API calls. It allows the configuration and execution of tasks such as retrieving, creating, or modifying service desk tickets.

## Overview

The module consists of three primary Python files:

1. **typed.py:** Defines input and output data structures using `TypedDict`.
2. **__init__.py:** Contains initialization code for the package.
3. **ManageEngineAgent.py:** Implements the `ManageEngineAgent` class which performs the main functionality of interacting with the ManageEngine ServiceDesk.

## Inputs

The `ManageEngineAgent` class requires a dictionary of inputs specified in the `ManageEngineAgentInputs` data structure. The fields include:

- **Required Inputs:**
  - `zoho_access_token`: A required string for authorization.
  - `user_prompt`: A string that defines the initial prompt for user interaction.
  - `prompt_value`: A dictionary containing data related to the prompt.

- **Optional Inputs:**
  - `max_agent_calls`: An integer to limit the number of conversation rounds (default is 1).
  - `openai_api_key`, `anthropic_api_key`, `google_api_key`: Strings for API keys with logical OR operation between them.
  - `system_prompt`: Optional prompt for configuring the system's initial state.
  - `example_json`: An optional dictionary providing example structures.

## Outputs

The outputs of the `ManageEngineAgent` are defined in the `ManageEngineAgentOutputs` data structure, which includes:

- `conversation_history`: A list of dictionaries containing the conversation flow.
- `tool_records`: A list of dictionaries capturing tool interaction details.
- `request_tokens`: An integer count of tokens used in the request.
- `response_tokens`: An integer count of tokens used in the response.

## Functionality

### Initialization

When an instance of `ManageEngineAgent` is created, it initializes the headers for API requests and configures the agent-based strategy for interacting with the ManageEngine ServiceDesk. The strategy is tailored to allow communication through AI models while using predefined tools.

### Execution

The primary method, `run()`, executes the configured agentic strategy for a specified number of interactions (`max_agent_calls`). It leverages the `AgenticStrategyV2` with contextual prompts to achieve this goal, interfacing with the ManageEngine API to perform required operations.

### Error Handling

The class raises a `ValueError` if the `zoho_access_token` or `user_prompt` is not provided, ensuring necessary context and authorization for API interactions.

## Use Case

This module is useful for developers aiming to integrate AI-driven task handling within the ManageEngine ServiceDesk environment. It supports making complex API requests in a conversational manner and streamlines interaction with service management tasks programmatically.
