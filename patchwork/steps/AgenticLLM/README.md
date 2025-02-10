# `AgenticLLM` Module Documentation

## Overview

The `AgenticLLM` module is a step in a system designed to facilitate conversations with language models using agentic strategies. It integrates with various language model clients and executes a strategy involving multiple prompts. This module is part of a larger system that likely involves multiple steps, each handling different parts of the interaction with language models or tools.

## Files

### 1. `AgenticLLM.py`

This file contains the core implementation of the `AgenticLLM` class, which is responsible for:

- Initializing and configuring the agentic strategy based on provided inputs.
- Executing the language model strategy with a specified conversation limit.
- Returning the history of the conversation and records of the tools used.

#### Inputs

The class expects an input dictionary compatible with the `AgenticLLMInputs` type, which includes:

- `base_path` (str): Base directory path for tools.
- `prompt_value` (Dict): Template data for creating prompts.
- `system_prompt` (str): Template for system prompts.
- `user_prompt` (str): Template for user prompts.
- `max_llm_calls` (int): Limits the number of language model calls.
- API keys like `openai_api_key`, `anthropic_api_key`, `patched_api_key`, `google_api_key` for authorization with different language models.

#### Outputs

- `conversation_history` (List[Dict]): Logs of the conversation that took place.
- `tool_records` (List[Dict]): Details of tool interactions during execution.

### 2. `__init__.py`

This file is a package initializer script. Currently, it does not contain any code but is used to define the `AgenticLLM` as a package.

### 3. `typed.py`

Defines typed dictionaries for input and output configuration, enforcing structured data throughout the interfaces in this module.

#### `AgenticLLMInputs`

- Ensures proper input types and validation for configuration keys.
- Supports comprehensive API key configurations to ensure connection to the appropriate model service.

#### `AgenticLLMOutputs`

- Defines the expected output structure from the `AgenticLLM` operation, aiding in processing downstream or debugging.

## Usage

1. **Initialization**: To use the `AgenticLLM` class, instantiate it with a set of inputs conforming to `AgenticLLMInputs`.
2. **Execution**: Call the `run()` method to execute the conversation. This method employs the configured agentic strategy to interact with the language model.
3. **Output Handling**: The result of the `run()` method includes conversation history and tool interaction records, which can be used for logging, user feedback, or further analysis.

This module is ideal for developers integrating language model interactions where structured and strategized prompt usage is required, particularly in scenarios involving multiple external tools or services.
