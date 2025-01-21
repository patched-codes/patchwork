# Documentation: CallSQL Module

## Overview

The `CallSQL` module is a component of the `patchwork` library designed to facilitate the execution of SQL queries against a database using SQLAlchemy. It includes functionality for establishing a database connection, executing a specified query, and returning the results as structured data.

## Files in the Module

1. **`typed.py`**: Defines the inputs and outputs schema using `TypedDict` to ensure type safety.
2. **`__init__.py`**: Empty initialization file for the package.
3. **`CallSQL.py`**: Implements the main functionality to execute SQL queries.

## File: `typed.py`

### Inputs

- **`CallSQLInputs`**: A `TypedDict` class used to define possible input parameters for the SQL call.
  - **Required:**
    - `db_dialect`: (str) Database dialect.
    - `db_query`: (str) The SQL query to be executed.
  - **Optional:**
    - `db_driver`: (str) Database driver.
    - `db_username`: (str) Username for database login.
    - `db_password`: (str) Password for the user.
    - `db_host`: (str) Database host address.
    - `db_port`: (int) Port for the database connection.
    - `db_name`: (str) Name of the database.
    - `db_params`: (dict) Additional query parameters.
    - `db_driver_args`: (dict) Arguments for the database driver.
    - `db_query_template_values`: (dict) Values for rendering the query if templating is used.

### Outputs

- **`CallSQLOutputs`**: A `TypedDict` class defining the structure of output.
  - `results`: (list of dict) List containing the resulting rows from the query execution.

## File: `CallSQL.py`

### Class: `CallSQL`

The core class responsible for setting up a database connection and executing an SQL query.

#### Methods

- **`__init__(self, inputs: dict)`**: Initializes the class with input parameters, processes query template values, and builds the database connection engine.
  
- **`__build_engine(self, inputs: dict)`**: Constructs the SQLAlchemy engine used to connect to the specified database using parameters provided in the input.
  
- **`run(self) -> dict`**: Executes the query and returns the results. Handles exceptions during query execution and returns an empty list if an error occurs.

### Usage

This module is likely used to integrate with a database from another application or within workflows requiring database interaction. Users must provide adequate configuration in `CallSQLInputs`, ensuring proper SQL rendering and connection establishment, to retrieve results using the `run()` method.

### Example

```python
from patchwork.steps.CallSQL.CallSQL import CallSQL

# Define input parameters
inputs = {
    "db_dialect": "postgresql",
    "db_driver": "psycopg2",
    "db_username": "user",
    "db_password": "password",
    "db_host": "localhost",
    "db_port": 5432,
    "db_name": "mydatabase",
    "db_query": "SELECT * FROM my_table"
}

# Create CallSQL instance
sql_step = CallSQL(inputs)

# Execute the query
results = sql_step.run()
print(results)  # Outputs the results of the query
```

This example demonstrates how to set up an `CallSQL` instance and execute a SQL query fetching data from a PostgreSQL database.
