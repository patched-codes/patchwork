# Documentation for CallSQL Module

## Overview

The `CallSQL` module is a part of the Patchwork framework, designed as a step in a workflow that executes SQL queries against a specified database. This module is built using SQLAlchemy for database connection and query execution and logs activities for auditing and debugging purposes.

The primary component is the `CallSQL` class, which initializes with connection details and SQL query data, builds a suitable SQLAlchemy engine, executes the query, and returns the results.

## Inputs

To effectively utilize the `CallSQL` class, inputs should be formatted as a dictionary encompassing the following parameters:

- **Required Parameters**:
  - `db_dialect`: (str) Database dialect (e.g., `postgresql`, `mysql`).
  - `db_query`: (str) SQL query to be executed.

- **Optional Parameters**:
  - `db_driver`: (str) Specific database driver.
  - `db_username`: (str) Username for database authentication.
  - `db_password`: (str) Password for database authentication.
  - `db_host`: (str) Host address of the database, defaults to `localhost`.
  - `db_port`: (int) Port to connect to, defaults to 5432.
  - `db_database`: (str) Database name.
  - `db_params`: (dict) Additional query parameters for the database connection.
  - `db_driver_args`: (dict) Additional arguments for the database driver.
  - `db_query_template_values`: (dict) Template values for rendering the query.

## Outputs

Upon execution, the `CallSQL` class outputs a dictionary with the following structure:

- `results`: A list of dictionaries containing the rows fetched by the SQL query. Each dictionary corresponds to a row with column names as keys.

## How To Use

1. **Initialization**:
   Initialize an instance of the `CallSQL` class with the necessary inputs defined above. The SQL query can include placeholders that will be filled with `db_query_template_values`.

   ```python
   call_sql_step = CallSQL(inputs={
       "db_dialect": "postgresql",
       "db_query": "SELECT * FROM users WHERE id = {{ user_id }}",
       "db_query_template_values": {"user_id": 1}
   })
   ```

2. **Execution**:
   Call the `run()` method to execute the SQL query and receive the results.

   ```python
   results = call_sql_step.run()
   ```

3. **Handling Results**:
   The returned `results` is a dictionary where the key `results` contains a list of query result dictionaries.

   ```python
   print(results['results'])
   ```

## Additional Files

- **`__init__.py`**: An empty file indicating that the directory `patchwork/steps/CallSQL` should be treated as a package.

- **`typed.py`**: Contains the TypedDict definitions for input and output, ensuring type safety and clarity regarding what keys and value types are required.

## Notes

- The module includes robust error handling and logging, ensuring that failures in executing queries are properly captured and the status is updated.
- The use of the SQLAlchemy ORM allows the flexibility to interface with a wide variety of databases, making this module versatile and powerful for database operations within workflows.
