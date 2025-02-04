# AgenticLLM Documentation

## Overview

The `AgenticLLM` module is designed to execute a generic agent-like strategy using Large Language Models (LLM). It provides features to interact with an LLM in a multi-turn conversational setup, utilizing additional tools to enhance the capabilities of the LLM. This module is likely used in situations where a complex, context-aware dialogue is needed, potentially with the execution of certain actions based on the conversation flow.

## File Structure

- **AgenticLLM.py**: Contains the main logic and implementation of the `AgenticLLM` class.
- **typed.py**: Contains type definitions for inputs and outputs used by the `AgenticLLM` class.
- **__init__.py**: Empty initialization file for the package.

## `AgenticLLM.py`

### Inputs

The inputs for the `AgenticLLM` class are encapsulated in the `AgenticLLMInputs` dictionary. Here's a breakdown of the expected input parameters:

- **base_path (str):** Path to the tools. Defaults to the current working directory.
- **prompt_value (Dict[str, Any]):** Provides data for the prompt used by the LLM.
- **system_prompt (str):** Template for the system prompt.
- **user_prompt (str):** Template for the user prompt.
- **max_llm_calls (int):** Maximum number of calls that can be made to the LLM. This is used to control the conversation limit.
- **API Keys (str):** Tokens for OpenAI, Anthropics, Patched, and Google LLM services.

### Outputs

The outputs from executing the `AgenticLLM` class are encapsulated in the `AgenticLLMOutputs` dictionary:

- **conversation_history (List[Dict]):** A record of the conversation history.
- **tool_records (List[Dict]):** Log of actions and tool usage throughout the conversation.

### Class Usage

- **Initialization:** Create an instance of `AgenticLLM` with the required inputs.
- **Execution:** Call the `run()` method to execute the agentic strategy and interact with the LLM.
- **Output Retrieval:** Access conversation history and tool records from the returned dictionary.

## `typed.py`

### Type Definitions

- **AgenticLLMInputs (TypedDict):** A dictionary that defines the structure and types of the inputs expected by `AgenticLLM`.
- **AgenticLLMOutputs (TypedDict):** A dictionary defining the types of outputs produced after the execution.

## Usage Example

```python
from patchwork.steps.AgenticLLM.AgenticLLM import AgenticLLM, AgenticLLMInputs

# Define your inputs
inputs = AgenticLLMInputs(
    base_path="your/tool/path",
    prompt_value={"key1": "value1", "key2": "value2"},
    system_prompt="This is a system prompt",
    user_prompt="This is a user prompt",
    max_llm_calls=10,
    openai_api_key="your_openai_api_key"
)

# Initialize the class and execute
agentic_llm = AgenticLLM(inputs)
output = agentic_llm.run()

# Access results
conversation_history = output['conversation_history']
tool_records = output['tool_records']
```

This example sets up the `AgenticLLM` with custom prompt configurations, API keys, and executes a conversation strategy, retrieving the history and tool usage as output.

## Conclusion

The `AgenticLLM` module provides configurable multi-turn conversational capabilities with the use of LLMs, integrating a toolkit for expanded functionalities. Its design facilitates the creation of automated conversation agents which can interact in dynamic and context-aware environments.
