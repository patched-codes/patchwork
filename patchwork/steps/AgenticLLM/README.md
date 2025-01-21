# AgenticLLM Documentation

## Overview
The `AgenticLLM` module is a component of a larger system designed to interact with Language Learning Models (LLMs) in a smart and flexible way, employing an agentic strategy. It defines input and output types, and includes logic to initialize and run LLM processing steps.

## Key Files
- `typed.py`
- `AgenticLLM.py`
- `__init__.py`

### 1. `typed.py`

#### Purpose
Defines the input and output data structures for the `AgenticLLM` class using `TypedDict`, which ensures type checking and clear structure for data being processed.

#### Inputs
- `base_path`: Path to the base directory where tools and configurations are located.
- `prompt_value`: A dictionary of prompt-related data for the LLM.
- `system_prompt`: A template string for system-level prompts.
- `user_prompt`: A template string for user-level prompts.
- `max_llm_calls`: Maximum number of LLM API calls, with configuration.
- `openai_api_key`, `anthropic_api_key`, `patched_api_key`, `google_api_key`: API keys for various LLM services, configured using `StepTypeConfig`.

#### Outputs
- `conversation_history`: A list of dictionaries containing the history of conversations.
- `tool_records`: A list of dictionaries containing records from any tools used during processing.

### 2. `AgenticLLM.py`

#### Purpose
Implements the `AgenticLLM` class, which serves as a step in a processing pipeline. This class handles the logic for managing conversation limits, initializing strategies, and executing strategies.

#### Usage
- **Initialization**: Sets up the LLM environment, paths, and configurational parameters using provided `AgenticLLMInputs`.
- **Execution**: Calls `execute()` on the `AgenticStrategy` object to process data using LLM with a defined conversation limit.
- **Returns**: Results in the form of conversation history and tool records encapsulated in a dictionary form.

### 3. `__init__.py`

#### Purpose
This file acts as a module initializer for the `AgenticLLM` package, though currently contains no code.

## Summary

The `AgenticLLM` module is designed to efficiently utilize language models within a larger processing system through a structured approach to inputs and outputs. The primary class, `AgenticLLM`, manages the input parameters, initializes strategy instances, and executes LLM operations by interfacing with multiple possible APIs. Through this approach, developers can implement sophisticated conversational agents within their applications.
