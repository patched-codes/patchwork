# AgenticLLM

The `AgenticLLM` class is designed to implement an agentic strategy using a Language Model (LLM). It uses a client setup for asynchronous communication and employs various tools and strategies to handle user prompts and execute predefined conversations. This documentation provides an overview of the implementation, inputs, and outputs of the `AgenticLLM` class and related components.

## Overview

The `AgenticLLM` is a step-based component that applies agentic strategies to handle multi-turn conversations with an LLM. The strategy involves using an LLM client, a set of tools, and predefined templates to execute conversation limits effectively. It integrates with different API keys supporting multiple AI service providers, ensuring flexibility in deployment.

## Components

### Files

- **AgenticLLM.py**: Contains the main `AgenticLLM` class definition and its `run` method.
- **typed.py**: Defines `AgenticLLMInputs` and `AgenticLLMOutputs` using TypedDict to specify structured inputs and outputs for the `AgenticLLM` component.
- **__init__.py**: Empty file typically used to signal that its directory is a Python package.

## `AgenticLLM` Class

### Inputs

- **base_path** `(str)`: Defines the base path for toolset configurations, with a default to the current working directory.
- **prompt_value** `(Dict[str, Any])`: Contains the data to be used in prompts for the LLM.
- **system_prompt** `(str)`: Template string for system prompts.
- **user_prompt** `(str)`: Template string for user prompts.
- **max_llm_calls** `(int)`: Configures the maximum number of LLM calls; effectively limits the conversation rounds.
- **openai_api_key**, **anthropic_api_key**, **patched_api_key**, **google_api_key** `(str)`: API keys for different AI service providers, with checks ensuring at least one valid key is provided.

### Outputs

- **conversation_history** `(List[Dict])`: Captures the history of the conversation executed by the agentic strategy.
- **tool_records** `(List[Dict])`: Maintains records of tools used during the execution.

## Methods

### `__init__(self, inputs)`

- Initializes the `AgenticLLM` instance with provided inputs, setting up the agentic strategy with the LLM client and tools.

### `run(self) -> dict`

- Executes the agentic strategy up to a specified limit and returns the conversation history and tool records.

## Usage

Anyone implementing the `AgenticLLM` class would typically be looking to handle sophisticated, multi-turn interactions with an LLM using pre-configured prompts and tools. The ability to define structured inputs and outputs allows seamless integration into a larger AI system or workflow that might require interacting with a language model efficiently. Suitable API keys need to be provided for execution. The focus on strategy execution and tool utilization makes this component apt for applications in customer support, virtual assisting, or other automated dialogue systems where maintaining an intelligent conversation flow is crucial.
