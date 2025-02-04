# Documentation: CallSQL Module

## Overview

The `CallSQL` module is designed to execute SQL queries against a specified database using SQLAlchemy. It allows users to define their SQL query and database connection parameters through inputs. The `CallSQL` class manages the connection to the database and execution of the query, returning the results as a dictionary.

## File Structure

- **CallSQL.py**: Main implementation of the `CallSQL` class.
- **__init__.py**: Empty initialization file for the module.
- **typed.py**: Contains the typed dictionary classes defining the inputs and outputs for the `CallSQL` class.

## CallSQL Class

### Inputs

The `CallSQL` class requires a set of inputs to execute SQL queries. These are encapsulated within `CallSQLInputs`, which extends `TypedDict`. Important input fields include:

- **db_dialect**: `str` - Required. SQL database dialect (e.g., 'postgresql', 'mysql').
- **db_query**: `str` - Required. SQL query to be executed.
- **db_driver**: `str` - Optional. Database driver to use.
- **db_username**: `str` - Optional. Username for database authentication.
- **db_password**: `str` - Optional. Password for database authentication.
- **db_host**: `str` - Optional. Database host, default is 'localhost'.
- **db_port**: `int` - Optional. Port number, default is 5432.
- **db_name**: `str` - Optional. Name of the database.
- **db_params**: `dict[str, Any]` - Optional. Additional parameters for the connection URL.
- **db_driver_args**: `dict[str, Any]` - Optional. Additional driver-specific arguments.
- **db_query_template_values**: `dict[str, Any]` - Optional. Template values for rendering the query using the Mustache syntax.

### Outputs

Upon execution, `CallSQL` provides outputs encapsulated in `CallSQLOutputs`, which includes:

- **results**: `list[dict[str, Any]]` - A list of dictionaries where each dictionary represents a row from the query results.

### Usage 

To use the `CallSQL` class, instantiate it with a dictionary of input parameters conforming to the `CallSQLInputs` structure. Then, call the `run()` method to execute the query and obtain the results.

```python
inputs = {
    "db_dialect": "postgresql",
    "db_query": "SELECT * FROM users WHERE age > {{ min_age }}",
    "db_username": "admin",
    "db_password": "password123",
    "db_query_template_values": {"min_age": 21}
}

call_sql_step = CallSQL(inputs)
results = call_sql_step.run()
print(results)
```

## Error Handling

If an SQL execution fails due to a request error, the `CallSQL` class will log the failure and report it through the `StepStatus` mechanism. It will return an empty result set in such cases. 

By utilizing this modular design, the `CallSQL` class offers flexibility and ease of use for executing dynamic SQL queries across different database backends.
