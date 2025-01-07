# Documentation: AgenticLLM Step

## Overview

The `AgenticLLM` code comprises three Python files that together implement a structured process for interacting with a language model (LLM) using an agentic strategy. It relies on typed input parameters and produces outputs to track the conversations and tool records utilized. The agent runs through an execution strategy that potentially utilizes different API keys and prompts to interact with LLMs.

## File Structure

### 1. `patchwork/steps/AgenticLLM/typed.py`

This file defines the input and output types required for executing an agentic LLM step.

#### **Inputs:**

- `prompt_value`: A dictionary for custom prompt configuration.
- `system_prompt`: A string to setup the system prompt.
- `user_prompt`: A string for configuring the user prompt.
- `max_llm_calls`: An integer specifying the maximum allowed calls to the LLM, with configurations.
- `model_args`: String arguments configuring the model.
- `client_args`: String arguments for setting up the client.
- API Keys:
  - `openai_api_key`
  - `anthropic_api_key`
  - `patched_api_key` (Main API key)
  - `google_api_key`
  
  These are configured to be interchangeable, ensuring at least one is provided.

#### **Outputs:**

- `conversation_history`: A list of dictionary entries logging each stage of conversation.
- `tool_records`: A list of dictionary entries detailing the use of any tools in the process.

### 2. `patchwork/steps/AgenticLLM/AgenticLLM.py`

Implements the main functionality for running an LLM-based step using the defined inputs and outputs.

#### **Functionality:**

- **Initialization:**
  - Accepts inputs as defined in `AgenticLLMInputs`.
  - Sets a base path where tools might be located.
  - Initializes an agentic strategy using the `AioLlmClient` and a set of tools based on the inputs.

- **Execution (`run` Method):**
  - Executes the agentic strategy up to a defined limit based on `max_llm_calls`.
  - Collects and returns the conversation history and tool records.

### 3. `patchwork/steps/AgenticLLM/__init__.py`

Contains no code. Likely used for package initialization purposes.

## Usage

To use the `AgenticLLM` step, one must:

1. Configure inputs using `AgenticLLMInputs`, ensuring to set the appropriate API keys for LLM access, prompts, model, and client configurations.
2. Instantiate `AgenticLLM` with these inputs.
3. Call the `run` method to execute the step, which manages interaction with the LLM and outputs the conversation history and tool records. 

This setup is likely employed in more extensive frameworks relying on LLM-based decision-making and response generation, such as AI assistants and automation tools using multi-turn interaction strategies.
