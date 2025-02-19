# CallSQL Module Documentation

This documentation outlines the structure and functionality of the `CallSQL` module, which is part of the Patchwork pipeline system. Its primary function is to execute SQL queries against a specified database using SQLAlchemy.

## Overview

The `CallSQL` module is designed to facilitate running SQL queries with dynamic input parameters. This is beneficial for applications that require querying databases with customizable query templates.

## Files in the Module

### 1. `CallSQL.py`

#### Description

The main implementation file for the `CallSQL` class. It defines the constructor to initialize the database connection and the `run` method to execute the queries.

#### Class: `CallSQL`

The class `CallSQL` inherits from `Step` and uses `CallSQLInputs` and `CallSQLOutputs` types for input and output validation, respectively.

##### Methods

- **`__init__(inputs: dict)`**: 
  - Initializes the SQL query from the provided template using mustache rendering.
  - Constructs a database engine using connection parameters.

- **`__build_engine(inputs: dict) -> None`**: 
  - Constructs a SQLAlchemy engine connecting to the specified database. 
  - Validates the connection by executing a simple query.

- **`run() -> dict`**: 
  - Executes the specified SQL query.
  - Returns the results as a list of dictionaries, or an empty list if an error occurs.

#### Inputs

To create a valid `CallSQL` object, the following input keys are expected:

- `db_dialect`: The type of SQL dialect to use (e.g., `postgresql`, `mysql`).
- `db_query`: The SQL query to execute, potentially containing mustache-style placeholders.
  
Optional inputs include:
- `db_driver`, `db_username`, `db_password`, `db_host`, `db_port`, `db_name`, `db_params`, `db_driver_args`, `db_query_template_values`.

#### Outputs

- Returns a dictionary with a key `results` containing a list of dictionaries, each representing a row from the query results.

### 2. `__init__.py`

An empty file which allows Python to treat the `CallSQL` directory as a package. This allows the contained modules and classes to be imported.

### 3. `typed.py`

#### Description

Contains typed dictionaries used to define the expected inputs and outputs for the `CallSQL` class in a structured manner.

#### Classes

- **`CallSQLInputs`**: 
  - Defines required fields (`db_dialect`, `db_query`) and optional fields for creating a `CallSQL` instance.

- **`CallSQLOutputs`**: 
  - Defines the expected structure of the results, which is a list of dictionaries.

## Usage

To use the `CallSQL` module, instantiate the `CallSQL` class with appropriate input parameters and call the `run` method to execute the query. The results can be retrieved and used as desired in the application. This modular approach can be particularly useful in data pipeline applications where dynamically generated SQL queries need to interact with different databases.
