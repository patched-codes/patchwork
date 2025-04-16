# Documentation: DatabaseAgent Module

## Overview

The `DatabaseAgent` module is designed to facilitate interaction with a database by generating and executing appropriate SQL queries. It uses machine learning to understand and interpret user tasks and generates an execution plan to gather and process necessary data from a database using the specified database dialect (e.g., SQL).

The main functionality is encapsulated within a class called `DatabaseAgent`, which leverages the `AgenticStrategyV2` to dynamically generate responses to user tasks. This agent uses the `AioLlmClient` and `DatabaseQueryTool` to perform its operations, geared towards summarizing conversations and fetching data based on user prompts.

## Inputs

### DatabaseAgent Inputs Class

In the file `typed.py`, the `DatabaseAgentInputs` class defines the input structure that the `DatabaseAgent` expects:

- **task (str):** A string describing the task that needs completion.
- **db_dialect (str):** Specifies the type of SQL dialect the database uses (e.g., MySQL, PostgreSQL).
- **db_driver (str):** The database driver used for connections.
- **db_username (str):** Username for database authentication.
- **db_password (str):** Password for database authentication.
- **db_host (str):** Host address of the database.
- **db_port (int):** Port number for database connection.
- **db_name (str):** Name of the database.
- **db_params (dict):** Additional connection parameters.
- **db_driver_args (dict):** Additional driver-specific arguments.
- **prompt_value (Dict[str, Any]):** Dictionary holding values for prompt customization.
- **max_llm_calls (int):** Configures the maximum number of large language model calls.
- **openai_api_key (str):** API key for OpenAI services.
- **anthropic_api_key (str):** API key for Anthropic services.
- **google_api_key (str):** API key for Google services.
- **example_json (str):** A JSON example to guide response structure.

## Outputs

### DatabaseAgent Outputs Class

Within `typed.py`, the `DatabaseAgentOutputs` class is introduced to outline the expected output format:

- **request_tokens (int):** Number of tokens used in the request.
- **response_tokens (int):** Number of tokens received in the response.

## DatabaseAgent Implementation

### Core Functionality

In `DatabaseAgent.py`, the `DatabaseAgent` class derives from the `Step` class and uses both `DatabaseAgentInputs` and `DatabaseAgentOutputs`. The class:

- Initializes an agentic strategy to process user-provided tasks and database information.
- Sets up database query configurations through the `DatabaseQueryTool`.
- Employs the `mustache_render` utility to tailor command-line interactions and strategy prompts.
- Executes the task, restricting output operation to a maximum of ten results (`limit=10`).

### `run` Method

The `run` function executes the agent's strategy to fetch requested data and append execution usage metrics from the `AgenticStrategyV2`.

By employing this module, users can expect an automated task execution environment, where high-level natural language prompts can seamlessly translate into concrete database operations. This setup is particularly useful for data analysis and management tasks that require flexible and interactive database querying capabilities.
