# GitHubAgent Module Documentation

## Overview

The GitHubAgent module provides functionality to interact with GitHub through a conversational agent. This agent utilizes AI models and the GitHub CLI to perform tasks as directed by user prompts. The module consists of three main files:

1. `GitHubAgent.py`: Contains the main implementation of the `GitHubAgent` class, responsible for executing tasks using a conversational strategy.
2. `typed.py`: Defines input and output types for the GitHubAgent, enabling type-safe configuration and interaction.
3. `__init__.py`: Initializes the module.

---

## GitHubAgent.py

### Description
The core functionality of the module, encapsulated in the `GitHubAgent` class, which uses an agentic strategy for managing interactions with GitHub. The class utilizes a Language Model (LLM) client to derive instructions from prompts and execute them using the GitHub CLI.

### Inputs

- **`base_path`**: *str* (optional)  
  Directory path for operations, defaults to the current working directory.
  
- **`task`**: *str*  
  Task description for which the GitHub CLI must be used.

- **`github_api_token`**: *str*  
  GitHub API token for authentication.

- **`example_json`**: *dict* (optional)  
  Example JSON data for guiding the LLM strategy.

### Outputs

- **`conversation_history`**: *List[Dict]*  
  A list of dictionaries containing the history of messages exchanged during task execution.

- **`tool_records`**: *List[Dict]*  
  Logs the use of tools during task execution, such as the GitHub CLI.

- **`request_tokens`**: *int*  
  Number of tokens used in the request interaction with the LLM.

- **`response_tokens`**: *int*  
  Number of tokens used in the response from the LLM.

### Usage
To use `GitHubAgent`, instantiate with the required inputs and call `run()` to perform specified GitHub tasks. It is ideally suited for automating GitHub interactions based on language-based tasks and requires appropriate configuration of API keys and tokens.

---

## typed.py

### Description
Defines input and output structures using `TypedDict`, ensuring that inputs and outputs are type-checked for consistency and reliability.

### Inputs

- **`base_path`**: *str*  
  Default filesystem path for relative operations.

- **`prompt_value`**: *Dict[str, Any]*  
  Dictionary storing values relevant to the user prompt.

- **`system_prompt`**: *str*  
  Defines the overarching context or instructions for the system.

- **`user_prompt`**: *str*  
  Specific prompt for user tasks, guiding the GitHub operations.

- **`max_llm_calls`**: *int*  
  Maximum allowable calls to the LLM service.

- **API Keys**: *str*  
  Includes `openai_api_key`, `anthropic_api_key`, `google_api_key`, required for LLM interactions.

### Outputs

- **`conversation_history`**  
  Detailed history of message exchanges during task execution.

- **`tool_records`**  
  Record of tools utilized, particularly during CLI interactions.

- **`request_tokens` / `response_tokens`**  
  Provides token usage metrics which can be useful for cost and performance analysis.

---

## __init__.py

### Description
The `__init__.py` file serves to mark the directory as a Python package. It does not currently contain any logic or imports for module initialization. 

---

This module is mainly useful for development environments where automated interaction with GitHub repositories is beneficial, especially when tasks need to be performed through structured natural language prompts.
