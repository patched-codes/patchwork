# CallSQL Documentation

The provided code relates to a module that facilitates SQL interactions using Python, primarily with the help of SQLAlchemy. Here, the CallSQL step is intended for executing SQL queries, retrieving results, and handling database connections dynamically. This document outlines the key components of the code, highlighting inputs, outputs, and functionality.

## Overview

The module defines a class `CallSQL` that executes SQL queries against a database and retrieves the results. This functionality is encapsulated into a step presumably used in a larger data processing pipeline.

## Inputs

### Required Inputs

The following inputs are necessary for executing a SQL query:

- `db_dialect` (str): Specifies the SQL dialect to be used (e.g., `postgresql`, `mysql`).
- `db_query` (str): The SQL query string to execute.

### Optional Inputs

These inputs provide additional connection and query customization:

- `db_driver` (str): Specifies the database driver.
- `db_username` (str): Username for database authentication.
- `db_password` (str): Password for the given username.
- `db_host` (str): Hostname of the database server. Defaults to `localhost`.
- `db_port` (int): Port number on which the database server is listening. Defaults to `5432`.
- `db_name` (str): Name of the database to connect to.
- `db_params` (dict[str, Any]): Additional parameters for the database connection.
- `db_driver_args` (dict[str, Any]): Driver-specific arguments to pass to the database connection.
- `db_query_template_values` (dict[str, Any]): Values to render into the SQL query string using a templating mechanism.

## Outputs

### CallSQLOutputs

The outputs from the `CallSQL` class execution are structured as follows:

- `results` (list[dict[str, Any]]): A list of dictionaries, where each dictionary represents a row resulting from the SQL query. Each key-value pair corresponds to a column and its respective value.

## Usage

### Initialization

To employ the `CallSQL` class, instantiate it with a dictionary containing the necessary inputs. The inputs dictate database connection details and the query to be executed.

### Running a Query

Once initialized, the `run()` method should be called to execute the prepared SQL query. This method will establish a connection to the database, execute the query, and return the results.

```python
# Example Usage
inputs = {
    "db_dialect": "postgresql",
    "db_query": "SELECT * FROM users WHERE age > {{ min_age }}",
    "db_username": "user",
    "db_password": "password",
    "db_host": "my.db.host",
    "db_query_template_values": {"min_age": 18},
}

call_sql = CallSQL(inputs)
results = call_sql.run()
```

### Error Handling

If the query execution encounters an error, it will set the step's status to failed and log the error message.

This modular approach allows flexible integration into larger systems that require efficient data handling and operations based on SQL databases, leveraging Python's power and adaptability.
