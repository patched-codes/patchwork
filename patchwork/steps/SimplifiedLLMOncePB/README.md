# SimplifiedLLMOncePB Documentation

## Table of Contents
- [File: patchwork/steps/SimplifiedLLMOncePB/typed.py](#file-patchworkstepssimplifiedllmoncepbtypedpy)
    - [Code Explanation](#code-explanation-typed)
    - [Inputs](#inputs-typed)
- [File: patchwork/steps/SimplifiedLLMOncePB/__init__.py](#file-patchworkstepssimplifiedllmoncepbinitpy)
    - [Code Explanation](#code-explanation-init)
- [File: patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py](#file-patchworkstepssimplifiedllmoncepbsimplifiedllmoncepbpy)
    - [Code Explanation](#code-explanation-simplifiedllmoncepb)
    - [Inputs](#inputs-simplifiedllmoncepb)
    - [Outputs](#outputs-simplifiedllmoncepb)

## File: patchwork/steps/SimplifiedLLMOncePB/typed.py

### Code Explanation

This file defines the expected input structure for the `SimplifiedLLMOncePB` step using Python's `TypedDict` for type enforcement. It ensures the necessary fields are provided and outlines conditional requirements for API keys.

### Inputs (Typed)

- **json_schema**: `Dict[str, Any]`
  - Description: JSON schema to validate the response format.
  - Configurable: Yes

- **user_prompt**: `str`
  - Description: User's prompt input.
  - Configurable: Yes

- **prompt_value**: `Dict[str, Any]`
  - Description: Values to be used within the prompt.

- **system_prompt**: `str` (optional)
  - Description: System's prompt input.
  - Configurable: Yes

- **model**: `str`
  - Description: Model identifier for the LLM.
  - Configurable: Yes

- **openai_api_key** / **anthropic_api_key** / **patched_api_key** / **google_api_key**: `str`
  - Description: API keys for various LLM services.
  - Configurable: Yes
  - Conditional: Only one key is required.

## File: patchwork/steps/SimplifiedLLMOncePB/__init__.py

### Code Explanation

This file initializes the `SimplifiedLLMOncePB` module. It is currently empty, serving as a marker for the package.

## File: patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py

### Code Explanation

This file implements the `SimplifiedLLMOncePB` step, extending the `Step` class and using the defined `SimplifiedLLMOncePBInputs` class for input structure validation. It processes user and system prompts to query a language model (LLM), ensuring responses follow a specific JSON format.

### Inputs (SimplifiedLLMOncePB)

- **inputs**: `SimplifiedLLMOncePBInputs`
  - Description: The input dictionary conforming to the `SimplifiedLLMOncePBInputs` class.

### Outputs (SimplifiedLLMOncePB)

- **run()**: `dict`
  - Description: Executes the step, sending the formatted prompts to the LLM and returning the structured JSON response.
  - Fields Returned:
    - **extracted_responses**: LLM generated responses parsed from the JSON schema.
    - **request_tokens**: Number of tokens requested.
    - **response_tokens**: Number of tokens in the LLM's response.

---

Feel free to refer to the contents above to understand the usage and input/output specifications for the `SimplifiedLLMOncePB` code files.