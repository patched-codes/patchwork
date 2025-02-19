# AgenticLLM Module Documentation

This documentation provides an overview of the `AgenticLLM` module found in the `patchwork/steps/AgenticLLM` directory. The module encompasses multiple files, including `__init__.py`, `typed.py`, and `AgenticLLM.py`. The module is designed to handle Long Language Model (LLM) interactions, potentially useful for dialogue systems requiring multiple tool integrations and conversation handling.

## Files Overview

### 1. `__init__.py`

- **Purpose:** This file initializes the module. It is currently empty, but it typically serves as the entry point for module initialization and can be used to import necessary submodules or components.

### 2. `typed.py`

- **Purpose:** Defines input and output types for the `AgenticLLM` class, using Python's `TypedDict` and `Annotated` types for more structured data handling.
- **Key Components:**
  - **`AgenticLLMInputs`**: Specifies possible configurations for API keys, user prompt settings, and limits on LLM calls.
  - **`AgenticLLMOutputs`**: Defines the structure of the output data, including conversation history and tool records.

#### Inputs

- `base_path`: Base directory for tools.
- `prompt_value`, `system_prompt`, `user_prompt`: Prompt configurations utilized in the dialogue generation.
- `max_llm_calls`: Maximum number of LLM calls that can be made.
- Various API keys such as `openai_api_key`, `anthropic_api_key`, `patched_api_key`, and `google_api_key`.

#### Outputs

- `conversation_history`: A list of dictionaries capturing conversation exchanges.
- `tool_records`: Records of tool interactions.

### 3. `AgenticLLM.py`

- **Purpose:** Implements the `AgenticLLM` class which orchestrates the use of LLM for dialogue management integrated with different tools.
- **Key Components:**
  - **Class `AgenticLLM`:** Inherits from `Step` and uses input and output classes for structured data flow.
  - **Constructor (`__init__`):** Initializes the class with input data, configures tool sets, and sets up the conversation strategy.
  - **Method `run`:** Executes the agentic strategy and captures the dialogue and tool interaction history.

#### How to Use

1. **Initialization:** Create an `AgenticLLM` instance by providing a dictionary matching the structure of `AgenticLLMInputs`.
2. **Running:** Call the `run` method to execute the LLM conversation strategy and generate outputs defined in `AgenticLLMOutputs`.

## Usage Example

Here is a hypothetical example of how one might initialize and run the `AgenticLLM` implementation:

```python
inputs = {
    'base_path': '/path/to/tools',
    'prompt_value': {...},
    'system_prompt': 'Your system prompt here.',
    'user_prompt': 'Your user prompt here.',
    'max_llm_calls': 10,
    'openai_api_key': 'your_openai_api_key',
    # Other api keys if needed
}

agentic_llm = AgenticLLM(inputs)
results = agentic_llm.run()

print(results['conversation_history'])
print(results['tool_records'])
```

This example sets up the module with a specific configuration and executes a dialogue session, returning the conversation history and tool interaction records.
