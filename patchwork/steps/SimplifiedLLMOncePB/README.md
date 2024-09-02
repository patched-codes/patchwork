# Documentation: SimplifiedLLMOncePB Module

## Overview
This module defines the `SimplifiedLLMOncePB` class, which is a step for interacting with a simplified large language model (LLM) once over the Patchwork framework. It also includes typed input definitions required for initializing the step and running it with user-specified prompts and model configurations.

## File: patchwork/steps/SimplifiedLLMOncePB/typed.py

### Imports
- Modules from `typing_extensions`
- Custom `StepTypeConfig` from `patchwork.common.utils.step_typing`
- `TOKEN_URL` from `patchwork.steps.CallLLM.CallLLM`

### Class Definitions
- `__SimplifiedLLMOncePBInputsRequired`: A typed dictionary specifying required inputs for the LLM, including `json_schema`, `user_prompt`, and `prompt_value`.
- `SimplifiedLLMOncePBInputs`: Extends `__SimplifiedLLMOncePBInputsRequired` and includes optional fields `system_prompt`, `model`, and several API keys (`openai_api_key`, `anthropic_api_key`, `patched_api_key`, `google_api_key`).

### Inputs
#### Required
- `json_schema`: A dictionary defining the JSON schema for expected LLM output.
- `user_prompt`: A string containing the user's prompt.
- `prompt_value`: A dictionary of values related to the prompt.

#### Optional
- `system_prompt`: A string containing an additional system prompt.
- `model`: A string specifying the model to use.
- `openai_api_key`, `anthropic_api_key`, `patched_api_key`, `google_api_key`: Strings for respective API keys, for authenticating the LLM.

### Usage
This file is used to validate and structure the expected configuration and inputs for the `SimplifiedLLMOncePB` class step.


## File: patchwork/steps/SimplifiedLLMOncePB/__init__.py

### Description
The `__init__.py` file is used to mark the directory as a package. This file is currently empty and doesn't contain any implementation.

## File: patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py

### Imports
- Standard `json` library
- `Step` from `patchwork.step`
- `SimplifiedLLM` from `patchwork.steps.SimplifiedLLM.SimplifiedLLM`
- `SimplifiedLLMOncePBInputs` from `typed.py`

### Class Definition
#### `SimplifiedLLMOncePB`
Extends `Step` class and initializes with `SimplifiedLLMOncePBInputs`.

### Constructor (`__init__` method)
- Initializes the inputs into the class.
- Stores the user prompt, system prompt (optional), prompt values, and JSON schema.

### Methods
#### `__json_schema_as_suffix(self, prompt: str)`
- Appends the JSON schema to the prompt to ensure responses conform to the specified format.

#### `run(self) -> dict`
- Constructs the prompt dictionary based on user and system prompts.
- Initializes and runs a `SimplifiedLLM` instance, passing the inputs and prompt.
- Returns the extracted responses along with the token usage statistics from the LLM output.

### Usage
#### Example
To use the `SimplifiedLLMOncePB` class, instantiate it with the required and optional inputs, and then call the `run` method:

```python
inputs = {
    "json_schema": {"type": "object", "properties": {"response": {"type": "string"}}},
    "user_prompt": "What is the capital of France?",
    "prompt_value": {},
    "model": "text-davinci-002",
    "openai_api_key": "YOUR_OPENAI_API_KEY",
}

step = SimplifiedLLMOncePB(inputs)
output = step.run()
print(output)
```

## Conclusion
This module, particularly the `SimplifiedLLMOncePB` class, facilitates a structured way to interact with LLMs by defining the necessary input configurations and handling the execution of a prompt to the LLM. It adheres to a strict input schema to ensure reliable and predictable interactions with the language model APIs.