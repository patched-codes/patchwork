# Documentation for SQL Call Utility

This documentation provides an overview of the code developed for executing SQL queries using a structured approach. The code is designed to interface with databases using SQLAlchemy and can handle a variety of connection inputs.

## Overview

The provided code consists of three main files:

1. **typed.py**: Defines the input and output types for the SQL connection and execution.
2. **__init__.py**: An empty initializer for the module.
3. **CallSQL.py**: Implements the main functionalities to execute SQL queries using the provided inputs.

## Code Details

### File 1: typed.py

#### Inputs

The `typed.py` file defines structured input and output classes using `TypedDict` from Python's typing module.

- **CallSQLInputs**:
  - **Required**:
    - `db_dialect`: The database dialect (e.g., 'postgresql').
    - `db_query`: The SQL query string to execute.
  - **Optional**:
    - `db_driver`: The specific database driver to use.
    - `db_username`: Username for database authentication.
    - `db_password`: Password for database authentication.
    - `db_host`: Host where the database is running.
    - `db_port`: Port where the database is accepting connections.
    - `db_name`: Name of the database to connect to.
    - `db_params`: Additional connection parameters.
    - `db_driver_args`: Additional driver-specific arguments.
    - `db_query_template_values`: Template values for rendering the query.

#### Outputs

- **CallSQLOutputs**:
  - `results`: A list of dictionaries containing the rows returned by the executed query.

### File 2: __init__.py

The `__init__.py` file is currently empty and serves as a placeholder to initialize the SQL Call module.

### File 3: CallSQL.py

The `CallSQL.py` file contains the main logic for executing SQL queries.

#### Key Classes and Functions

- **CallSQL Class**: Inherits from a hypothetical `Step` class, setup to handle inputs and outputs as defined by `CallSQLInputs` and `CallSQLOutputs`.

  - **Initialization**: Responsible for preparing the SQL query using provided template values and building the connection engine based on the input parameters.

  - **__build_engine**: Constructs a SQLAlchemy `Engine` object for connecting to the specified database. Supports various configurations via connection arguments.

  - **run Method**: Executes the SQL query using the connection engine and returns the results as a list of dictionaries. Handles exceptions that may arise during query execution, logging the error messages.

#### Usage

A user should instantiate the `CallSQL` class with required inputs to execute a SQL query and retrieve results from a database. This is particularly useful in scenarios where database operations are a part of a larger automated workflow, such as data pipelines.

### Logging and Error Handling

The implementation uses a logger to provide feedback, particularly on the number of rows retrieved. Error handling is incorporated to manage invalid queries and connection issues by catching SQLAlchemy-specific exceptions.

This package is primarily intended for those needing to seamlessly integrate SQL query execution within a Python-based project, leveraging input configurations for flexible database connectivity.
