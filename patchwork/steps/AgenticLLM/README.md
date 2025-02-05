# Documentation: AgenticLLM Module

## Overview
The `AgenticLLM` module provides the implementation of an autonomous agent that utilizes a Large Language Model (LLM) to execute multi-turn conversation strategies. At its core, it uses an agentic strategy that orchestrates tools and utilizes templates for generating conversations. This functionality is encapsulated in the `AgenticLLM` class, which extends the generic `Step` class and utilizes defined input and output types to maintain structure and reliability.

### Main Components
- `AgenticLLM`: A class that integrates tools and strategies to facilitate LLM-based conversation execution.
- `AgenticLLMInputs`: A typed dictionary that defines the expected inputs for the `AgenticLLM` class.
- `AgenticLLMOutputs`: A typed dictionary that defines the structure of the outputs produced by the `AgenticLLM` class.

## Inputs

### `AgenticLLMInputs` Structure
- **base_path**: `str`
  - The base directory path for loading tools.
  
- **prompt_value**: `Dict[str, Any]`
  - Dictionary of prompt parameters for template usage during conversation.
  
- **system_prompt**: `str`
  - Template for the system prompt.
  
- **user_prompt**: `str`
  - Template for the user prompt.
  
- **max_llm_calls**: `int`
  - Maximum number of LLM calls allowed, impacting the conversation limit.
  
- **openai_api_key**: `str`
  - API key for OpenAI services with fallback options for other API keys.
  
- **anthropic_api_key**: `str`
  - API key for Anthropic services, also allows fallbacks for different API keys.
  
- **patched_api_key**: `str`
  - Primary API key used with clear instructions on obtaining and using, capable of substituting other keys.
  
- **google_api_key**: `str`
  - API key for Google services, interchangeable with other service keys.

## Outputs

### `AgenticLLMOutputs` Structure
- **conversation_history**: `List[Dict]`
  - A list containing the conversation history in dictionary form.
  
- **tool_records**: `List[Dict]`
  - A list of tool usage records captured during conversation execution.
  
## Usage
1. **Initialization**: Create an instance of `AgenticLLM` by providing a dictionary that matches the `AgenticLLMInputs` structure.

2. **Execution**: Call the `run` method on the `AgenticLLM` instance to execute the conversation strategy defined and managed by `AgenticStrategy`.

3. **Accessing Results**: The output is a dictionary as defined by `AgenticLLMOutputs`, which includes the conversation history and any tool usage records.

This module is designed for developers and engineers who want to implement and manage advanced conversation strategies powered by LLMs, in environments where integration with different toolsets and API platforms is necessary. The structured input and output dictionaries help in maintaining clarity and consistency across different use cases and conversation configurations.
