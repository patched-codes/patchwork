# ManageEngine Agent Documentation

## Overview

This documentation provides an overview of the ManageEngine Agent code, which consists of two main files: `typed.py` and `ManageEngineAgent.py`. The code defines a system that allows interaction with the ManageEngine ServiceDesk via an API using a tailored agent strategy. Users can utilize it to create, modify, or retrieve service desk tickets by providing necessary input configurations and leveraging OpenAI, Google, or Anthropic API keys for language model processing.

## Inputs

### Required Inputs

These inputs are necessary for initializing the ManageEngineAgent:

- **me_access_token** (`str`): A token required for authentication with the ManageEngine API.
- **user_prompt** (`str`): A prompt provided by the user, which guides the agent's task.
- **prompt_value** (`Dict[str, Any]`): A dictionary containing dynamic values to render within the prompt.

### Optional Inputs

These inputs can be provided to customize the agent behavior:

- **max_agent_calls** (`int`, default `1`): The maximum number of agent calls to process in a session.
- **openai_api_key** (`str`): API key for OpenAI services.
- **anthropic_api_key** (`str`): API key for Anthropic services.
- **google_api_key** (`str`): API key for Google services.
- **system_prompt** (`Optional[str]`): System-level instructions to the agent.
- **example_json** (`Optional[Dict]`): Example structure to guide the agent's response formatting.

## Outputs

The result from running the ManageEngine Agent includes:

- **conversation_history** (`List[Dict]`): A history of the interactions processed by the agent.
- **tool_records** (`List[Dict]`): Records of the API calls or tool usage by the agent.
- **request_tokens** (`int`): Number of tokens processed in the request.
- **response_tokens** (`int`): Number of tokens in the response.

## Usage

To use the ManageEngine Agent:

1. **Initialization**: Create an instance of `ManageEngineAgent` with suitable inputs, including API keys and prompts.
2. **Execution**: Call the `run()` method to execute the agentic strategy. The method handles the interaction with the ManageEngine API, performs necessary transformations on the prompts, and processes tasks as defined in the setup.
3. **Result Handling**: The `run()` method returns a dictionary containing the conversation history, tool usage, and token statistics, allowing users to analyze or further process the results.

```python
inputs = {
    "me_access_token": "your_access_token",
    "user_prompt": "Retrieve all open tickets",
    "prompt_value": {"department": "IT"},
    "max_agent_calls": 5
}

agent = ManageEngineAgent(inputs)
result = agent.run()
```

By integrating this agent into systems, users can automate and streamline interactions with the ManageEngine ServiceDesk, making service management more efficient and automated.
