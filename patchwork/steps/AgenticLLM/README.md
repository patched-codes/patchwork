# Documentation for `AgenticLLM`

## Overview

The `AgenticLLM` module is designed to facilitate interactions with language models using multiple APIs, leveraging agentic strategies. It includes typed input and output definitions along with a class to manage conversational logic. The code is structured in three Python files: `typed.py`, `AgenticLLM.py`, and `__init__.py`.

## Files

### 1. `typed.py`

This file defines typed dictionaries for inputs and outputs used by the Agentic LLM class. It ensures that inputs conform to expected types, enhancing code readability and reducing runtime errors.

#### Inputs

- **`base_path`** (optional): Base directory for tools, defaulting to the current working directory.
- **`prompt_value`**: Dictionary containing prompts for language model interaction.
- **`system_prompt`**: System-level prompt provided to the language model.
- **`user_prompt`**: User-level prompt for interaction.
- **`max_llm_calls`**: Maximum number of allowed language model calls, defined with a configuration annotation.
- **API Keys**: 
  - `openai_api_key`
  - `anthropic_api_key`
  - `patched_api_key`
  - `google_api_key`
  
  All API keys are annotated with configuration settings and fallback options.

#### Outputs

- **`conversation_history`**: List of conversation entries with the LLM.
- **`tool_records`**: Records of tools used during the session.

### 2. `AgenticLLM.py`

This file contains the main class `AgenticLLM`, which orchestrates the interaction with the language model using a multiturn agentic strategy.

#### Usage

- **Initialization**:
  - Takes a dictionary of inputs defined in `AgenticLLMInputs`.
  - Determines the base path and initializes conversation limits.
  
- **Method**:
  - `run()`: Executes the agentic strategy and returns a dictionary containing conversation history and tool records.

### 3. `__init__.py`

This file is currently empty, serving primarily to indicate that the directory is a Python package.

## Usage Example

To utilize the `AgenticLLM` class, provide the necessary inputs in a well-defined structure. For example, create an instance with necessary API keys, prompts, and a base path, then call the `run` method to initiate interactions.

```python
from patchwork.steps.AgenticLLM.AgenticLLM import AgenticLLM

inputs = {
    "base_path": "/path/to/tools",
    "prompt_value": {...},
    "system_prompt": "Your system prompt here",
    "user_prompt": "Your user prompt here",
    "max_llm_calls": 4,
    "openai_api_key": "your-openai-api-key",
    # Other optional keys...
}

agent = AgenticLLM(inputs)
output = agent.run()

print(output['conversation_history'])
print(output['tool_records'])
```

This module is ideal for applications requiring structured and multi-turn conversations with language models, supported by various API providers.
