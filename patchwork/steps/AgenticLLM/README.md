# Documentation for AgenticLLM Module

## Overview

The `AgenticLLM` module provides a step implementation within the Patchwork framework, designed to interact with a Language Learning Model (LLM) using an agentic strategy. It allows automated multi-turn conversations and decision-making processes aided by LLMs, employing various tools and templates to enhance interactions.

This module is composed of three primary files:
- `AgenticLLM.py` - Contains the main logic for the agentic strategy step.
- `__init__.py` - Present for package initialization.
- `typed.py` - Provides type annotations for inputs and outputs used by the `AgenticLLM`.

## File Details

### 1. AgenticLLM.py

#### Description

This file defines the `AgenticLLM` class, which extends the `Step` class. It initiates the necessary components such as the `AgenticStrategy` and executes LLM interactions based on specified conversation limits and templates.

#### Inputs

- **base_path** (str): Path for tool configurations. Defaults to the current working directory.
- **prompt_value** (Dict[str, Any]): Data to customize the conversation prompts.
- **system_prompt** (str): Template for system-generated prompts.
- **user_prompt** (str): Template for user-generated prompts.
- **max_llm_calls** (int): Maximum number of calls allowed to the LLM, divided by two to determine conversation limits.
- Credentials: API keys are required to interact with specific LLM services:
  - **openai_api_key** (str)
  - **anthropic_api_key** (str)
  - **patched_api_key** (str)
  - **google_api_key** (str)

#### Outputs

- **conversation_history** (List[Dict]): A list of dictionaries capturing each conversation turn.
- **tool_records** (List[Dict]): Logs of tool interactions during the conversation.

### 2. __init__.py

An empty file used for module initialization. It ensures that Python treats the directories as containing packages.

### 3. typed.py

#### Description

Contains type definitions using `TypedDict` from the `typing_extensions`. This provides structured types for `AgenticLLM` inputs and outputs to facilitate type checking and clarity in data handling.

#### AgenticLLMInputs and AgenticLLMOutputs

- **AgenticLLMInputs**: A dictionary of potential input parameters, including paths, prompts, API keys, and configurations.
- **AgenticLLMOutputs**: Defines the expected format of the output, mainly focusing on conversation history and tool interaction records.

## Usage

Developers implementing this module would typically:
1. Initialize the `AgenticLLM` class with input parameters.
2. Execute the `run()` method to perform the agentic LLM conversation strategy.
3. Retrieve outputs such as conversation history and tool records for further processing or analysis.

This module is ideal for use cases requiring advanced multi-turn LLM interactions with intricate prompting strategies and tool integrations.
