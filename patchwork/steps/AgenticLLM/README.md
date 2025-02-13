# Documentation: AgenticLLM Module

This documentation provides an overview of the `AgenticLLM` module, focusing on its purpose, input requirements, and the output it generates. The module is part of a larger project, potentially designed for integrating language models (LLMs) with additional functionalities through various APIs.

## Files Overview

The `AgenticLLM` module consists of the following files:

1. `__init__.py`: Placeholder for Python package initialization.
2. `typed.py`: Defines the input and output types for the module.
3. `AgenticLLM.py`: Contains the main logic for the AgenticLLM class.

## File: `typed.py`

### Inputs

The `AgenticLLMInputs` class defines the input schema required for the `AgenticLLM` class:

- **base_path (str)**: The base directory path. Defaults to current working directory if not provided.
- **prompt_value (Dict[str, Any])**: Template data for generating prompts.
- **system_prompt (str)**: The template for a system prompt.
- **user_prompt (str)**: The template for a user prompt.
- **max_llm_calls (int)**: Maximum number of LLM calls allowed. Configurable through `StepTypeConfig`.
- **API Keys**: 
  - **openai_api_key (str)**
  - **anthropic_api_key (str)**
  - **patched_api_key (str)**
  - **google_api_key (str)**

  These keys are interchangeable, allowing flexibility in the API used.

### Outputs

The `AgenticLLMOutputs` class captures the output from the module:

- **conversation_history (List[Dict])**: A log of the conversation history with the LLM.
- **tool_records (List[Dict])**: Records of tools used during the execution.

## File: `AgenticLLM.py`

### Overview

The `AgenticLLM` class orchestrates interaction with Language Models using a specified strategy. It utilizes strategies, tools, and templates to execute multi-turn conversations with the LLM.

### Usage

#### Initialization

```python
agentic_llm = AgenticLLM(inputs)
```

- **inputs**: Dictionary conforming to `AgenticLLMInputs` schema, containing configuration data and API keys.

#### Execution

```python
output = agentic_llm.run()
```

- This method executes the defined strategy over the configured number of interactions, captures the conversation details, and any tools used.

### Implementation Details

- **AgenticStrategy**: Applies a predefined strategy for interacting with the LLM.
- **AioLlmClient**: Asynchronous client to manage LLM communications.
- **Tool**: Framework to integrate tools with specified functionalities, enhancing LLM capabilities.

## Conclusion

The `AgenticLLM` module provides a flexible and configurable interface for LLM interactions, designed to handle multi-turn conversations and tool integrations. By supporting multiple API configurations, it allows users to adapt to different environments and requirements seamlessly.
