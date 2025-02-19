# AgenticLLM Module Documentation

This module comprises the `AgenticLLM` functionality, intended to manage interactions with Large Language Models (LLM) using a strategic approach. The code is structured across multiple files to handle inputs, outputs, and the core logic for executing tasks related to LLM.

## Overview
The `AgenticLLM` module provides a systematic interface to set up and execute conversations with LLMs using a pre-defined agent strategy. This is useful for applications that require a robust interaction setup with multiple calls to the LLM and for maintaining a structured conversation history and tool usage record.

## Files and Their Roles

### 1. `__init__.py`
- **Purpose**: This file is essentially empty and serves as an initializer for the package/folder. It allows the other scripts in this directory to be treated as part of a package.
- **Usage**: Not directly used by developers but necessary for Python to recognize the directory as a package.

### 2. `typed.py`
- **Purpose**: Defines the input and output types for the `AgenticLLM` class.
- **Inputs**:
  - `base_path`: The base directory path for tool configuration.
  - `prompt_value`: Dictionary containing input values for the prompts.
  - `system_prompt`: The template for the system prompt string.
  - `user_prompt`: The template for the user prompt string.
  - `max_llm_calls`: Configuration for the maximum number of LLM calls allowed.
  - API Keys like `openai_api_key`, `anthropic_api_key`, `patched_api_key`, and `google_api_key`.
- **Outputs**:
  - `conversation_history`: List of dictionaries capturing the conversation’s historical data.
  - `tool_records`: List of dictionaries recording the tools used during interactions.

### 3. `AgenticLLM.py`
- **Purpose**: Implements the main logic for handling LLM interactions using an agentic strategy.
- **Class**: `AgenticLLM`, which inherits from `Step`.
- **Core Methods**:
  - `__init__(self, inputs)`: Initializes the class with inputs, sets up the base path, conversation limit, and initializes the agentic strategy with LLM client and tools.
  - `run(self)`: Executes the agentic strategy, permits a specified number of LLM interaction calls, and returns conversation history and tool usage records.

## Usage
The `AgenticLLM` class is primarily utilized where systematic and strategic interactions with LLMs are needed. It is designed to facilitate easy tool integration and manages the logistics of multiple LLM calls, making it ideal for advanced conversational AI applications. Users must provide necessary API keys and configuration through the inputs setup, and the class will handle conversation management and tool coordination internally.

### Key Considerations
- Ensure valid API keys are provided for different LLM services.
- Configure the base path and prompts correctly to align with the desired interaction setup.
- The class should be instantiated with careful consideration of the maximum number of LLM calls to avoid exceeding resource limits.
