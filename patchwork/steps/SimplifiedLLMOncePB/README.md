# Documentation for `patchwork/steps/SimplifiedLLMOncePB`

This documentation covers the files and code within the `patchwork/steps/SimplifiedLLMOncePB` directory. This module is designed to handle a simplified language model (LLM) once with pre-batched (PB) inputs.

## File: `patchwork/steps/SimplifiedLLMOncePB/typed.py`

- **Extension**: .py
- **Size**: 1616 bytes
- **Created**: 2024-09-17 10:06:22
- **Modified**: 2024-09-17 10:06:22

### Summary
This file defines the structure of the inputs required for the `SimplifiedLLMOncePB` step using `TypedDict` and `Annotated`. It includes configurations for required and optional fields that represent the prompts and API keys necessary to call a language model.

### Inputs

The class `SimplifiedLLMOncePBInputs` defines various fields:
- **json_schema**: A dictionary representing the schema of the JSON.
- **user_prompt**: A string containing the user's prompt.
- **prompt_value**: A dictionary of additional values relevant to the prompt.

Optional fields include:
- **system_prompt**: A string containing the system's prompt.
- **model**: A string specifying the model to use.
- **openai_api_key**: An API key for OpenAI.
- **anthropic_api_key**: An API key for Anthropic.
- **patched_api_key**: An API key obtained from a specific token URL.
- **google_api_key**: An API key for Google.

## File: `patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py`

- **Extension**: .py
- **Size**: 1351 bytes
- **Created**: 2024-09-17 10:06:22
- **Modified**: 2024-09-17 10:06:22

### Summary
This file contains the implementation of the `SimplifiedLLMOncePB` class which extends the `Step` class and is designed to interface with the `SimplifiedLLM` step.

### Inputs
- The class expects an input dictionary `{}` that adheres to the structure defined in `SimplifiedLLMOncePBInputs`.

### Outputs
- **run** method: Executes the step, and calls the underlying LLM with appropriately structured prompts and configurations.
- Returns a dictionary containing the extracted responses and tokens from the LLM.

### Usage
The class is initialized with inputs defined by `SimplifiedLLMOncePBInputs`, and its `run` method constructs the prompts and invokes the language model, returning relevant outputs.

## File: `patchwork/steps/SimplifiedLLMOncePB/__init__.py`

- **Extension**: .py
- **Size**: 0 bytes
- **Created**: 2024-09-17 10:06:22
- **Modified**: 2024-09-17 10:06:22

### Summary
This file is an empty file intended to mark the directory as a Python package.

---

By summarizing the functionality and structures present in these files, users can better understand how to use the `SimplifiedLLMOncePB` step within their workflows and the necessary inputs and expected outputs.