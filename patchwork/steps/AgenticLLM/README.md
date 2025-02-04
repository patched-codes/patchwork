# AgenticLLM Module Documentation

This documentation provides an overview of the `AgenticLLM` Python module, part of the `patchwork` package. The functionality and structure of the module are explained, with clear definitions of inputs and outputs.

## Overview

The `AgenticLLM` module is designed to facilitate interaction with Large Language Models (LLMs) using an agentic strategy. This strategy involves interacting with LLMs through a series of prompts and tools to generate responses effectively. The module leverages an asynchronous LLM client and multiturn agentic strategy to conduct conversations and log tool usage records.

## Files

### 1. `AgenticLLM.py`

This is the core implementation of the `AgenticLLM`, defining its initialization and execution logic.

#### Inputs

- **base_path (str)**: Base directory path for tools; defaults to current working directory.
- **prompt_value (Dict[str, Any])**: Data to be included in the conversation prompts.
- **system_prompt (str)**: Template for system-level prompts to the LLM.
- **user_prompt (str)**: Template for user-level prompts.
- **max_llm_calls (int)**: Maximum number of LLM calls permitted, used to set conversation limits.
- **API Keys**: Configurable keys for accessing external LLM services, including:
  - `openai_api_key`
  - `anthropic_api_key`
  - `patched_api_key`
  - `google_api_key`

#### Outputs

- **conversation_history (List[Dict])**: Log of conversation exchanges during the execution.
- **tool_records (List[Dict])**: Records detailing the use of tools in the conversation flow.

### 2. `__init__.py`

This file exists to make the `AgenticLLM` package a valid Python package. It is currently empty.

### 3. `typed.py`

Contains the definitions for structured input and output types used by the `AgenticLLM` class.

#### Input Type: `AgenticLLMInputs`

A typed dictionary that includes fields for configuring the `AgenticLLM`, including API keys and prompt formats.

#### Output Type: `AgenticLLMOutputs`

A typed dictionary defining the structure of the output from the agentic strategy, primarily encompassing conversation history and tool usage records.

## Usage

Users might employ the `AgenticLLM` to orchestrate structured interactions with LLMs, leveraging tools and agentic strategies for enhanced conversation capabilities. Users must configure the necessary API keys and prompts to tailor the LLM responses to their needs. This module is suitable for applications requiring integration with external LLM services and sophisticated interaction flows.

This documentation serves as a guide to understanding the structure and function of the `AgenticLLM` module, supporting developers in implementing and utilizing its capabilities in various applications.
