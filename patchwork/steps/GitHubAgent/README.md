# GitHub Agent Documentation

## Overview

The GitHub Agent is a component within the `patchwork` system designed to interface with GitHub using natural language instructions. It leverages the power of an LLM (Large Language Model) to interpret tasks and fetch data from GitHub by executing the GitHub CLI commands.

This agent can be particularly useful for software developers, project managers, and data analysts who need to automate the retrieval of data from GitHub repositories or other tasks that involve interacting with GitHub's services.

## Inputs

### `GitHubAgentInputs` (Defined in `typed.py`)

- **task (required)**: A string describing the task that needs to be performed using the GitHub CLI.
- **base_path**: A string representing the base directory path to be used. Defaults to the current working directory.
- **prompt_value**: A dictionary containing data used for rendering the task description using a mustache template.
- **max_llm_calls**: An integer configuration for limiting the number of LLM calls.
- **openai_api_key, anthropic_api_key, google_api_key**: Annotated strings for API key configuration. These keys are used for LLM services and are interchangeable based on availability.

## Outputs

### `GitHubAgentOutputs` (Defined in `typed.py`)

- **conversation_history**: A list of dictionaries capturing the history of the conversation.
- **tool_records**: A list of dictionaries detailing the use of tools during the task execution.
- **request_tokens**: An integer indicating the number of tokens used in the request phase.
- **response_tokens**: An integer indicating the number of tokens used in the response phase.

## Core Functionality

The GitHub Agent, defined in `GitHubAgent.py`, utilizes `AgenticStrategyV2` to interpret the task described in natural language and translate it into actionable commands using the GitHub CLI. The agent structure facilitates:

1. **LLM Integration**: Using `AioLlmClient`, the agent communicates with a language model to comprehend and process input tasks.
2. **Data Rendering**: The tasks are rendered using the `mustache_render` function to integrate dynamic data into the task description.
3. **GitHub Interaction**: Through the `GitHubTool`, authenticated CLI commands are executed to fulfill the task.
4. **Agent Configuration**: `AgentConfig` helps configure the agent, specifying tools and system prompts essential for task execution.
5. **Output Composition**: Upon execution, results are compiled along with usage statistics to ensure comprehensive feedback on the operation conducted.

## Usage

To use the GitHub Agent, instantiate it with the necessary inputs and call the `run` method to perform the designated task. The output will include details of the execution process and any data fetched from GitHub.

```python
inputs = GitHubAgentInputs(
    task="List all open issues in the repository.",
    base_path="/some/path",
    prompt_value={"repo_name": "example-repo"},
    max_llm_calls=5,
    openai_api_key="your-openai-api-key"
)

agent = GitHubAgent(inputs)
result = agent.run()
```

This setup allows the GitHub Agent to serve as an extensible and intelligent interface for GitHub operations, driven by natural language inputs and augmented by LLM capabilities for enhanced automation and accuracy.
