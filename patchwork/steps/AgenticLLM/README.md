# Documentation for AgenticLLM Module

## Overview

The `AgenticLLM` module consists of several Python files that define typed dictionaries and classes to support communication with large language models (LLMs) using an agentic strategy. It facilitates executing multi-turn, dialogue-like interactions with LLMs and maintaining a conversation history. 

### Files

1. **`typed.py`** - Defines input and output types for the `AgenticLLM` class.
2. **`AgenticLLM.py`** - Implements the core functionality of the `AgenticLLM` class using these types.
3. **`__init__.py`** - A placeholder file for the module initialization.

## File: `typed.py`

### Description

This file defines two primary data structures used within the AgenticLLM module—`AgenticLLMInputs` and `AgenticLLMOutputs`, which are TypedDicts used to specify required and optional input/output parameters for the `AgenticLLM` class.

### Inputs

- **prompt_value**: A dictionary that includes various data inputs to be passed as prompts.
- **system_prompt**: A string containing the template for the system-level prompt.
- **user_prompt**: A string containing the template for the user-level prompt.
- **max_llm_calls**: An integer specifying the maximum number of LLM calls allowed.
- **model_args, client_args**: Strings used to pass configuration arguments for the model and client.
- **openai_api_key, anthropic_api_key, patched_api_key, google_api_key**: Strings that hold various API keys for authentication with different LLM providers.

### Outputs

- **conversation_history**: A list of dictionaries detailing the past interactions in the conversation.
- **tool_records**: A list of dictionaries logging the details of the tools used along with each interaction.

## File: `AgenticLLM.py`

### Description

This file implements the `AgenticLLM` class, a step that automates interactions with LLMs by applying an agentic multi-turn strategy. 

### Usage

1. **Initialization**: The class is initialized with the parameters defined in `AgenticLLMInputs`.

2. **Execution**: The `run` method engages the `AgenticStrategy` to handle the execution of the multi-turn interaction, recording both conversation history and tool usage.

### Inputs

The inputs utilized within the class include:

- **AgenticLLMInputs**: As defined in `typed.py`, these inputs are used for setting initial conditions like prompt values and API keys.

### Outputs

The method `run` returns an object structured similarly to `AgenticLLMOutputs`, consisting of:

- **conversation_history**: Retrieved from the `AgenticStrategy` after execution.
- **tool_records**: Logged during execution by `AgenticStrategy`.

## File: `__init__.py`

### Description

An empty initializer file for the `AgenticLLM` module.

---

These files collectively provide a foundation for integrating tool-based, agentic interactions with LLMs into Python applications, offering structured input and output handling, along with API key management. The module is useful in applications involving multi-turn dialogues where interactions with LLMs are mediated by external tools to improve the effectiveness of communication.
