# Documentation: `patchwork/steps/SimplifiedLLMOncePB`

## Overview

The `SimplifiedLLMOncePB` module consists of several Python files that are designed to facilitate interaction with a Language Learning Model (LLM) in a simplified manner, using a Prompt-Blocking process. The main files include:

1. `typed.py` which defines the input schema for the module.
2. `SimplifiedLLMOncePB.py` which implements the actual logic for calling the LLM.
3. `__init__.py` which serves as the package initializer.

---

## File: `patchwork/steps/SimplifiedLLMOncePB/typed.py`

- **Extension**: .py
- **Size**: 1616 bytes
- **Created**: 2024-09-17 06:13:17
- **Modified**: 2024-09-17 06:13:17

### Code Summary

This file defines the required and optional inputs for the `SimplifiedLLMOncePB` class through TypedDict and Annotated types. The inputs are parameterized to configure the model and API keys required to interact with various LLM services. 

### Inputs

- **json_schema**: A dictionary representing the JSON schema configuration required (type: `Dict[str, Any]`).
- **user_prompt**: The user-provided prompt (type: `str`).
- **prompt_value**: A dictionary containing specific values for prompt (type: `Dict[str, Any]`).
- **system_prompt** (Optional): The system-generated prompt (type: `str`).
- **model**: The model to be used (type: `str`).
- **openai_api_key**: API key for OpenAI (type: `str`).
- **anthropic_api_key**: API key for Anthropic (type: `str`).
- **patched_api_key**: API key for the patched model (type: `str`).
- **google_api_key**: API key for Google (type: `str`).

---

## File: `patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py`

- **Extension**: .py
- **Size**: 1351 bytes
- **Created**: 2024-09-17 06:13:17
- **Modified**: 2024-09-17 06:13:17

### Code Summary

This file implements the `SimplifiedLLMOncePB` class which is a subclass of `Step`. It initializes with the given inputs and runs a language model prompt, consolidating the responses and token usage into a final output dictionary.

### Inputs

- **inputs**: A dictionary containing various configuration parameters such as `user_prompt`, `system_prompt`, `prompt_value`, `json_schema`, and different possible API keys.

### Outputs

- **Output Dictionary**: 
  - The extracted LLM responses (`extracted_responses`).
  - The number of tokens requested (`request_tokens`).
  - The number of tokens in the response (`response_tokens`).

### How to Use

1. Initialize the `SimplifiedLLMOncePB` with the required inputs (e.g., `user_prompt`, `json_schema`, etc.).
2. Call the `run()` method to execute the LLM prompt.
3. Receive a dictionary containing the prompt's response and token information.

---

## File: `patchwork/steps/SimplifiedLLMOncePB/__init__.py`

- **Extension**: .py
- **Size**: 0 bytes
- **Created**: 2024-09-17 06:13:17
- **Modified**: 2024-09-17 06:13:17

### Code Summary

This file is the package initializer and does not contain any code.

---

This documentation provides a comprehensive overview of each file's purpose, input parameters, and expected outputs within the `SimplifiedLLMOncePB` module. This should aid developers in understanding and implementing the functionality offered by this package.
