# Documentation: CallSQL Python Module

This documentation provides an overview of the `CallSQL` module, detailing its purpose, inputs, and outputs. The `CallSQL` module is useful for running SQL queries against a specified database using SQLAlchemy, and can be integrated as part of data processing workflows.

## Contents

- CallSQL.py
- __init__.py
- typed.py

## File: CallSQL.py

### Overview

`CallSQL.py` contains the `CallSQL` class, which is designed to execute SQL queries using SQLAlchemy. This class inherits from the `Step` class and utilizes inputs to configure a database engine, render query templates, and execute SQL commands.

### Inputs

- **db_dialect** (str): The database dialect (e.g., 'postgresql').
- **db_driver** (optional, str): The database driver (e.g., 'psycopg2').
- **db_username** (optional, str): Username for database authentication.
- **db_password** (optional, str): Password for database authentication.
- **db_host** (optional, str): Database host address (default is 'localhost').
- **db_port** (optional, int): Port number (default is 5432).
- **db_database** (optional, str): Database name.
- **db_params** (optional, dict): Additional database connection parameters.
- **db_driver_args** (optional, dict): Additional arguments for the database driver.
- **db_query** (str): SQL query to be executed.
- **db_query_template_values** (optional, dict): Values for query templating using Mustache syntax.

### Outputs

- A dictionary with a single key, `results`, which is a list of dictionaries, each representing a row retrieved from the query execution.

### Usage

The `CallSQL` class is used for integrating database query functionalities within a larger Python application. It initializes the necessary database engine using input parameters, renders query templates, and executes the formulated SQL query. Results are logged and returned to the caller.

## File: __init__.py

### Overview

The `__init__.py` file is currently empty and serves as a placeholder to indicate that the `CallSQL` directory is a Python package.

## File: typed.py

### Overview

`typed.py` defines the `CallSQLInputs` and `CallSQLOutputs` typed dictionaries. These are used to specify the expected structure and data types of inputs and outputs for the `CallSQL` class.

### Inputs (Defined in CallSQLInputs)

- Mandatory fields: `db_dialect`, `db_query`
- Optional fields: Various configurations for database connection parameters and query templating.

### Outputs (Defined in CallSQLOutputs)

- **results** (list[dict[str, Any]]): Execution results of the SQL query as a list of dictionaries.

### Usage

`typed.py` provides a structured approach to defining input and output contracts for the `CallSQL` class. It improves the readability and maintainability of code that interacts with SQL databases by detailing required inputs and expected outputs.
