# ManageEngineAgent Documentation

## Overview

The `ManageEngineAgent` integration facilitates seamless interaction between an application and the ManageEngine ServiceDesk Plus via the ServiceDeskPlus API. This component is designed to automate the management of service desk tickets through conversations, leveraging language models for natural language processing.

## `typed.py`

### Inputs

- **zoho_access_token** (`str`): Required authentication token for Zoho.
- **user_prompt** (`str`): Required prompt string for user input.
- **prompt_value** (`Dict[str, Any]`): Dictionary containing the values for the prompts.
  
*Optional Fields:*

- **max_agent_calls** (`int`): Maximum number of calls the agent can handle.
- **openai_api_key** (`str`): API key alternative for OpenAI, which can be used interchangeably with the Anthropic or Google API keys.
- **anthropic_api_key** (`str`), **google_api_key** (`str`): API key options for Anthropic and Google, respectively.
- **system_prompt**, **example_json**: Optional fields for additional prompt and configuration.

### Outputs

- **conversation_history** (`List[Dict]`): History of conversation exchanges.
- **tool_records** (`List[Dict]`): Records of the tool's activities.
- **request_tokens** (`int`), **response_tokens** (`int`): Token counts for requests and responses.

## `ManageEngineAgent.py`

### Description

The `ManageEngineAgent` class extends the `Step` class to set up the environment for agent interaction with the ManageEngine API. It utilizes the `AgenticStrategyV2` for managing conversation flows with the necessary configuration.

### Key Functionalities

- **Initialization**: Confirms input provision (mandatory `zoho_access_token` and `user_prompt`).
- **Agent Configuration**: Prepares headers with the Zoho authentication token and sets up the `AioLlmClient` using provided prompts.
- **Strategy Execution**: Implements a conversation strategy with the `AgenticStrategyV2`, which is contoured with specific instructions for API interaction.

### Execution

```python
def run(self) -> dict:
    # Execute the agentic strategy
    result = self.agentic_strategy.execute(limit=self.conversation_limit)

    # Return results with usage information
    return {**result, **self.agentic_strategy.usage()}
```

This method runs the defined agent strategy and returns the results in conjunction with usage metrics.

## Typical Usage

A developer would use this component to automate service desk operations by creating an instance of `ManageEngineAgent` with the appropriate input data and executing the `run` method. The agent facilitates direct API interactions based on conversational inputs, which simplifies managing service tickets through ManageEngine's API.

Ensure all required tokens and prompt configurations are correctly set up to achieve successful execution and desired productivity enhancements.
