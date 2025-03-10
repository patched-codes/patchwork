# GitHubAgent Module Documentation

## Overview

The GitHubAgent module is a part of a larger pipeline designed to automate interactions with GitHub using AI-powered strategies. This module primarily serves as an interface to perform tasks involving GitHub data retrieval using natural language instructions. It leverages an agentic strategy pattern to execute tasks through a language model interface and interfaces with GitHub using a command-line interface (CLI).

## Contents

This module consists of the following files:

- **GitHubAgent.py**: Implements the core logic for the GitHubAgent class, which processes input to interact with GitHub.
- **typed.py**: Defines type annotations and input/output structures for the GitHubAgent.
- **__init__.py**: Placeholder for package initialization.

---

## GitHubAgent.py

### Description

The `GitHubAgent` class provides an interface for executing commands involving GitHub tasks using AI. It uses an agentic strategy to interact with GitHub's command-line interface (CLI). The class takes user inputs, processes them using a language model client, and performs the specified task on GitHub.

### Inputs

The `GitHubAgent` class requires input data structured as `GitHubAgentInputs`, which includes:

- `task` (str): The task to be executed.
- `base_path` (str, optional): The path where GitHub operations are to be performed.
- `prompt_value` (dict): Data required for rendering a task.
- API keys for language model configuration:
  - `openai_api_key` (str, config)
  - `anthropic_api_key` (str, config)
  - `google_api_key` (str, config)
- `max_llm_calls` (int, config): Maximum number of language model calls allowed.

### Outputs

The `GitHubAgent` produces output data structured as `GitHubAgentOutputs`, containing:

- `request_tokens` (int): Number of tokens used for requests.
- `response_tokens` (int): Number of tokens received in responses.

### Usage

To use the `GitHubAgent`, initialize it with the required inputs, and call the `run()` method to execute the specified GitHub task. This will interact with GitHub's CLI through the predefined agent strategy and return relevant output data.

```python
inputs = GitHubAgentInputs(
    task='Describe your task here',
    base_path='/path/to/directory',
    prompt_value={'key': 'value'},
    openai_api_key='your-openai-api-key',
    max_llm_calls=10
)

agent = GitHubAgent(inputs)
result = agent.run()
```

---

## typed.py

### Description

This file contains the type annotations for inputs and outputs necessary for the `GitHubAgent` class. It provides structured data definitions to enforce type safety and ensure that the inputs/outputs comply with expected formats.

### Types Defined

- `__GitHubAgentRequiredInputs`: Mandatory fields for inputs.
- `GitHubAgentInputs`: Extends required inputs with optional configuration fields.
- `GitHubAgentOutputs`: Structure for outputs returned by the agent.

---

## __init__.py

### Description

The `__init__.py` is a placeholder file for initializing the Python package. It does not contain any functional code but signals that the directory can be treated as a package module.

--- 

This documentation should serve as a reference for developers integrating the `GitHubAgent` into their applications, taking advantage of its capabilities to automate GitHub CLI tasks through AI strategies.
