# GitHubAgent Documentation

## Overview
The `GitHubAgent` class is designed to facilitate interactions with GitHub using the GitHub CLI. It is implemented as a custom step in a larger system which involves an agentic strategy to automate tasks on GitHub. This step is particularly suitable for users needing to programmatically access and manage GitHub data through a user task-based approach.

## Components

### GitHubAgent
- **Location**: `patchwork/steps/GitHubAgent/GitHubAgent.py`
- **Purpose**: Utilizes OpenAI and GitHub APIs to execute specified tasks on GitHub.
- **Dependencies**: Imports several classes and utilities such as `AioLlmClient`, `AgentConfig`, `AgenticStrategyV2`, and `GitHubTool`.
- **Class Signature**: `GitHubAgent(Step, input_class=GitHubAgentInputs, output_class=GitHubAgentOutputs)`

## Inputs

### GitHubAgentInputs
- **task (str)**: Required. The specific task to be executed on GitHub.
- **base_path (str)**: The base directory path for operations, defaults to current working directory.
- **prompt_value (Dict[str, Any])**: A dictionary of additional prompt values.
- **max_llm_calls (int)**: Maximum number of calls allowed to the language model.
- **openai_api_key, anthropic_api_key, google_api_key (str)**: API keys for accessing respective services. Configurable and interchangeable via logical operations.

## Outputs

### GitHubAgentOutputs
- **request_tokens (int)**: Number of tokens used for making the request.
- **response_tokens (int)**: Number of tokens received in response.

## How it Works
- The `GitHubAgent` is initialized with inputs based on `GitHubAgentInputs`.
- Uses an agentic strategy (`AgenticStrategyV2`) with a predefined system and user prompt to guide the operation.
- Communicates with GitHub through a toolset and accesses it using an authenticated `gh` CLI app.
- The execution results are processed and returned as a dictionary containing usage statistics.

## Usage
To use the `GitHubAgent`, instantiate the class with the required inputs and call the `run()` method to execute the defined tasks on GitHub. The output will include relevant token usage data, assisting in monitoring and optimization of API interaction costs.

```python
# Example usage
inputs = {
    "task": "List all repositories for a user",
    "base_path": "/home/user/projects",
    "prompt_value": {},
    "max_llm_calls": 5,
    "openai_api_key": "your_openai_key",
}
github_agent = GitHubAgent(inputs)
output = github_agent.run()
print(output)
```

## File Structure

### `GitHubAgent.py`
- Contains the main class and logic for task execution on GitHub.

### `typed.py`
- Defines input and output data types for `GitHubAgent`.

### `__init__.py`
- Currently empty, meant for module initialization.

This implementation is suited for software developers and project managers who require scripted interactions with GitHub while maintaining flexibility in their task definitions and output handling.
