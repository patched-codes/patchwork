# DatabaseAgent Module Documentation

This document provides an overview of the `DatabaseAgent` module found within the `patchwork.steps.DatabaseAgent` package, which is designed to assist in generating database queries based on inputs provided by the user. The module integrates AI-driven strategies to assist users in interacting with databases efficiently.

## Overview

The `DatabaseAgent` module provides a framework to create, manage, and execute database queries with the help of AI-driven strategies. This is particularly useful for users who need to interact with databases but may not be proficient in writing complex queries themselves.

## Components

The module comprises three main files:
- `DatabaseAgent.py`: Contains the core logic and implementation of the `DatabaseAgent` class.
- `typed.py`: Defines the typing and input/output structures used by `DatabaseAgent`.
- `__init__.py`: Initializes the `DatabaseAgent` package.

## Files and Their Purpose

### 1. DatabaseAgent.py

This file defines the `DatabaseAgent` class, which extends the `Step` class, and handles the setup and execution of database queries using AI strategies.

#### Inputs

The `DatabaseAgent` class requires several inputs, encapsulated within the `DatabaseAgentInputs` class. Notable inputs include:

- **task**: A string defining the task or query to be executed.
- **db_dialect**: The database dialect (e.g., SQL).
- **db connection details**: Includes parameters like `db_host`, `db_port`, `db_username`, `db_password`, etc.
- **max_llm_calls**: Maximum allowed calls to the large language model.
- **API keys**: For various service integrations (`openai_api_key`, `anthropic_api_key`, `google_api_key`).
- **prompt_value**: Additional data for query construction.
- **example_json** (optional): Example JSON structure for expected outputs.

#### Outputs

The execution results are provided through a dictionary which includes:
- **request_tokens**: Number of tokens used in the request.
- **response_tokens**: Number of tokens in the response.

### 2. typed.py

This file defines structured types to be used for the inputs and outputs of the `DatabaseAgent`:

- **DatabaseAgentInputs**: Typed dictionary for input parameters, including API keys and configuration details.
- **DatabaseAgentOutputs**: Typed dictionary for the results returned by the `DatabaseAgent`.

### 3. __init__.py

This file serves as the initializer for the `DatabaseAgent` package, ensuring module recognition within the package structure.

## Usage

The `DatabaseAgent` is designed to be instantiated with relevant inputs and executed to perform database queries with AI assistance. Users can incorporate this module in automation scripts where database interactions are needed, leveraging AI to simplify query generation and execution.

```python
from patchwork.steps.DatabaseAgent import DatabaseAgent
from patchwork.steps.DatabaseAgent.typed import DatabaseAgentInputs

inputs = DatabaseAgentInputs(
    task="Select all records from the sales table",
    db_dialect="SQL",
    db_username="user",
    db_password="password",
    db_host="localhost",
    db_name="database"
)

agent = DatabaseAgent(inputs)
result = agent.run()
print(result)
```

The code above exemplifies the setup and usage of `DatabaseAgent` in a Python script, showcasing its integration simplicity and utility in database management tasks.
