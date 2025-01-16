# Documentation for AgenticLLM Step

## Overview

The provided code is part of a larger module intended for use with artificial intelligence models and specifically focuses on agent-based language model interactions. It defines a typed structure for inputs and outputs related to the operation of an "AgenticLLM" and implements its logic. This code is part of the `patchwork` library, which seems to provide functionality for executing multi-turn strategies with AI language models. The files covered are `typed.py`, `AgenticLLM.py`, and `__init__.py`.

## File: `typed.py`

### Description

This file defines the expected inputs and outputs for the `AgenticLLM` class using typed dictionaries. These structures specify the configuration and operational parameters needed to execute agent-based language model operations.

### Inputs

- **base_path (str):** Optional; the base directory path.
- **prompt_value (Dict[str, Any]):** Contains values for templates in prompts.
- **system_prompt (str):** Template string for the system prompt.
- **user_prompt (str):** Template string for the user prompt.
- **max_llm_calls (int):** Maximum number of language model API calls allowed.
- **openai_api_key (str):** Configuration option for using an OpenAI API key.
- **anthropic_api_key (str):** Configuration option for using an Anthropic API key.
- **patched_api_key (str):** Fallback configuration requiring a valid API key.
- **google_api_key (str):** Configuration option for using a Google API key.

All API keys are mutually exclusive options, and at least one must be provided.

### Outputs

- **conversation_history (List[Dict]):** History of interactions with the language model.
- **tool_records (List[Dict]):** Records of tools created or utilized during execution.

## File: `AgenticLLM.py`

### Description

`AgenticLLM.py` implements the actual logic using the structured inputs and producing accordingly structured outputs. It leverages the `AgenticStrategy` which is geared towards multi-turn conversation with language models.

### Main Class: `AgenticLLM`

#### Initialization

- It initializes using input dictionaries. It takes parameters and sets up the environment for executing the strategy.
- Configures a base path and determines the conversation limit by halving `max_llm_calls`.

#### Execution

- `run()` method executes the agent strategy.
- Returns a dictionary with conversation history and tool records.

## File: `__init__.py`

### Description

This file seems to be a placeholder, as it is empty. It is likely intended for package initialization purposes, allowing for the `AgenticLLM` module to be imported as part of the `patchwork` library.

---

This package likely serves developers and researchers employing conversational AI models in complex environments, enabling effective management of multifaceted automated discussions through a structured yet flexible approach.
