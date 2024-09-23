# Documentation for `patchwork/steps/SimplifiedLLMOncePB` Module

## Table of Contents
- [Overview](#overview)
- [Files](#files)
  - [File: `typed.py`](#file-typedpy)
    - [Inputs](#inputs)
    - [Outputs](#outputs)
  - [File: `__init__.py`](#file-initpy)
  - [File: `SimplifiedLLMOncePB.py`](#file-simplifiedllmoncepbpy)
    - [Class: `SimplifiedLLMOncePB`](#class-simplifiedllmoncepb)

## Overview
The module `SimplifiedLLMOncePB` is part of the Patchwork library and contains functionality for running a simplified Large Language Model (LLM) using a specific schema and set of parameters. The main components of this module include type definition for inputs, an initialization file, and the implementation file, which includes the primary logic for invoking the LLM.

## Files

### File: `typed.py`

- **Extension**: `.py`
- **Language**: Python
- **Size**: 1616 bytes
- **Created**: 2024-09-23 12:00:21
- **Modified**: 2024-09-23 12:00:21

#### Inputs
The `typed.py` defines structured input types for the `SimplifiedLLMOncePB` step using Python's `TypedDict` and `Annotated` from `typing_extensions`. Here’s a summary of the input types:

- **json_schema** (Required): A dictionary containing the JSON schema.
- **user_prompt** (Required): A string representing the user's prompt.
- **prompt_value** (Required): A dictionary holding the values to be substituted in the prompt.
- **system_prompt** (Optional): An optional string for system-generated prompt.
- **model** (Optional): The name of the LLM model to use.
- **openai_api_key** (Optional, Conditional): API key for OpenAI, with conditional alternatives.
- **anthropic_api_key** (Optional, Conditional): API key for Anthropic, with conditional alternatives.
- **patched_api_key** (Optional, Conditional): API key for Patched integration.
- **google_api_key** (Optional, Conditional): API key for Google, with conditional alternatives.

These inputs are organized within a class `SimplifiedLLMOncePBInputs`, which extends `TypedDict`.

#### Outputs
This file does not explicitly define outputs, but the structured input types are essential for running the LLM step correctly.

### File: `__init__.py`

- **Extension**: `.py`
- **Language**: Python
- **Size**: 0 bytes
- **Created**: 2024-09-23 12:00:21
- **Modified**: 2024-09-23 12:00:21

#### Code
This file is currently empty but is present to signify the directory as a Python package.

### File: `SimplifiedLLMOncePB.py`

- **Extension**: `.py`
- **Language**: Python
- **Size**: 1351 bytes
- **Created**: 2024-09-23 12:00:21
- **Modified**: 2024-09-23 12:00:21

#### Class: `SimplifiedLLMOncePB`

- **Base Classes**: `Step`
- **Inputs**: `SimplifiedLLMOncePBInputs`

##### Methods
- **`__init__(self, inputs)`**: Initializes the class with provided inputs. It organizes and stores the user and system prompts, as well as the prompted values and JSON schema example.
- **`run(self)`**: Executes the LLM based on provided inputs and returns a dictionary containing:
  - Extracted responses from the LLM
  - Request tokens
  - Response tokens

### Code

The core functionality lies in the `SimplifiedLLMOncePB` class within `SimplifiedLLMOncePB.py`. It constructs a prompt based on the provided inputs and invokes the `SimplifiedLLM` class to run the model. It processes the LLM responses and returns relevant output data.

This class is likely to be used by developers needing to integrate a simplified LLM into their applications, using a structured and configurable interface to manage prompts and API keys effectively.

---

For further details or specific usage examples, refer to the `patchwork` library documentation and the accompanying source code above.