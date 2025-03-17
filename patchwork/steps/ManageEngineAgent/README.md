# Documentation for ManageEngineAgent Module

This module provides the functionality to interact with the ManageEngine ServiceDesk through a specialized agent class, enabling operations such as retrieving, creating, or modifying service desk tickets. It leverages the `AgenticStrategyV2` for multi-turn conversational capabilities and requires valid API tokens for operation.

## File: `typed.py`

### Description

This file defines the input and output types for the `ManageEngineAgent`. It uses `TypedDict` to structure the required and optional fields for inputs, ensuring type safety and clarity in the input structure.

### Inputs

- **zoho_access_token** (`str`): Required. The API token for authenticating with Zoho's ManageEngine.
- **user_prompt** (`str`): Required. The prompt provided by the user for the agent to process.
- **prompt_value** (`Dict[str, Any]`): Required. Contains values to be used in prompt generation.
- **max_agent_calls** (`int`): Optional. Limits the number of agent calls in a conversation.
- **openai_api_key** (`str`): Optional. API Key for OpenAI, used in conjunction with other API keys.
- **anthropic_api_key** (`str`): Optional. Anthropic's API Key.
- **google_api_key** (`str`): Optional. Google API Key.
- **system_prompt** (`Optional[str]`): Configures the system prompt for the agent.
- **example_json** (`Optional[Dict]`): Provides example JSON for responses.

### Outputs

- **conversation_history** (`List[Dict]`): A record of the conversation history within a session.
- **tool_records** (`List[Dict]`): Logs of tool usage in the course of the conversation.
- **request_tokens** (`int`): Count of tokens used in requests.
- **response_tokens** (`int`): Count of tokens used in responses.

---

## File: `ManageEngineAgent.py`

### Description

This file contains the implementation of the `ManageEngineAgent` class, which extends the `Step` class and is structured to take specified inputs and produce structured outputs. It performs operations by interacting with the ManageEngine API using a configured conversation strategy.

### Inputs

- All inputs from `ManageEngineAgentInputs` as specified in `typed.py`.

### Outputs

- The outputs defined in `ManageEngineAgentOutputs`.

### Class: `ManageEngineAgent`

This class sets up a conversational agent tailored for interacting with the ManageEngine ServiceDesk API.

#### Initialization

- The class is initialized with a dictionary containing the required inputs.
- Checks are implemented to ensure the presence of mandatory fields like `zoho_access_token` and `user_prompt`.

#### Key Attributes

- **conversation_limit**: Limits the number of interactions per session.
- **headers**: Prepares the headers using the Zoho API token for API requests.
- **agentic_strategy**: Configured to handle conversational tasks using specified models and API tools.

#### Method: `run`

- Executes the agentic strategy to perform tasks as instructed by the conversation's input details.
- Returns a dictionary containing the results of the operations and additional usage data.

### Usage

This module is used to automate interactions with the ManageEngine ServiceDesk, making it valuable for IT teams seeking to streamline ticket management via API. It requires configuration with API keys and is capable of executing complex, multi-turn conversations with integrated API interactions. It can be extended or adjusted to integrate with different models or strategies as required by the user's deployment scenario.
