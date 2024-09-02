# Documentation for `patchwork/steps/SimplifiedLLMOncePB`


## Overview

This module consists of three files that provide functionality for a simplified interaction with a Large Language Model (LLM) using predefined prompts and API keys configuration:

1. [typed.py](#typedpy)
2. [__init__.py](#initpy)
3. [SimplifiedLLMOncePB.py](#simplifiedllmoncepbpy)

---

## File: typed.py

### Description

The `typed.py` file defines input typing for the `SimplifiedLLMOncePB` step using TypedDicts and annotations to ensure proper configuration of the input parameters.

### Inputs

The code defines two classes:

- `__SimplifiedLLMOncePBInputsRequired`: A TypedDict used to specify mandatory input fields.
- `SimplifiedLLMOncePBInputs`: Extends `__SimplifiedLLMOncePBInputsRequired` and adds optional fields, including various API keys that can be used interchangeably.

#### Fields

- `json_schema`: JSON schema (Dictionary).
- `user_prompt`: User-provided prompt (String).
- `prompt_value`: Dictionary of prompt values.
- `system_prompt`: System prompt (Optional, String).
- `model`: Model to be used (String).
- `openai_api_key`, `anthropic_api_key`, `patched_api_key`, `google_api_key`: API keys for various services (Strings).

### Usage

This file is typically used as an input schema to ensure that any instance of the `SimplifiedLLMOncePB` class has the proper configuration before execution.

---

## File: `__init__.py`

### Description

An empty `__init__.py` file that makes the directory a package.

### Usage

This file is not meant for direct use but is necessary for module packaging and imports.

---

## File: SimplifiedLLMOncePB.py

### Description

The `SimplifiedLLMOncePB.py` file defines the main functionality for running a simplified LLM step with pre-configured inputs.

### Class: SimplifiedLLMOncePB

This class extends the `Step` class and uses `SimplifiedLLMOncePBInputs` for input validation.

### Methods

#### `__init__(self, inputs)`

Initializes the class with the user, system prompts, and other required inputs.

- **Parameters**
  - `inputs`: Dictionary of inputs complying with `SimplifiedLLMOncePBInputs`.

#### `run(self) -> dict`

Executes the LLM step and returns a dictionary containing the response and token usage.

- **Returns**
  - A dictionary containing 
    - Extracted responses 
    - Request tokens 
    - Response tokens 

### Usage

This class is instantiated with required inputs and is used to execute an LLM step with properly validated input data. It uses another class `SimplifiedLLM` to perform the main computation.

---

### Example

Below is an example of how you might use `SimplifiedLLMOncePB`:

```python
from patchwork.steps.SimplifiedLLMOncePB.SimplifiedLLMOncePB import SimplifiedLLMOncePB

inputs = {
    "json_schema": {...},
    "user_prompt": "Translate the following text",
    "prompt_value": {"text": "Hello World"},
    "model": "gpt-3.5-turbo",
    "openai_api_key": "your-openai-api-key"
}

step = SimplifiedLLMOncePB(inputs)
output = step.run()
print(output)
```

This demonstrates setting up and running a simplified LLM step with API key configuration and prompt inputs.