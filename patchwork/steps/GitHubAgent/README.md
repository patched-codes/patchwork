# GitHubAgent Module

This module defines the `GitHubAgent` class, which is designed to interact with GitHub using the GitHub CLI through a provided task prompt. It's part of a larger framework and employs an agentic strategy to fulfill a specified task, utilizing large language models (LLMs) for assistance.

## Modules and Files

### GitHubAgent.py

This is the primary file containing the `GitHubAgent` class, which leverages a multi-turn strategy for performing tasks using GitHub's CLI.

#### Inputs

- **base_path** `(str)`: Directory path where operations are based. Defaults to the current directory if not specified.
- **task** `(str)`: The task to be performed using the GitHub CLI.
- **prompt_value** `(dict)`: Data to be substituted in the task string using a mustache template.
- **max_llm_calls** `(int)`: Configuration for the maximum number of calls allowed to the LLM.
- **openai_api_key** `(str)`: API key for interacting with OpenAI services, interchangeable with other API keys.
- **anthropic_api_key** `(str)`: API key for Anthropic interaction.
- **google_api_key** `(str)`: API key for Google services.

#### Outputs

- **conversation_history** `(list)`: A list of dictionaries capturing the interaction history during task execution.
- **tool_records** `(list)`: A list of dictionaries detailing the use of tools involved in completing the task.
- **request_tokens** `(int)`: Number of tokens used in requests to the language model.
- **response_tokens** `(int)`: Number of tokens in the responses received.

#### Usage

To use this class, instantiate it with `GitHubAgentInputs` and execute its `run` method to perform the specified GitHub task. 

### typed.py

This script defines type annotations for input and output data structures used by the `GitHubAgent`.

### __init__.py

This file exists to make the folder a Python package; it currently does not contain any code beyond the obligatory presence to enable import functionality.

---

Together, these components enable the execution of GitHub-related tasks by issuing commands through a templated prompt strategy, primarily intended for developers automating or managing GitHub repositories programmatically.
