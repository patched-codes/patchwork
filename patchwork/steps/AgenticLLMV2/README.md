# AgenticLLMV2 Module Documentation

## Overview
The `AgenticLLMV2` module provides a step for executing a multi-turn conversation strategy using the `AgenticStrategyV2` framework. This is part of a system that involves complex conversational models and tool integrations. The module is composed of three scripts: an initializer, the main class implementation, and type definitions for controlled inputs and outputs.

## Components

### 1. AgenticLLMV2/__init__.py
This script is an initializer for the `AgenticLLMV2` module. It currently contains no code but serves to correctly package the Python files in this directory.

### 2. AgenticLLMV2/AgenticLLMV2.py

#### Description
This file implements the `AgenticLLMV2` class, which extends the `Step` class and is responsible for managing the setup and execution of an `AgenticStrategyV2` conversation process.

#### Inputs

- `base_path` (str): The base path for tool configurations. Defaults to the current working directory if not specified.
- `prompt_value` (Dict[str, Any]): Template data used in the prompts.
- `system_prompt` (str): The system prompt used if not overridden.
- `user_prompt` (str): Prompt provided for user-specific queries.
- `max_agent_calls` (int): Maximum number of turns for agent calls. Defaults to 1.
- `anthropic_api_key` (str): API key for Anthropic.
- `agent_system_prompt` (str): Custom system prompt for agents.
- `example_json` (str): JSON format data for prompt examples.

#### Outputs

- `request_tokens` (int): The number of tokens in the request.
- `response_tokens` (int): The number of tokens in the response.

#### Usage
To use the `AgenticLLMV2` class, instantiate it with `AgenticLLMV2Inputs`, then call the `run()` method to perform the conversation operations. It integrates tools found at the specified base path and supports a configurable number of conversation turns.

### 3. AgenticLLMV2/typed.py

#### Description
This script defines the data types used for input and output of the `AgenticLLMV2` class using Python's `TypedDict` for structured data handling.

#### Inputs
- Inputs are defined in `AgenticLLMV2Inputs` which includes optional attributes such as `base_path`, `prompt_value`, and more, facilitating flexible configuration of the agent strategy.

#### Outputs
- Outputs are defined in `AgenticLLMV2Outputs`, ensuring that only request and response token counts are recorded as outputs.

## How to Use
1. Define input parameters using `AgenticLLMV2Inputs`.
2. Initialize the `AgenticLLMV2` class with these inputs.
3. Execute the `run()` method to process a conversation based on the configured strategy.
4. Analyze the token usage from the outputs to understand usage and billing metrics if needed.

This module is useful for developers working on advanced AI conversational systems, offering customization and detailed control over conversation flows and tools used within those flows.
