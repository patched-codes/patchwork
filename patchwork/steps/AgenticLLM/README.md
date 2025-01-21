# Documentation for `AgenticLLM` Module

## Overview

This module is part of a larger framework, implementing a step in a conversational agent's workflow. The `AgenticLLM` class is responsible for managing interactions with an external language model API using predefined prompts and strategies.

## Contents

- `type.py`
- `AgenticLLM.py`
- `__init__.py`

## File: `typed.py`

This file defines structured inputs and outputs for the module using Python's `TypedDict`. It facilitates type checking and outlines the configuration options available for the `AgenticLLM` step.

### Inputs

The `AgenticLLMInputs` dictionary includes the following keys:

- `base_path`: `str` - The base directory path for accessing tools.
- `prompt_value`: `Dict[str, Any]` - Data for prompt construction.
- `system_prompt`: `str` - Template for the system prompt.
- `user_prompt`: `str` - Template for the user prompt.
- `max_llm_calls`: `int` - Maximum number of language model calls (configurable).
- `openai_api_key`, `anthropic_api_key`, `patched_api_key`, `google_api_key`: `str` - API keys required for accessing different LLM services. The keys have flexible configurations to allow one of several options.

### Outputs

The `AgenticLLMOutputs` dictionary contains:

- `conversation_history`: `List[Dict]` - A record of the conversation between the agent and LLM.
- `tool_records`: `List[Dict]` - A log of the tools used during the `AgenticLLM` operations.

## File: `AgenticLLM.py`

This file implements the `AgenticLLM` class, extending the `Step` class from the framework. The main functionality involves configuring a conversational strategy and executing LLM interactions.

### Key Components

- **Constructor (`__init__`)**: Initializes the `AgenticStrategy` by creating an asynchronous LLM client and loads the relevant tools using provided inputs.
- **Method (`run`)**: Executes the agentic strategy, handling the conversation logic and tool management. Returns a result dictionary with conversation history and tools used.

## File: `__init__.py`

This file is empty, serving primarily as a marker for the Python package structure, indicating the directory `patchwork/steps/AgenticLLM` can be treated as a module.

## Usage

The module is designed to be part of a larger conversational system, allowing for dynamic interactions with language models using custom prompts and tools. The configuration flexibility for the API keys helps accommodate various operational environments and API endpoints.
