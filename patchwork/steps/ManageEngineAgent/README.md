# ManageEngine Agent

This module provides a `ManageEngineAgent` class used for interacting with the ManageEngine ServiceDesk through the ServiceDeskPlus API. It is designed to manage service desk tickets and related operations by leveraging an agent-based strategy and language models.

## Table of Contents

- [ManageEngineAgentInputs](#manageengineagentinputs)
- [ManageEngineAgentOutputs](#manageengineagentoutputs)
- [ManageEngineAgent Class](#manageengineagent-class)
  - [Initialization](#initialization)
  - [Functionality](#functionality)

## ManageEngineAgentInputs

### Inputs

- **zoho_access_token** (str, required): Access token required for authenticating API requests to the ManageEngine service.
- **user_prompt** (str, required): User prompt to guide the agent on the task to be performed.
- **prompt_value** (Dict[str, Any], required): Dictionary of prompt values used to render the user prompt.
- **max_agent_calls** (int, optional): Limit on the number of conversations. Defaults to 1.
- **openai_api_key** (str, optional): API key for OpenAI. Can be used as part of the authentication interchangeably with other API keys.
- **anthropic_api_key** (str, optional): API key for Anthropic. Can be used interchangeably with other API keys.
- **google_api_key** (str, optional): API key for Google. Can be used interchangeably with other API keys.
- **system_prompt** (str, optional): System-defined prompt text to provide context and guide the strategy.
- **example_json** (Dict, optional): JSON example for demonstrating expected interaction or formatting.

## ManageEngineAgentOutputs

### Outputs

- **conversation_history** (List[Dict]): List of conversational history records.
- **tool_records** (List[Dict]): Logs or records of tool usage during interaction.
- **request_tokens** (int): Number of tokens used in the request.
- **response_tokens** (int): Number of tokens in the response.

## ManageEngineAgent Class

The `ManageEngineAgent` class is the primary interface for users to automate interactions with the ManageEngine service. It extends a `Step` class, indicating its use within a workflow or process pipeline.

### Initialization

- The agent requires initialization with the `ManageEngineAgentInputs` dictionary, ensuring critical inputs like the `zoho_access_token` and `user_prompt` are provided.
- API headers are set up using the access token.
- A system prompt guides the logical flow, particularly focused on working within the ManageEngine ServiceDesk context.

### Functionality

- Utilizes the `AioLlmClient` and `AgenticStrategyV2` for engaging with language models.
- Leverages API tools to interact with ManageEngine's ServiceDeskPlus API for operations like ticket creation, modification, or information retrieval.
- The agent's run method executes the defined strategy, handling multiple conversation turns as defined by the input constraints.
- Returns a comprehensive dictionary including conversation history, tool usage records, and token usage metrics.

### Use Case

- Ideal for software developers, IT administrators, or service managers aiming to automate ticket management workflows and interactions with ManageEngine via an API.
- Supports dynamic rendering of prompts using user inputs for nuanced, contextual API operations.
- Useful as part of a larger orchestration system managing IT operations or customer service workflows.
