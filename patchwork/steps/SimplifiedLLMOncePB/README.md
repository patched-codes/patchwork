# Documentation for `SimplifiedLLMOncePB` Module

## Overview

This module integrates a simplified Large Language Model (LLM) interaction, encapsulated within the `SimplifiedLLMOncePB` class. The class is designed to handle prompt-related functionalities by receiving inputs, processing prompts, and returning structured outputs based on the specified JSON schema.

## Files

### 1. `patchwork/steps/SimplifiedLLMOncePB/typed.py`

#### Description

Defines the types and structures for the input parameters required by the `SimplifiedLLMOncePB` class. This includes necessary and optional keys related to API keys, prompts, and schemas.

#### Inputs

- **Required Fields:**
  - `json_schema` (Dict[str, Any]): The schema to validate the output, annotated with `StepTypeConfig`.
  - `user_prompt` (str): The user-provided prompt, annotated with `StepTypeConfig`.
  - `prompt_value` (Dict[str, Any]): Variables to be filled in the prompt.

- **Optional Fields:**
  - `system_prompt` (str): System level prompt, annotated with `StepTypeConfig`.
  - `model` (str): Specifies the LLM model, annotated with `StepTypeConfig`.
  - `openai_api_key` (str): OpenAI API key (mutually exclusive with other API keys).
  - `anthropic_api_key` (str): Anthropic API key (mutually exclusive with other API keys).
  - `patched_api_key` (str): Patched API key (mutually exclusive with other API keys, includes helper message for acquiring key).
  - `google_api_key` (str): Google API key (mutually exclusive with other API keys).

### 2. `patchwork/steps/SimplifiedLLMOncePB/__init__.py`

#### Description

An empty file used to mark the directory as a Python package.

### 3. `patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py`

#### Description

Core functionality of the Simplified LLM Once Pattern-Based implementation. The `SimplifiedLLMOncePB` class utilizes the specified inputs to construct and process LLM prompts.

#### Class: `SimplifiedLLMOncePB`

- **Initialization:**
  - Takes `SimplifiedLLMOncePBInputs` as the input and initializes internal variables such as user prompts, system prompts, JSON schema, and prompt values.

- **Methods:**
  - `__json_schema_as_suffix(prompt: str)`: Generates a structured JSON format based on the provided prompt and the JSON schema.
  - `run() -> dict`: Main method that constructs the final prompt, interacts with the `SimplifiedLLM` class, and returns formatted responses including request and response tokens.

#### Outputs

- The `run` method returns a dictionary containing:
  - Extracted responses in JSON format.
  - Request tokens used for the interaction.
  - Response tokens received from the model.

## Usage

This module is used when there is a need to interact with a large language model in a structured manner, with specific schema validations and multiple API key support. It is likely used in a larger workflow where different LLMs can be swapped, and custom user prompts and system prompts are required for dynamic interactions.

Sample instantiation and usage might look like this:

```python
inputs = {
  "json_schema": {"type": "object", "properties": {"response": {"type": "string"}}},
  "user_prompt": "Translate this sentence.",
  "prompt_value": {"sentence": "Hello, world!"},
  "openai_api_key": "your_openai_api_key",
}

simplified_llm = SimplifiedLLMOncePB(inputs)
output = simplified_llm.run()
print(output)
```

This setup anticipates the user would provide necessary inputs as per the defined types in `typed.py`, initialize the `SimplifiedLLMOncePB` class, and subsequently call the `run` method to interact with the LLM and obtain the structured output.