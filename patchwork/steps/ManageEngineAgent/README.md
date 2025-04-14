# ManageEngineAgent Module

## Overview

The `ManageEngineAgent` module is a Python-based tool designed to interface with the ManageEngine ServiceDesk via the ServiceDeskPlus API. It utilizes large language models (LLMs) for handling multi-turn conversations and automating interactions with the ManageEngine system. The main components of this module include input validations, agent configurations, and API tool integrations.

## Inputs

The inputs required for the `ManageEngineAgent` are specified in the `ManageEngineAgentInputs` TypedDict. These include mandatory and optional fields:

- **Mandatory Inputs:**
  - `zoho_access_token`: A string representing the OAuth token for authenticating with ManageEngine.
  - `user_prompt`: A user-provided prompt to guide the conversation or interaction.
  - `prompt_value`: A dictionary containing key-value pairs for prompt customization.

- **Optional Inputs:**
  - `max_agent_calls`: An integer specifying the maximum calls for conversation in a session. Defaults to 1 if not specified.
  - `openai_api_key`: An OpenAI API key string, can be provided as an alternative to or in conjunction with other API keys like Google or Anthropic.
  - `anthropic_api_key`: An Anthropic API key string, alternative to OpenAI or Google API keys.
  - `google_api_key`: A Google API key string, alternative to OpenAI or Anthropic API keys.
  - `system_prompt`: An optional string for defining the system-level prompt for the agent.
  - `example_json`: An optional dictionary for providing example JSON structures to guide response shaping.

## Outputs

The outputs provided by `ManageEngineAgent` are specified in the `ManageEngineAgentOutputs` TypedDict:

- **Outputs:**
  - `conversation_history`: A list of dictionaries recording the history of interactions and conversations.
  - `tool_records`: A list of records detailing API tool interactions during the session.
  - `request_tokens`: An integer indicating the number of tokens used in requests.
  - `response_tokens`: An integer indicating the number of tokens used in responses.

## Usage

The `ManageEngineAgent` class serves as a step in a process, integrating seamlessly within workflows that require interaction with ManageEngine ServiceDesk instances.

### **Initialization:**
The class is initialized with a dictionary of inputs. It validates the presence of `zoho_access_token` and `user_prompt`, configuring headers for API requests and setting up a language model client.

### **Agentic Strategy:**
The agent uses the `AgenticStrategyV2` to manage conversation logic with a specified language model (`claude-3-7-sonnet-latest`). It configures the agent with tools needed for making API requests to the ManageEngine system.

### **Running the Agent:**
The `run` method executes the agentic strategy while respecting conversation limits and returns the results along with usage metrics, including conversation history, tool usage, and token counts.

This module is particularly useful for developers or teams looking to automate and streamline their ManageEngine interactions programmatically using LLMs. The flexibility to switch between API keys and provide system prompts allows customization and adaptation to various use cases.
