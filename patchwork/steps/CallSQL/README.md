# Documentation for `CallSQL` Code

## Overview

This documentation details the purpose and usage of the code files in the `patchwork/steps/CallSQL` directory. The primary focus is on the `CallSQL.py` file, which implements functionality for executing SQL queries using SQLAlchemy. This module is structured to allow dynamic query creation and safe execution via a templating approach.

## Key Features

- **Dynamic SQL Query Execution**: Through the use of placeholders and template rendering, SQL queries can be customized on-the-fly with given parameters.
- **Secure Database Connection Management**: It builds a secure, parametrized connection to the database using SQLAlchemy.
- **Error Logging**: Errors during execution are logged with clear messages.
- **Typed Inputs and Outputs**: The inputs and outputs are strongly typed using Python's `TypedDict` to ensure clear structure and expectation of data.

## Inputs

### CallSQLInputs

These are the expected inputs for the `CallSQL` Step and are defined in `typed.py`.

- **Required Inputs**
  - `db_dialect (str)`: Specifies the database dialect (e.g., `postgresql`, `mysql`).
  - `db_query (str)`: SQL query string that may include placeholders for parameterized execution.

- **Optional Inputs**
  - `db_driver (str)`: Specific driver for the database, if any.
  - `db_username (str)`: Username for database authentication.
  - `db_password (str)`: Password for database authentication.
  - `db_host (str)`: Host address of the database. Defaults to `localhost`.
  - `db_port (int)`: Port number for the database, default is 5432.
  - `db_name (str)`: Name of the database.
  - `db_params (dict[str, Any])`: Additional connection parameters.
  - `db_driver_args (dict[str, Any])`: Driver-specific connection arguments.
  - `db_query_template_values (dict[str, Any])`: Values for rendering the query template.

## Outputs

### CallSQLOutputs

This is the output format expected from the `CallSQL` Step, defined in `typed.py`.

- **results (list[dict[str, Any]])**: A list of dictionaries representing the rows returned from the executed query.

## How to Use

1. **Initialization**: Instantiate the `CallSQL` class with a dictionary matching the expected `CallSQLInputs`.
2. **Configuration**: Set necessary configuration options like database credentials, host information, and query template values.
3. **Execution**: Call the `run()` method to execute the query. The method returns a dictionary containing query results.
4. **Error Handling**: Any execution issues will result in a failed step with the error message logged.

## Example

```python
inputs = {
    "db_dialect": "postgresql",
    "db_query": "SELECT * FROM users WHERE status = '{{status}}'",
    "db_query_template_values": {"status": "active"},
    "db_username": "user",
    "db_password": "password",
    "db_host": "localhost",
    "db_port": 5432,
}

call_sql_step = CallSQL(inputs)
output = call_sql_step.run()
print(output)
```

In this example, a SQL query is dynamically formed and executed against a PostgreSQL database. The results of the query are printed to the console.
