# GitHubAgent Module Documentation

## Overview

The GitHubAgent module is a component of the Patchwork software designed to facilitate interactions with the GitHub API using a highly configurable strategy driven by large language models (LLMs). The main functionality provided by this module revolves around executing tasks on GitHub using the GitHub CLI, under the guidance of a senior software developer acting role.

## Files

### GitHubAgent.py

This file defines the `GitHubAgent` class, which inherits from the `Step` class, designed to make use of the agent strategy for accomplishing user-defined tasks on GitHub. It utilizes the mustache templating system to dynamically format prompts, leveraging tools like `GitHubTool` and `AioLlmClient` to interact with GitHub and process tasks programmatically.

#### Inputs

- **Inputs**: `GitHubAgentInputs` consists of several fields like `task`, `base_path`, `prompt_value`, `max_llm_calls`, `openai_api_key`, `anthropic_api_key`, `google_api_key`, `client_is_gcp`.
  - *task (str)*: A description of the task to be performed.
  - *base_path (str, optional)*: The base path for executing GitHub commands. Defaults to the current working directory.
  - *prompt_value (dict, optional)*: A dictionary of data to be used in rendering the task prompt.
  - *max_llm_calls (int, optional in config)*: Configuration parameter limiting the number of LLM calls.
  - Several API keys (*openai_api_key, anthropic_api_key, google_api_key*) and configuration flags indicate which API set is active.

#### Outputs

- **Outputs**: `GitHubAgentOutputs` containing:
  - *request_tokens (int)*: Number of tokens used in requests.
  - *response_tokens (int)*: Number of tokens received in responses.

#### Usage

This module is intended for use in environments where programmatic control over GitHub operations is required. It is particularly useful for automation scripts and applications performing data retrieval and manipulation on GitHub repositories. Users can define tasks via templates and execute them using the tools provided.

### typed.py

This file defines the input and output schemas used by the `GitHubAgent` class. It contains two main classes:

- **GitHubAgentInputs**: Details the structure and types of data expected as inputs for a GitHub task.
- **GitHubAgentOutputs**: Defines the structure of the output results, including token usage statistics.

### __init__.py

This file is currently empty and serves as an initializer for the `GitHubAgent` package. 

## Conclusion

The `GitHubAgent` provides a structured approach to interfacing with the GitHub API using LLM-driven strategies. It's flexible enough to support various API configurations while offering precise control over GitHub tasks through templating and scripting methods. This module is essential for developers needing to automate and manage GitHub workflows programmatically.
