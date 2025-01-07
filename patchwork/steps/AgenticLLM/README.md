# AgenticLLM Module Documentation

## Overview

The `AgenticLLM` module is part of the `patchwork` library designed to utilize an agent-based strategy for interacting with large language models (LLMs). This module facilitates the management of conversations with LLMs and tracking tool interactions within a conversation context. It uses configurations and API keys to initialize different types of LLM clients.

## Components

### 1. `typed.py`

This file defines the data structure for inputs and outputs of the AgenticLLM module using Python's `TypedDict` and annotations.

#### Inputs

- **base_path**: `str`, optional - The base directory path for toolset.
- **prompt_value**: `Dict[str, Any]` - A dictionary containing key-value pairs for prompt data.
- **system_prompt**: `str` - A template string for system-generated prompts.
- **user_prompt**: `str` - A template string for user-generated prompts.
- **max_llm_calls**: `int` - Maximum number of call limit to LLMs, configurable.
- **openai_api_key**: `str` - API key for accessing OpenAI services.
- **anthropic_api_key**: `str` - API key for accessing Anthropic services.
- **patched_api_key**: `str` - A general API key for patched models, with fallback options.
- **google_api_key**: `str` - API key for accessing Google's LLM services.

#### Outputs

- **conversation_history**: `List[Dict]` - A list tracking the history of conversations.
- **tool_records**: `List[Dict]` - A list recording tool interactions.
- *(commented out unused fields)*
  - **request_tokens**: `int`
  - **response_tokens**: `int`

### 2. `AgenticLLM.py`

Implements the core functionality of the AgenticLLM object that inherits from the `Step` class.

#### Usage

The `AgenticLLM` class, through its constructor, initializes:
  - `AgenticStrategy` with an asynchronous LLM client and a tool set.
  - LLM conversation limits set through input configurations.

#### Method

- **`run()`**: Executes the agent strategy and returns a dictionary containing:
  - **conversation_history**: List of conversation stages.
  - **tool_records**: List of tool interactions carried out within the conversation.

### 3. `__init__.py`

This file is a placeholder to denote that the directory is a Python package. It doesn't contain any functional code.

## Intended Usage

The AgenticLLM module is intended for developers who need to integrate conversation-driven interactions with LLMs into their applications. By providing configurable input parameters such as API keys and prompt templates, it allows for adaptable usage across different contexts requiring LLM processing and agent strategies.

**Note**: Ensure all required API keys are set properly and paths are correctly configured for the tools and strategy to function optimally.
