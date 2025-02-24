# Documentation for Agentic LLM Code

## Overview

The Agentic LLM module appears to be part of the `patchwork` package designed to handle Large Language Model (LLM) interactions using a predefined agentic strategy. This implementation facilitates the elicitation of responses from a language model, manages API keys, and defines the input and output data structures for the interactions.

### Structure

The module is organized as follows:

- **`__init__.py`**: An empty initialization file to make the directory a package.
- **`typed.py`**: Defines the input and output data types for the agentic LLM process.
- **`AgenticLLM.py`**: Implements the main logic for the agentic LLM step, utilizing an agentic strategy and multi-turn interactions with a language model.

## Detailed Description

### File: `typed.py`

#### Inputs

- **`base_path`**: (Optional) The base path for accessing necessary tools.
- **`prompt_value`**: A dictionary that contains dynamic values for templated prompts.
- **`system_prompt`**: A string used as a system prompt template.
- **`user_prompt`**: A string used as a user prompt template.
- **`max_llm_calls`**: An integer that indicates the maximum number of LLM API calls allowed. It is treated as a configuration parameter.
- **API Keys**: Includes `openai_api_key`, `anthropic_api_key`, `patched_api_key`, and `google_api_key`. These configurations allow different API keys to be specified for integrations with various LLM services.

#### Outputs

- **`conversation_history`**: A list of dictionaries tracking the conversation steps with the model.
- **`tool_records`**: A list of dictionaries containing records of tool usage during interactions.
- **`request_tokens`**: An integer indicating the number of tokens sent in requests.
- **`response_tokens`**: An integer showing the number of tokens received in responses.

### File: `AgenticLLM.py`

#### Functionality

- **Initialization**: The class initializes by configuring the LLM client and toolset for interaction. It uses the provided input configuration to create an agentic strategy.
- **Execution**: The `run` method executes the agentic strategy with a set conversation limit. It returns structured output data including conversation history and tool usage statistics.

#### Usage

The `AgenticLLM` class is likely used in scenarios where automated and dynamic interaction with a language model is needed. The inputs are configured to adjust queries dynamically, and the comprehensive configuration support ensures flexible integration across multiple API providers.

---

This documentation is intended to offer a comprehensive overview and guide for developers working with or extending the functionality of the AgenticLLM module within the `patchwork` framework.
