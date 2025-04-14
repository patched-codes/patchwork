# GitHubAgent Documentation

## Overview

The `GitHubAgent` module within the `patchwork` library provides a specialized tool to interface with GitHub using an agentic strategy. The agent is designed to perform tasks on GitHub by leveraging the CLI and Long Language Models (LLMs) to execute sequences of actions based on user prompts. 

## Structure

This module consists of three main files:

1. `GitHubAgent.py` - The core implementation of the GitHubAgent.
2. `typed.py` - Definitions for input and output data structures used by the agent.
3. `__init__.py` - Marks the directory as a Python package.

## `GitHubAgent.py`

### Description

The `GitHubAgent` class inherits from the `Step` class and implements a system that uses the `AgenticStrategyV2`. This agent uses language model clients to process tasks via an agent configurator pattern tailored for interacting with GitHub.

### Inputs

- **base_path**: `str` (optional)  
  The base directory path, defaulting to the current working directory.

- **prompt_value**: `Dict[str, Any]` (optional)  
  Data used within the task rendering.

- **task**: `str`  
  A task description written in a mustache template format used to facilitate GitHub operations.

- **example_json**: `str` (optional)  
  A JSON string showing an example of the expected result format.

- **github_api_key**: `str`  
  The API key used for authenticating GitHub CLI operations.

### Outputs

- **request_tokens**: `int`  
  The number of tokens used in the request phase.

- **response_tokens**: `int`  
  The number of tokens received in the response phase.

### Usage

The `GitHubAgent` runs by executing its `run` method, which processes the input task, interacts with the GitHub API, and returns the results along with LLM usage statistics.

## `typed.py`

### Description

Defines the structure of inputs and outputs the `GitHubAgent` expects and generates. It includes required configurations and optional parameters for flexibility in task execution.

### Structures

- **GitHubAgentInputs**: A typed dictionary that includes mandatory fields like `github_api_key` and `task`, along with optional configurations and API keys.

- **GitHubAgentOutputs**: A typed dictionary that contains token usage metrics.

## `__init__.py`

This file initializes the `GitHubAgent` directory as a Python package. It does not contain code but allows for the import and use of the `GitHubAgent` module within the broader `patchwork` library.

## Conclusion

This module is intended for developers and engineers who need to automate or simplify interactions with GitHub. By abstracting the complexity of managing GitHub API calls with LLMs, users can easily define tasks and receive structured outputs.
