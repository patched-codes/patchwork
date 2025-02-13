# Documentation for CallSQL Module

The `CallSQL` module is designed to execute SQL queries using SQLAlchemy within a data pipeline framework. This module facilitates the connection to a database, execution of SQL queries, and retrieval of results in a structured format. 

## Components Overview

- **CallSQL.py**: Contains the main logic for connecting to a database, executing SQL queries, and returning results.
- **typed.py**: Defines the input and output types used by the `CallSQL` class for better type safety and readability.
- **__init__.py**: Initializes the package; currently, it is an empty file.

## File: CallSQL.py

### Inputs

The `CallSQL` class takes a dictionary of inputs, which is processed to connect to the database and execute the specified query. The key inputs include:

- `db_dialect`: The database dialect (e.g., 'postgresql', 'mysql') (required).
- `db_driver`: The database driver (optional).
- `db_username`: The database username (optional).
- `db_password`: The password for authentication (optional).
- `db_host`: The database server host (default 'localhost').
- `db_port`: The port number (default 5432).
- `db_name`: The name of the database (optional).
- `db_params`: Additional parameters for the database connection (optional).
- `db_driver_args`: Driver-specific arguments (optional).
- `db_query`: The SQL query string to be executed (required).
- `db_query_template_values`: Values to render into the query template (optional).

### Outputs

The `run` method returns a dictionary with the results of the executed SQL query:

- `results`: A list of dictionaries, where each dictionary represents a row in the result set.

### Functionality

- **Connection Initialization**: Builds a SQLAlchemy engine using the provided database credentials and connection details.
- **Query Execution**: The SQL query is prepared using a template rendering function (mustache), executed, and results are fetched.
- **Error Handling**: Captures and logs SQL execution errors, marking the step status as FAILED if necessary.

## File: typed.py

### Purpose

Defines TypedDict classes for strongly-typed inputs and outputs, ensuring that the data passed to and from the `CallSQL` class conforms to expected structures.

### Definitions

- **CallSQLInputs**: Includes all possible input parameters with required fields `db_dialect` and `db_query`.
- **CallSQLOutputs**: Defines the expected output format, primarily the query results list.

## Usage

To utilize the `CallSQL` module in a data pipeline:

1. **Instantiate** the `CallSQL` class with appropriate inputs.
2. **Invoke** the `run` method to execute the query and retrieve results.

The module is suitable for users familiar with SQL, who need to integrate database interactions into larger data processing workflows. It leverages SQLAlchemy for broad database compatibility and efficient query handling.
