# SimplifiedLLMOncePB Documentation

## Overview

The `SimplifiedLLMOncePB` module comprises three essential files to facilitate the interaction with a Simplified Large Language Model (LLM). It is organized in a way that allows you to configure and run a single prompt against the Simplified LLM, using a specified JSON schema for formatting the responses.

## Files

### [patchwork/steps/SimplifiedLLMOncePB/typed.py](#patchworkstepsSimplifiedLLMOncePBtyped.py)

#### Purpose

Defines input types and configurations for the `SimplifiedLLMOncePB` step. It ensures that user inputs and API keys are correctly handled and validated.

#### Inputs

- `json_schema`: Dictionary with any contents, enforced by `StepTypeConfig(is_config=True)`.
- `user_prompt`: String containing the user prompt, enforced by `StepTypeConfig(is_config=True)`.
- `prompt_value`: Dictionary containing various prompt values.
- `system_prompt`: Optional string for additional context.
- `model`: String specifying the model to use.
- `openai_api_key`: Optional string for OpenAI API key.
- `anthropic_api_key`: Optional string for Anthropic API key.
- `patched_api_key`: Optional string for a general patched API key.
- `google_api_key`: Optional string for Google API key.

#### Outputs

N/A (This file only defines the input schema)

---

### [patchwork/steps/SimplifiedLLMOncePB/__init__.py](#patchworkstepsSimplifiedLLMOncePB__init__.py)

#### Purpose

Contains package initialization code. It is currently empty but necessary for Python module structure.

#### Inputs

N/A

#### Outputs

N/A

---

### [patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py](#patchworkstepsSimplifiedLLMOncePBSimplifiedLLMOncePB.py)

#### Purpose

Implements the `SimplifiedLLMOncePB` class, which initializes and runs a single prompt against the Simplified LLM.

#### Inputs

- `inputs`: A dictionary adhering to the schema defined in `typed.py`. It includes:
  - `user_prompt`
  - `system_prompt` (optional)
  - `prompt_value`
  - `json_schema`
  - API keys (one of several types)

#### Outputs

- Returns a dictionary with:
  - Extracted responses in JSON format based on the `json_schema`.
  - Tokens information (`request_tokens` and `response_tokens`).

#### Methods

- `__init__(self, inputs)`: Initializes class variables.
- `__json_schema_as_suffix(self, prompt)`: Creates a prompt suffix using the JSON schema.
- `run(self)`: Executes the LLM interaction and returns the formatted response.

---

## How to Use

1. **Set up your inputs**: Ensure the inputs dictionary follows the schema defined in `typed.py`. This includes valid API keys and necessary prompts.
2. **Initialize the class**: Create an instance of the `SimplifiedLLMOncePB` class by passing the inputs.
3. **Run the process**: Call the `run` method to execute the LLM interaction and get the response formatted according to the provided JSON schema.

### Example

```python
from patchwork.steps.SimplifiedLLMOncePB.SimplifiedLLMOncePB import SimplifiedLLMOncePB

# Define inputs
inputs = {
    "json_schema": {"type": "object", "properties": {"response": {"type": "string"}}},
    "user_prompt": "Hello, how are you?",
    "prompt_value": {"some_key": "some_value"},
    "openai_api_key": "your-openai-api-key"
}

# Create an instance
llm_instance = SimplifiedLLMOncePB(inputs)

# Run the instance
response = llm_instance.run()

print(response)
```

This will send your prompt to the specified LLM and return the response in the JSON format you specified.