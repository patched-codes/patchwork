# ManageEngineAgent Code Documentation

## Overview

The `ManageEngineAgent` module is part of a larger framework and facilitates interactions with the ManageEngine ServiceDesk API by utilizing advanced AI models to assist in ticket management through API requests. This implementation relies on a strategic AI-driven approach to handle conversations and API interactions, aiming to streamline service desk operations.

## File Structure

- **typed.py**: Defines input and output types for the `ManageEngineAgent` using Python's `TypedDict` for structured data annotations.
- **__init__.py**: An empty initialization file that allows the directory to be treated as a package.
- **ManageEngineAgent.py**: The core of the module where the `ManageEngineAgent` class is implemented, leveraging AI and API tools for efficient service desk management.

## Inputs

Defined in `typed.py` as part of the `ManageEngineAgentInputs` class:

### Required

- `zoho_access_token`: A string representing the Zoho authentication token to authorize API requests.
- `user_prompt`: A string to guide the AI interaction and provide context for the tasks to be accomplished.
- `prompt_value`: A dictionary containing dynamic information to be used in the user prompt.

### Optional

- `max_agent_calls`: An integer that limits the number of API calls during a session.
- `openai_api_key`, `anthropic_api_key`, `google_api_key`: Keys that specify which AI model to use for generating conversational and strategic responses, considering mutual exclusivity.
- `system_prompt`: An optional string to refine the AI's overarching conversation context.
- `example_json`: An optional dictionary for example data used in training or AI-response generation.

## Outputs

Defined in `typed.py` as part of the `ManageEngineAgentOutputs` class:

- `conversation_history`: A list of dictionaries representing the history of the AI-driven conversations.
- `tool_records`: A list of dictionaries documenting the interactions with the ManageEngine API.
- `request_tokens`: An integer indicating the number of tokens used in requests.
- `response_tokens`: An integer indicating the number of tokens generated in responses.

## Key Features

- **AI-Driven API Interactions**: The `ManageEngineAgent` uses a state-of-the-art conversational AI model to automate interactions with the ManageEngine ServiceDesk API.
- **Configurable Strategy**: Offers flexibility in selecting AI models and configuring API call limits to suit different operational needs.
- **Template-Driven Input Handling**: Utilizes `mustache_render` for dynamic user prompts and system messages, ensuring context-relevant interactions.

## Example Use Case

- **Automating Service Desk Tasks**: Integrate this agent into an IT service workflow to automate tasks such as ticket retrieval, updates, and creation via ManageEngine's ServiceDesk API.
- **AI-Augmented Decision Support**: Use configured conversation strategies to provide AI recommendations alongside operational reports to decision-makers.

By structuring the code using Python’s `TypedDict` and leveraging advanced AI strategies, the `ManageEngineAgent` module provides robust support for intelligent service management operations.
