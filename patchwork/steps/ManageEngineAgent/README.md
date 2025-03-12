# ManageEngineAgent Module Documentation

This documentation covers the ManageEngineAgent module, which consists of two main Python files: `typed.py` and `ManageEngineAgent.py`. These files define classes and functions used to integrate with ManageEngine ServiceDesk using LLM (Large Language Model) strategies.

## File: patchwork/steps/ManageEngineAgent/typed.py

### Purpose

The `typed.py` file contains type definitions for the inputs and outputs used by the ManageEngineAgent. It leverages Python's `TypedDict` from the `typing_extensions` module to define expected input and output structures. 

### Inputs

- **`me_access_token` (str)**: Required access token for authentication with ManageEngine.
- **`user_prompt` (str)**: Required prompt value to be used for interacting with the API.
- **`prompt_value` (Dict[str, Any])**: Dictionary with dynamic prompt data.
- **`max_agent_calls` (int)**: Optional limit for the maximum number of calls to the agent.
- **`openai_api_key`, `anthropic_api_key`, `google_api_key`**: Annotated API keys for different LLM services, only one is needed as they are interchangeable.
- **`system_prompt` (Optional[str])**: An optional custom system prompt for the agent.
- **`example_json` (Optional[Dict])**: An optional example JSON structure for strategy configuration.

### Outputs

- **`conversation_history` (List[Dict])**: Logs of the interaction history.
- **`tool_records` (List[Dict])**: Records of tools used during execution.
- **`request_tokens` (int)**: The number of tokens used for requests.
- **`response_tokens` (int)**: The number of tokens received in responses.

## File: patchwork/steps/ManageEngineAgent/ManageEngineAgent.py

### Purpose

The `ManageEngineAgent.py` file contains the implementation of the `ManageEngineAgent` class, which integrates with the ManageEngine ServiceDesk using a configurable agent strategy. This agent is designed to manage service desk tickets and perform API interactions.

### Inputs

- Inherits from `ManageEngineAgentInputs`, with all input definitions as specified above.

### Functionality

1. **Initialization**: The constructor checks for required inputs (`me_access_token` and `user_prompt`) and initializes various configuration settings, such as conversation limits and system prompts.

2. **LLM Client Configuration**: Configures a language model client (`AioLlmClient`) to handle natural language processing needs.

3. **Agentic Strategy**: Sets up an `AgenticStrategyV2` object to handle dialogues with the model `claude-3-7-sonnet-latest`, enriching prompts with specific context for managing service desk operations through the ManageEngine API.

4. **Proprietary API Interaction**: Illustrates how to configure an API request tool for communication with ManageEngine using dynamically generated headers and request methods.

### Outputs

- The `run` method returns a dictionary of results from executing the agentic strategy, including usage statistics (tokens used).

### Usage

This module is intended for developers managing service desk operations with ManageEngine, who want to enhance their interaction with automated, natural language-driven agents. By configuring inputs and executing the `ManageEngineAgent`, users can automate ticket management tasks efficiently.
