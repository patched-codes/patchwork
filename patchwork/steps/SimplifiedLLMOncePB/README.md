# Documentation for SimplifiedLLMOncePB Module

## Overview

This module defines the `SimplifiedLLMOncePB` class, which interoperates with various LLM (Large Language Model) APIs by supporting multiple API keys and manages the construction and execution of a prompt from user inputs.

## Files

### [typed.py](#file-typed.py)
### [__init__.py](#file-__init__.py)
### [SimplifiedLLMOncePB.py](#file-SimplifiedLLMOncePB.py)

## File: typed.py

This file defines the input data structure for the `SimplifiedLLMOncePB` class using `TypedDict` from the `typing_extensions`. It specifies required and optional input fields along with their respective type annotations and configurations.

### Inputs
- **json_schema** (`Dict[str, Any]`): JSON schema definition, marked as required.
- **user_prompt** (`str`): User's input prompt, marked as required.
- **prompt_value** (`Dict[str, Any]`): Dynamic values to populate the user prompt, marked as required.
- **system_prompt** (`str`, optional): Predefined system prompt.
- **model** (`str`): Model selection.
- **openai_api_key** (`str`): OpenAI API key.
- **anthropic_api_key** (`str`): Anthropic API key.
- **patched_api_key** (`str`): Patched API key.
- **google_api_key** (`str`): Google API key.

### Outputs
- The `TypedDict` does not produce direct outputs but is used as a schema for validating and configuring class inputs.

## File: __init__.py

This is an empty file that initializes the `SimplifiedLLMOncePB` module.

### Code
```python

```

## File: SimplifiedLLMOncePB.py

This file defines the main logic for the `SimplifiedLLMOncePB` class, inheriting from the `Step` class.

### Class Definition

```python
class SimplifiedLLMOncePB(Step, input_class=SimplifiedLLMOncePBInputs):
```

### Inputs
The class accepts an `inputs` dictionary aligning with `SimplifiedLLMOncePBInputs` schema, containing fields like `user_prompt`, `system_prompt`, and various API keys.

### Initialization
- **__init__(self, inputs)**: Constructor initializes class variables from `inputs`.

### Main Method
- **run(self) -> dict**: Executes the LLM call based on user inputs and system prompts.
    - Constructs a prompt dictionary.
    - Instantiates and runs the `SimplifiedLLM` class.
    - Returns a consolidated response including extracted responses and token details.

### Outputs
Returns a dictionary containing:
- **extracted_responses**: The processed output from the LLM.
- **request_tokens**: Token usage in request.
- **response_tokens**: Token usage in response.

### Example Usage

```python
inputs = {
    "json_schema": {...},
    "user_prompt": "Explain the concept of AI",
    "prompt_value": {"example_key": "example_value"},
    "openai_api_key": "your-openai-api-key"
}

llm_step = SimplifiedLLMOncePB(inputs)
result = llm_step.run()
print(result)
```

### Note
This class ensures compatibility with multiple API keys and prompts users to generate appropriate keys if needed.

By following this documentation, you should be able to understand the structure, configuration, and usage of the `SimplifiedLLMOncePB` class effectively.