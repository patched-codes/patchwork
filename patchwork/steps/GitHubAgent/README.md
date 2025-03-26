# GitHubAgent Module Documentation

This documentation provides an overview of the `GitHubAgent` module, detailing the components and functionality for using the `GitHubAgent` to interact with GitHub via the CLI, leveraging a strategy-based approach with AI models.

## Overview

The `GitHubAgent` module is designed to abstract tasks involving interactions with GitHub. By using an agentic strategy, it interfaces with the GitHub CLI and handles various user-defined tasks. This module can be particularly useful for developers and project managers who need to automate or script interactions with GitHub repositories.

### Main Features

- Utilizes the `AgenticStrategyV2` for task execution.
- Employs AI models such as `claude-3-5-sonnet-latest` and `gemini-2.0-flash`.
- Integrates with GitHub CLI via `GitHubTool`.
- Customizable input and output classes for flexible task execution.

## Files

### GitHubAgent.py

#### Inputs

- **base_path (str)**: The base path for GitHub CLI operations, defaults to the current working directory.
- **prompt_value (dict)**: Dictionary containing additional data for task rendering.
- **task (str)**: A string template for tasks to be executed.
- **max_llm_calls (int)**: Maximum number of LLM (Language Model) calls permissible.
- **openai_api_key (str)**: API key for OpenAI resources.
- **anthropic_api_key (str)**: API key for Anthropic resources.
- **google_api_key (str)**: API key for Google resources.
- **client_is_gcp (str)**: Flag indicating if the client is Google Cloud Platform.

#### Outputs

- **request_tokens (int)**: Number of tokens used in the request.
- **response_tokens (int)**: Number of tokens used in the response.

#### Usage

The `GitHubAgent` class is instantiated with `GitHubAgentInputs`, which are then used to set up the agentic strategy, incorporating various tasks and models. The `run()` method executes the strategy and returns a dictionary combining execution results and usage statistics.

### typed.py

This file defines the input and output data structures for the `GitHubAgent`. The use of `TypedDict` and `Annotated` supports type checking and annotating configuration-specific parameters.

#### Structures

- **GitHubAgentInputs**: A typed dictionary that extends required inputs with optional configurations.
- **GitHubAgentOutputs**: A typed dictionary indicating the structure of the output data.

### __init__.py

The `__init__.py` file serves as a placeholder for initializing the module, conforming to Python package requirements. It currently does not include additional logic or code.
