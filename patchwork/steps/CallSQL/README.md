# `CallSQL` Module Documentation

## Overview

The `CallSQL` module is a part of the `patchwork` package designed to execute SQL queries on a specified database using the SQLAlchemy library. It consists of three Python files:

- **CallSQL.py**: Core implementation of the `CallSQL` step for running SQL queries.
- **__init__.py**: Module initializer.
- **typed.py**: Definitions of input and output types for typing and validation.

This module is intended for developers who need to integrate SQL data retrieval tasks in Python applications.

## Components

### CallSQL.py

This file contains the main logic for executing SQL queries. The `CallSQL` class inherits from `Step`, facilitating the modular design of processes. It utilizes SQLAlchemy for managing database connections and executing queries. Error handling is incorporated to manage query failures gracefully.

#### Inputs

The `CallSQL` class requires certain inputs to establish a connection and execute a query. These inputs are passed as a dictionary and parsed through the `CallSQLInputs` class:

- `db_dialect`: **Required**. The database dialect (e.g., `postgresql`, `mysql`).
- `db_query`: **Required**. The SQL query to execute.
- `db_driver`: The database driver (e.g., `psycopg2` for PostgreSQL).
- `db_username`: Username for database authentication.
- `db_password`: Password for database authentication.
- `db_host`: Host address of the database. Defaults to `localhost`.
- `db_port`: Port number for the database connection. Defaults to `5432`.
- `db_name`: Name of the database to connect to.
- `db_params`: Additional parameters for the database connection.
- `db_driver_args`: Arguments specific to the database driver.
- `db_query_template_values`: Values for templating within the query.

#### Outputs

The output is defined by the `CallSQLOutputs` class and is a dictionary containing:

- `results`: A list of dictionaries, each representing a row in the query result set.

### __init__.py

This is an empty file serving as the package initializer, allowing the `CallSQL` logic to be imported as a module.

### typed.py

This file provides detailed type definitions using Python's `TypedDict`. It defines `CallSQLInputs` and `CallSQLOutputs` types, specifying required and optional fields for SQL task execution.

## Usage

To use the `CallSQL` step, you need to create an instance of the `CallSQL` class with appropriate inputs and call the `run` method to execute the given SQL query. This step is ideal for integrating SQL command execution in a larger workflow managed by the `patchwork` framework.

Here's an example snippet for usage:

```python
from patchwork.steps.CallSQL.CallSQL import CallSQL

inputs = {
    "db_dialect": "postgresql",
    "db_driver": "psycopg2",
    "db_query": "SELECT * FROM users WHERE active = :active",
    "db_query_template_values": {"active": True},
    "db_username": "user",
    "db_password": "password",
    "db_host": "localhost",
    "db_port": 5432,
}

call_sql_step = CallSQL(inputs)
results = call_sql_step.run()
print(results)
```

This module effectively handles database querying, making it a valuable tool for developers dealing with database operations in Python.
