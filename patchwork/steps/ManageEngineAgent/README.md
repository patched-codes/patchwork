# ManageEngineAgent Code Documentation

This documentation provides an overview of two files: `typed.py` and `ManageEngineAgent.py`, which are part of the `patchwork/steps/ManageEngineAgent/` module.

## File: `typed.py`

This file defines the input and output types for the ManageEngineAgent. The purpose of these classes is to specify the expected structure and types of data that can be input into, and output from, the agent.

### Inputs

- **`me_access_token`** *(str)*: A required authentication token for accessing the ManageEngine ServiceDesk API.
- **`user_prompt`** *(str)*: A required user prompt that directs the agent's actions.
- **`prompt_value`** *(Dict[str, Any])*: Additional contextual values to support the user prompt.

#### Optional Inputs

- **`max_agent_calls`** *(int)*: Defines the maximum number of API calls that the agent can make.
- **`openai_api_key`**, **`anthropic_api_key`**, **`google_api_key`** *(str)*: API keys for choosing different NLP models; optional but at least one is required.
- **`system_prompt`** *(Optional[str])*: An optional prompt to provide context for system operations.
- **`example_json`** *(Optional[Dict])*: An optional JSON structure to guide example outputs.

### Outputs

- **`conversation_history`** *(List[Dict])*: A list of previous interaction records with the ManageEngine.
- **`tool_records`** *(List[Dict])*: A list comprising records of tools used during the interaction.
- **`request_tokens`** *(int)*: The number of tokens/request units utilized.
- **`response_tokens`** *(int)*: The number of tokens/response units generated.

## File: `ManageEngineAgent.py`

This file implements the `ManageEngineAgent` class, which is designed to integrate with the ManageEngine ServiceDesk via API requests and handle interactions as per user prompts using an agentic strategy.

### Usage

This class extends a `Step` and is designed to automate interactions with ManageEngine ServiceDesk. It utilizes language models, defined in different agent configurations, to summarize conversations, handle API requests, and manage tickets. 

### Inputs

- **`inputs`** *(dict)*: Dictionary containing all the input parameters defined in the `ManageEngineAgentInputs`.

### Outputs

- Returns a dictionary that merges the agent execution results with usage information, including the number of tokens used.

### Key Functionalities

- **Initialization**: Set up authorization headers and configure conversation limits and prompts.
- **Agentic Strategy Configuration**: Leverages `AgenticStrategyV2` to handle and execute strategies with the specified `system_prompt_template` and actions within the context of ManageEngine ServiceDesk tasks.
- **Run Method**: Executes the agentic strategy and returns the execution results including token usage.

### How to Use

1. **Instantiate the ManageEngineAgent** class using a dictionary containing the required inputs; ensure that the necessary APIs tokens and prompts are provided.
2. **Call the `run` method** to execute the agent and complete tasks such as creating, modifying, or summarizing tickets in the ManageEngine ServiceDesk.

This code provides robust management and automation for organizations using ManageEngine ServiceDesk, facilitating efficient API interactions and conversation management through the use of advanced language processing models.
