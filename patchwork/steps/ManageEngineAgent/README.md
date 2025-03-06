# Documentation for ManageEngineAgent

## Overview

The ManageEngineAgent is a Python module designed to interact with the ManageEngine ServiceDesk via the ServiceDeskPlus API. It employs a sophisticated multiple-turn conversational strategy using language model clients to perform actions such as retrieving, creating, or modifying service desk tickets. This solution is specifically useful for integrating machine learning-driven conversational agents with service desk functionalities to automate and streamline service operations.

## Files and Classes

### 1. `typed.py`

This file defines typed structures for the inputs and outputs of the `ManageEngineAgent`. It uses Python's `TypedDict` to create structured data types that help in validating input and output formats.

#### Inputs

- **Required**:
  - `me_access_token` (str): Access token for authenticating requests to ManageEngine.
  - `user_prompt` (str): The user prompt that initiates the conversation.
  - `prompt_value` (Dict[str, Any]): Dynamic data to render within the user prompt using mustache templating.
  
- **Optional**:
  - `max_agent_calls` (int): Maximum number of calls the agent can make in a single conversation session. Defaults to 1 if not specified.
  - `openai_api_key`, `anthropic_api_key`, `google_api_key` (Annotated[str]): API keys used for integrating different AI services, allowing flexibility through OR operators.
  - `system_prompt` (Optional[str]): Custom system prompt to guide the agent conversation.
  - `example_json` (Optional[Dict]): Example data to guide the structure and content of API interactions.

#### Outputs

- `conversation_history` (List[Dict]): A structured log of the conversation exchanges.
- `tool_records` (List[Dict]): Records of tool usage in fulfilling user requests.
- `request_tokens` (int): Tokens utilized in the API request.
- `response_tokens` (int): Tokens consumed in the API response.

### 2. `ManageEngineAgent.py`

This file contains the implementation of the `ManageEngineAgent` class, which is responsible for setting up and executing the agentic strategy with parameters provided through the inputs.

#### How It Works

- **Initialization**: Takes a dictionary of inputs, validating that essential parameters like `me_access_token` and `user_prompt` are provided.
- **Configuration**: Sets up necessary parameters such as headers for API authentication and constructs an `AgenticStrategyV2` object. This strategy is configured with a language model client and an API request tool tailored for ManageEngine.
- **Run Method**: Executes the agentic strategy within the specified conversation limit, using the multi-turn dialogue approach to complete requested tasks and returning the result alongside usage metrics.

#### Likely Usage

The `ManageEngineAgent` would typically be integrated into service desk automation solutions where an intelligent conversational interface can enhance task efficiency. Analysts and developers can use it to automate routine service desk operations, reducing the response time and manual effort involved in managing tickets through seamless API interactions.

## Use Cases

- Automating service desk interactions using a conversational AI framework.
- Streaming API calls to manage service tickets efficiently.
- Implementing a hybrid solution that combines AI capabilities from providers like OpenAI, Anthropic, or Google with ManageEngine service desk functionalities.

This module provides a structured approach to leveraging conversational AI for service automation, optimizing both user experience and operational workflows.
