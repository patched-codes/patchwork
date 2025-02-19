# CallSQL Module Documentation

This documentation provides an overview of the `CallSQL` module, designed for performing SQL operations using Python's SQLAlchemy library within the Patchwork framework.

## Overview

The `CallSQL` module is primarily implemented in the `CallSQL.py` file and provides a structured way to perform SQL queries. It uses the SQLAlchemy framework to manage database connections and execute SQL commands.

## Files

### CallSQL.py

This is the main implementation file for the `CallSQL` module.

#### Inputs

- **db_dialect (str)**: The database dialect to be used (e.g., `postgresql`).
- **db_driver (str, optional)**: The database driver if needed (e.g., `psycopg2`).
- **db_username (str, optional)**: Username for database authentication.
- **db_password (str, optional)**: Password for database authentication.
- **db_host (str, optional)**: Database host name, default is `"localhost"`.
- **db_port (int, optional)**: Port to connect to the database, default is `5432`.
- **db_database (str, optional)**: Name of the database.
- **db_params (dict, optional)**: Additional query parameters for the connection.
- **db_driver_args (dict, optional)**: Additional driver-specific arguments.
- **db_query (str)**: The SQL query to be executed.
- **db_query_template_values (dict, optional)**: Template values to render dynamic parts of the SQL query.

#### Outputs

- **results (list[dict])**: The query returns a list of dictionary objects representing rows from the database.

#### Functionality

1. **Initialization**: Sets up the SQLAlchemy engine using provided inputs, formats the SQL query, and prepares for execution.

2. **Build Engine**: Establishes the connection to the database with proper URL formation and checks connectivity.

3. **Run Method**: Executes the SQL query and returns the results. In case of query failure, it logs the error and returns an empty list.

### __init__.py

This file is intended for module initialization but is currently empty, serving no specific purpose in its current state.

### typed.py

Contains input and output type definitions using TypedDict for structured data handling.

#### Classes

- **CallSQLInputs**: Specifies the expected input schema with required and optional fields for configuring the SQL call.
  
- **CallSQLOutputs**: Defines the structure of the output, which is a list of dictionaries where each dictionary represents a row from the query result.

## Usage

The `CallSQL` module is useful for developers needing to run SQL queries programmatically within a Python environment, leveraging the flexible and powerful SQLAlchemy. The module can be used in data processing pipelines where integration with databases is required.

### Example

To use this module:

1. Prepare a dictionary with database connection details and the SQL query.
2. Create an instance of `CallSQL` with these inputs.
3. Call the `run` method to execute the query and receive results.

This module abstracts the complexities of database connections and query execution, facilitating easier data retrieval within the broader Patchwork framework.
