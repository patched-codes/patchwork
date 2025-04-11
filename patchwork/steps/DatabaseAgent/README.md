# DatabaseAgent Module Documentation

This documentation provides an overview of the `DatabaseAgent` module within the Patchwork project. The module is designed to facilitate database query execution using an agentic strategy enhanced by language model clients. It consists of several Python files, each serving different purposes.

## Overview

The `DatabaseAgent` module is aimed at assisting users in executing database queries by providing a structured strategy involving language models. This module can be particularly useful for individuals needing to automate the retrieval and processing of data from databases using natural language interfaces.

## File: DatabaseAgent.py

### Description

The primary file responsible for defining the `DatabaseAgent` class, which integrates agentic strategy and language models to facilitate database interactions. It defines the core logic and operation of the agent.

### Inputs

- **prompt_value**: Dictionary containing data used for rendering task templates.
- **task**: A string representing the specific task or query to be performed.
- **db_dialect**: Specifies the type of SQL dialect for the database (e.g., PostgreSQL, MySQL).
- **example_json**: (Optional) String representation of example JSON data for input guidance.

### Class: DatabaseAgent

- **Initialization**: Sets up the agent configuration using provided inputs, renders the task, and initializes an agentic strategy with language models and a database query tool.
  
- **Method: run()**: Executes the agentic strategy up to a specified limit (default is 10 executions), returning results combined with usage statistics.

### Outputs

- A dictionary containing execution results and usage statistics, notably:
  - **request_tokens**: Number of tokens used for the request.
  - **response_tokens**: Number of tokens used in the response.

## File: typed.py

### Description

This file defines the typed inputs and outputs for the `DatabaseAgent`, encapsulating the data requirements and configurations necessary for its operation.

### Inputs

- **task**: The task to perform, expressed as a string.
- **db_dialect**: SQL dialect to be used.
- **db_driver**: Name of the database driver.
- **db_username**: Database username for authentication.
- **db_password**: Password for database authentication.
- **db_host**: Host address of the database server.
- **db_port**: Port number on which the database server is listening.
- **db_name**: Name of the database to connect to.
- **db_params**: Additional connection parameters as a dictionary.
- **db_driver_args**: Driver-specific arguments as a dictionary.
- **max_llm_calls**: Maximum language model calls (annotated for configuration).
- **openai_api_key**: API key for OpenAI services.
- **anthropic_api_key**: API key for Anthropic services.
- **google_api_key**: API key for Google services.
- **prompt_value**: Data used for dynamically populating templates.
- **example_json**: Example JSON input for processing (as a string).

### Outputs

- **request_tokens**: Tokens used for the initial request.
- **response_tokens**: Tokens generated in response from the language model.

## File: __init__.py

### Description

An initialization file for the `DatabaseAgent` module. It is empty, serving as a marker for Python module initialization.

## Usage

This module is typically utilized in contexts where users need to seamlessly query and retrieve data from databases using language models. It abstracts the complexity of database interactions and leverages natural language processing to enhance user experience and efficiency.
