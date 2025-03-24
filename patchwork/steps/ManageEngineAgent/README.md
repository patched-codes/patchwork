# ManageEngineAgent Documentation

This document provides an overview of the ManageEngineAgent component, detailing its inputs, outputs, and core functionality. This component design is intended to facilitate interactions with the ManageEngine ServiceDesk via the ServiceDeskPlus API, enabling operations such as ticket retrieval, creation, or modification.

## Overview

The `ManageEngineAgent` class is part of a larger framework for managing service desk interactions programmatically. The class defines a structured way to use a language model to interact with the ManageEngine API, turn inputs into actionable API operations, and return outputs in the form of conversation history and tokens used.

## Inputs

The `ManageEngineAgent` takes various inputs which are required for its operation:

### Required Inputs

- **zoho_access_token**: `str`
  - The OAuth token for authenticating API requests to ManageEngine.
  
- **user_prompt**: `str`
  - The initial prompt or query from the user that sets the context for API interactions.

- **prompt_value**: `Dict[str, Any]`
  - A dictionary of additional parameters and values to be used in rendering and handling prompts.

### Optional Inputs

- **max_agent_calls**: `int`
  - Maximum number of API calls the agent can make in a session. Default is 1.

- **openai_api_key**: `Annotated[str]`
  - OpenAI API key which can be used along with other API keys as an alternative.

- **anthropic_api_key**: `Annotated[str]`
  - Anthropic API key as an alternative to other API keys.

- **google_api_key**: `Annotated[str]`
  - Google API key that can be alternate to other API keys used for language model interactions.

- **system_prompt**: `Optional[str]`
  - A default system prompt which sets the agent's environment context if not provided by the user.

- **example_json**: `Optional[Dict]`
  - Sample JSON structure to guide how the outputs should be formatted.

## Outputs

The functionality provides outputs that include:

- **conversation_history**: `List[Dict]`
  - A list capturing the history of interactions or steps taken in the course of the agent's operation.

- **tool_records**: `List[Dict]`
  - Records of API interactions detailing the tools used and their outcomes.

- **request_tokens**: `int`
  - Number of tokens used in API requests.

- **response_tokens**: `int`
  - Number of tokens used in API responses.

## Usage

The `ManageEngineAgent` class is typically initiated with a dictionary of inputs, and it raises a `ValueError` if the required inputs are not provided. It uses a conversation limit to restrict the number of interactions. The primary method `run()` executes the agent's strategy and returns a result along with an account of tokens used, potentially useful for cost estimation in cases where language models or metered API services are involved.

## Implementation Details

Implementation involves primarily the setup and execution of an `AgenticStrategyV2`. It uses a preconfigured language model client for processing prompts and relies on tools specifically designed to interact with the ManageEngine API.

The headers for API requests are set using the `zoho_access_token`, and it uses the `make_api_request` tool to execute API operations. The entire system is designed to assist a software developer in automating service desk tasks effectively, and the framework is flexible to handle various service desk operations.
