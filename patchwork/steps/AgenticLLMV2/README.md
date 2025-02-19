# Documentation for AgenticLLMV2 Package

This documentation provides an overview of the `AgenticLLMV2` package, detailing its components, the input it receives, and the output it produces. This package is likely used to facilitate conversational AI strategies using an agentic approach.

## Overview

The `AgenticLLMV2` module is a Python implementation designed to manage agentic strategies in multi-turn conversational AI applications. It integrates with various tools and configurations to execute defined strategies with enhanced flexibility and control. 

The key component of this module is the `AgenticLLMV2` class, which inherits from `Step` and is responsible for orchestrating the conversational strategy using inputs and configurations provided by the user.

---

## Input

### `AgenticLLMV2Inputs`

The inputs are designated in the `AgenticLLMV2Inputs` class, which is a `TypedDict` encapsulating the necessary parameters:

- **base_path**: `str`
  - Optional path for tools configuration; defaults to current working directory if not provided.

- **prompt_value**: `Dict[str, Any]`
  - Dictionary containing key-value pairs for prompt customization.

- **system_prompt**: `str`
  - The initial system-wide prompt template to guide the conversation.

- **user_prompt**: `str`
  - Template for user-related input prompts in conversations.

- **max_agent_calls**: `int`
  - Maximum number of conversation rounds with the agent. Set via configuration using `StepTypeConfig`.

- **anthropic_api_key**: `str`
  - API key for accessing Anthropic services, crucial for agent operation.

- **agent_system_prompt**: `str`
  - System prompt specifically for the agent's context.

- **example_json**: `str`
  - JSON string containing examples for the agent to learn patterns or produce outputs.

---

## Outputs

### `AgenticLLMV2Outputs`

The output format is encapsulated in the `AgenticLLMV2Outputs` class, which currently does not specify any fields, indicating that all outputs are dynamic and context-dependent based on the agent's execution of the strategy.

---

## Usage

To utilize the `AgenticLLMV2` class, the user must supply the necessary inputs, particularly API keys, configuration paths, and relevant prompt templates. The `run()` method is the primary interface for executing the agentic strategy, which internally handles the execution limit and interaction with the `AgenticStrategyV2` class.

This setup is essential for developers looking to integrate complex, agent-based conversational systems into their applications, leveraging customizable prompts and strategy configurations to meet specific use cases. 

Overall, the `AgenticLLMV2` package provides a robust foundation for extending an application's conversational capabilities within a structured framework.
