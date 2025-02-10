# CallSQL Module Documentation

## Overview

The `CallSQL` module is designed to facilitate SQL database interactions using a configurable and extendable approach. It is implemented as a step in a broader workflow system, leveraging SQLAlchemy for database connections and query execution. This module is structured across three files: `CallSQL.py`, `__init__.py`, and `typed.py`.

## Components

### 1. `CallSQL.py`

This file contains the primary logic for setting up a database connection and executing SQL queries. It defines the `CallSQL` class, which extends a `Step` class, indicating its role as a component in a larger workflow system.

#### Inputs

The `CallSQL` class expects input data in the form of a dictionary with various parameters to configure the database connection and the SQL query. 

- **db_dialect (str):** The database dialect (e.g., 'postgresql').
- **db_query (str):** The SQL query to execute.
- **db_driver (str, optional):** The database driver (e.g., 'psycopg2' for PostgreSQL).
- **db_username (str, optional):** Username for database authentication.
- **db_password (str, optional):** Password for database authentication.
- **db_host (str, optional):** Host where the database is running. Defaults to 'localhost'.
- **db_port (int, optional):** Port on which the database is running. Defaults to 5432.
- **db_name (str, optional):** The database name.
- **db_params (dict, optional):** Additional parameters for the database connection.
- **db_driver_args (dict, optional):** Arguments specific to the database driver.
- **db_query_template_values (dict, optional):** Values to render into the `db_query`.

#### Outputs

The `run` method returns a dictionary structured as follows:

- **results (list of dicts):** A list containing dictionaries for each row returned by the SQL query. Each dictionary's keys correspond to the column names.

#### Usage

To use `CallSQL`, instantiate the class with the required inputs, then call the `run` method to execute the query against the database. Use the result of `run` to access the fetched data.

### 2. `__init__.py`

This is an empty file serving as the package marker, indicating that the directory `CallSQL` is a Python package.

### 3. `typed.py`

This file contains type definitions using `TypedDict` for strict type-checking of inputs and outputs in the `CallSQL` class.

#### Defined Types

- **CallSQLInputs:** A `TypedDict` defining required and optional input fields needed for the `CallSQL` class.
- **CallSQLOutputs:** A `TypedDict` defining the structure of the output from the `CallSQL` class.

These type definitions are helpful for developers to understand and enforce the expected structure of data when utilizing the `CallSQL` module.

## Conclusion

The `CallSQL` module is designed for users requiring dynamic SQL execution within a structured workflow. It abstracts the complexity of managing database connections and executing queries, enabling developers to focus on using SQL within their broader computational tasks efficiently.
