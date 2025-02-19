# Documentation for AgenticLLM Module

This module provides a structured approach to define, configure, and execute an "Agentic" Large Language Model (LLM) step in a programmatic pipeline. It integrates with various LLM services to perform tasks based on provided prompts and strategies.

## Files Overview

### 1. `__init__.py`

- **Extension:** .py
- **Purpose:** Marks the directory as a Python package. The file is empty, indicating no specific initialization functions or variables are defined at the package level.

### 2. `typed.py`

- **Extension:** .py
- **Purpose:** Defines the input and output data structures for the AgenticLLM step using Python's type hinting. These are critical for ensuring data consistency and integrity when interacting with LLM APIs.

#### Inputs

- **`base_path`**: The base directory path for tools and resources.
- **`prompt_value`**: A dictionary containing prompting data.
- **`system_prompt`**: A string for the system-generated prompt.
- **`user_prompt`**: A string for the user-generated prompt.
- **`max_llm_calls`**: Integer annotation, indicating the configurable limit of LLM calls.
- **API Keys**:
  - **`openai_api_key`**: API Key for OpenAI.
  - **`anthropic_api_key`**: API Key for Anthropic APIs.
  - **`patched_api_key`**: API Key setup instruction provided.
  - **`google_api_key`**: API Key for Google.

#### Outputs

- **`conversation_history`**: List documenting the exchange history.
- **`tool_records`**: List documenting the usage of tools throughout the conversation.

### 3. `AgenticLLM.py`

- **Extension:** .py
- **Purpose:** Implements the `AgenticLLM` class, inheriting from `Step`, responsible for controlling the interaction with the LLM services using an agentic strategy.

#### Class: `AgenticLLM`

**Constructor**

- Instantiates an agentic strategy using the provided inputs, including prompts and API keys.
- Calculates conversation limits and configures the tool set available to the agentic strategy.

**Method: `run()`**

- Executes the agentic strategy up to the predefined limit and returns the updated conversation and tool usage history. 

## Usage

The `AgenticLLM` module provides a method to interact with multiple LLM services using a structured, prompt-driven approach. It is ideal for scenarios requiring iterative conversations, where the history of interactions is crucial. Users can configure the module with API keys and prompts to tailor the interaction to specific requirements. The setup ensures flexibility and extensibility across various LLM services.
