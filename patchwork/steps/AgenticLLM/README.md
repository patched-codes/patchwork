# AgenticLLM Module Documentation

The `AgenticLLM` module is part of the `patchwork` library, designed for managing advanced conversation and reasoning strategies with language models. This module is structured into several components, each contained in a separate file within the directory `patchwork/steps/AgenticLLM`.

## Components

### 1. `typed.py`

#### Overview

This file defines the input and output types for the `AgenticLLM` class using `TypedDict` from the `typing_extensions` module. This enables strong typing for structured data, essential for ensuring the correct handling of inputs and outputs within the `AgenticLLM` workflow.

#### Inputs

- `base_path`: `str` (Optional) - Path for base directory.
- `prompt_value`: `Dict[str, Any]` - Structured data for prompts.
- `system_prompt`: `str` - Template for system-generated prompts.
- `user_prompt`: `str` - Template for user prompts.
- `max_llm_calls`: `int` - Maximum number of language model calls.
- `openai_api_key`, `anthropic_api_key`, `patched_api_key`, `google_api_key`: `str` - API keys required for accessing different language model services, handled with logical OR operations to allow for flexible configurations.

#### Outputs

- `conversation_history`: `List[Dict]` - Record of the conversation history.
- `tool_records`: `List[Dict]` - The logs of tool actions during interactions.

### 2. `AgenticLLM.py`

#### Overview

This file implements the `AgenticLLM` class, extending the `Step` class. It uses an agentic strategy to facilitate multi-turn conversations with an LLM client.

#### How It Works

- **Initialization**: Uses inputs to configure conversation limits and agentic strategy. It sets up the LLM client and available tools.
- **Execution**: The `run` method executes the conversation strategy, accumulating and returning the history of interactions and tool records.

### 3. `__init__.py`

#### Overview

This file is a placeholder for package initialization. It currently contains no code.

## Usage

The `AgenticLLM` module is intended for use in applications that require sophisticated interaction strategies with language models. Users need to provide necessary API keys and configure other parameters specific to their use case. The main operations will involve initializing `AgenticLLM` with required inputs and executing the `run` method to perform tasks.

### Prerequisites

- Appropriate API keys for LLM services.
- Python environment with required packages installed.

By organizing the module with clear type definitions (`typed.py`), core logic for interaction (`AgenticLLM.py`), and package setup (`__init__.py`), the `AgenticLLM` offers a structured framework for complex language model interactions, supporting dynamic strategy implementation through customizable inputs and outputs.
