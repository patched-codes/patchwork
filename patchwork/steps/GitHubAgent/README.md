# GitHubAgent Documentation

## Overview

The `GitHubAgent` is part of the `patchwork` library, which is designed to automate tasks related to GitHub using large language models (LLMs). The `GitHubAgent` class provides a structured way to execute specific GitHub-related tasks with conversational inputs, leveraging the capabilities of the GitHub CLI and LLMs for execution and response.

## File Descriptions

### 1. `GitHubAgent.py`

This is the main implementation file for the `GitHubAgent`. It defines the business logic for executing tasks using GitHub CLI commands via an AI strategy.

#### Key Components:

- **`GitHubAgent` Class**: Inherits from `Step` and utilizes `GitHubAgentInputs` and `GitHubAgentOutputs` for data handling.
- **AgenticStrategyV2**: An AI strategy handling the task execution which employs OpenAI's model (`claude-3-7-sonnet-latest`) for processing conversational inputs.
- **GitHubTool**: Facilitates the execution of GitHub CLI commands using authenticated sessions.

#### Inputs

- **`base_path` (str)**: Path used by the GitHub CLI.
- **`prompt_value` (Dict)**: Variables for task template processing.
- **`task` (str)**: Description of the GitHub-related task to be executed.
- **API Keys**: Managed through various configuration options for accessing LLM services.

#### Outputs

- **`conversation_history` (List of Dict)**: Log of conversation exchanges during task execution.
- **`tool_records` (List of Dict)**: Information on commands executed and results obtained.
- **`request_tokens` (int)**: Count of tokens used in the LLM request.
- **`response_tokens` (int)**: Count of tokens received in the LLM response.

### 2. `typed.py`

Defines the structured data types for inputs and outputs of the `GitHubAgent`.

#### Key Components:

- **`__GitHubAgentRequiredInputs`**: Required inputs such as `task`.
- **`GitHubAgentInputs`**: Optional configuration for API keys and prompt values.
- **`GitHubAgentOutputs`**: Structured output containing conversation and execution details.

### 3. `__init__.py`

An empty file which indicates that `GitHubAgent` is a module in the `patchwork.steps.GitHubAgent` package. 

## Use Cases

The `GitHubAgent` is designed for developers and program managers who need to automate tasks requiring interaction with GitHub. An example scenario is fetching repository data or managing pull requests programmatically through dialogue-based task specifications.

Users need to configure API keys to use different LLM services and customize `prompt_value` for flexibility in task execution contexts. The results can be analyzed through token usage metrics and historical logs maintained in the outputs.
