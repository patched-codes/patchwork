# ManageEngine Agent Code Documentation

## Overview

This codebase provides functionalities for interacting with ManageEngine ServiceDesk using an agentic strategy. It is structured into two primary files: `typed.py` and `ManageEngineAgent.py`. These files define the inputs and outputs for the ManageEngine agent and outline the implementation logic for handling API requests to the ManageEngine ServiceDesk via a step-based framework.

## File: typed.py

### Inputs

The `ManageEngineAgentInputs` class defines the necessary inputs for the ManageEngine agent:

- **zoho_access_token** (*str*): A required Zoho access token for authentication.
- **user_prompt** (*str*): A required user prompt that dictates the aim of the interaction.
- **prompt_value** (*Dict[str, Any]*): A dictionary containing additional data or variables needed for the execution.
- **max_agent_calls** (*int*, optional): The maximum number of API calls the agent can make.
- **openai_api_key** (*Annotated[str]*, optional): OpenAI API key with alternatives allowed (Google or Anthropic API Keys).
- **anthropic_api_key** (*Annotated[str]*, optional): Anthropic API key with alternatives allowed.
- **google_api_key** (*Annotated[str]*, optional): Google API key with alternatives allowed.
- **system_prompt** (*Optional[str]*): An optional system-level prompt for directing the agent's conversation style.
- **example_json** (*Optional[Dict]*): An optional example JSON structure for guiding responses.

### Outputs

The `ManageEngineAgentOutputs` class defines the outputs returned by the ManageEngine agent:

- **conversation_history** (*List[Dict]*): A history of the conversation steps.
- **tool_records** (*List[Dict]*): Recorded activities of tools used during execution.
- **request_tokens** (*int*): Count of tokens used in requests.
- **response_tokens** (*int*): Count of tokens received in responses.

## File: ManageEngineAgent.py

### Inputs

The `ManageEngineAgent` class processes the following inputs:

- A dictionary containing the keys defined in `ManageEngineAgentInputs`.

### Outputs

The output of the `ManageEngineAgent` run method is a dictionary consisting of:

- The results of the agentic strategy execution.
- Usage data, including token counts and execution steps.

### Functionality

The `ManageEngineAgent` class is designed to perform the following operations:

1. **Initialization**: 
   - Validates presence of necessary inputs like `zoho_access_token` and `user_prompt`.
   - Configures conversation limits and initializes system-level prompts.

2. **Agent Configuration**:
   - Sets up headers for API requests using the provided `zoho_access_token`.
   - Constructs an `AioLlmClient` to facilitate language model interactions.
   - Defines and configures an `AgenticStrategyV2` using a model tailored for ManageEngine ServiceDesk interactions.
   - Establishes a toolset (e.g., `make_api_request`) for making API requests to ManageEngine APIs.

3. **Execution**:
   - Executes the configured strategy, limited by `max_agent_calls`.
   - Returns the results including conversation data and resource utilization metrics.

### Use Cases

This code is particularly useful for developers or system administrators who need to automate interactions with the ManageEngine ServiceDesk. By configuring the agent with appropriate APIs and prompts, users can programmatically manage and operate on service desk tickets and related data, all while capturing conversation and resource usage statistics.

## Conclusion

The ManageEngine Agent provides a robust framework for integrating conversational strategies with ManageEngine ServiceDesk capabilities, allowing for flexible API operations and interaction tracking in automated workflows.
