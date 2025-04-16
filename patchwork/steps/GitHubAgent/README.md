# GitHubAgent Module Documentation

This module provides functionality to interact with GitHub based systems by creating a configurable agent using an LLM-based strategy. It is useful for developers who need to automate interactions with GitHub repositories via the GitHub CLI, including tasks like retrieving data from repositories.

## Contents

1. **GitHubAgent.py** - Defines the main `GitHubAgent` class responsible for executing tasks using a strategy-based approach.
2. **typed.py** - Contains type definitions for inputs and outputs used by the `GitHubAgent`.
3. **__init__.py** - An initializer for the module, currently empty.

## `GitHubAgent.py`

### Overview

The `GitHubAgent.py` file defines a `GitHubAgent` class, which utilizes an agent strategy to perform tasks on GitHub by leveraging multi-turn conversations facilitated by a backend AI client. Specifically, it utilizes the `AgenticStrategyV2` class to process tasks and interact with the GitHub CLI.

### Inputs

- **GitHubAgentInputs**
  - `github_api_key` (str): Required. The API key for accessing GitHub.
  - `task` (str): Required. A description of the task to perform.
  - `base_path` (str): Optional. The base path for execution, defaults to the current working directory.
  - `prompt_value` (dict): Optional. Data for template rendering.
  - `max_llm_calls` (int): Optional, config. Maximum number of LLM API calls allowed.
  - `example_json` (str): Optional. JSON string with example actions.
  - `openai_api_key` (str), `anthropic_api_key` (str), `google_api_key` (str), `client_is_gcp` (str): Various optional config API keys.

### Outputs

- **GitHubAgentOutputs**
  - `request_tokens` (int): Number of tokens used in the request.
  - `response_tokens` (int): Number of tokens used in the response.

### Usage

To use the `GitHubAgent`, instantiate it with input parameters, and then call the `run()` method. The method returns a dictionary containing results from GitHub interactions, including usage statistics like token counts.

```python
inputs = {
    "github_api_key": "your_key_here",
    "task": "Retrieve list of repositories",
    # ... other optional parameters
}

agent = GitHubAgent(inputs)
result = agent.run()
print(result)
```

## `typed.py`

### Overview

This file contains Python type definitions to ensure structured inputs and outputs for the `GitHubAgent` class. It uses `TypedDict` for strict typing checks.

## `__init__.py`

### Overview

This file is provided to initialize the GitHubAgent module package, though it currently contains no specific code.

---

This module is designed for developers needing to automate and streamline their GitHub-related workflows using AI-enhanced operations directly interfaced with the GitHub CLI. By offering structured input and output typing, it ensures a consistent and predictable integration experience.
