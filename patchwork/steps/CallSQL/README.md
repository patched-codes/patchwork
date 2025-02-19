# CallSQL Module Documentation

## Overview

The `CallSQL` module is a Python component used to execute SQL queries on a database. It is structured as part of the broader framework, potentially intended for data processing pipelines. The primary class, `CallSQL`, inherits from a `Step` base class, designed for pipeline steps, and utilizes SQLAlchemy for database interactions.

## Components

### 1. `CallSQL.py`

This is the main implementation file for the `CallSQL` class, responsible for establishing database connections and executing SQL queries.

#### Inputs

The `CallSQLInputs` class, defined in `typed.py`, specifies the expected inputs:

- **Required Inputs:**
  - `db_dialect`: Database dialect (e.g., `postgresql`, `mysql`).
  - `db_query`: The SQL query to execute.

- **Optional Inputs:**
  - `db_driver`: Database driver (e.g., `psycopg2` for PostgreSQL).
  - `db_username`: Username for database authentication.
  - `db_password`: Password for database authentication.
  - `db_host`: Host address of the database server (defaults to `localhost`).
  - `db_port`: Port number (defaults to `5432` for PostgreSQL).
  - `db_name`: The database name.
  - `db_params`: Additional query parameters.
  - `db_driver_args`: Driver-specific arguments.
  - `db_query_template_values`: Template values for rendering the SQL query.

#### Functionality

- **Initialization (`__init__`)**: 
  - Takes a dictionary of inputs, renders the SQL query with the provided template values, and builds a SQLAlchemy engine for database connection.
- **Private Method (`__build_engine`)**: 
  - Configures the database connection URL and creates a SQLAlchemy engine.
  - Validates the connection by executing a simple "SELECT 1".
- **Run Method (`run`)**: 
  - Executes the provided SQL query, fetches results, and logs the number of rows retrieved.
  - Handles exceptions, particularly `InvalidRequestError`, setting the step status to failed if an error occurs.

#### Outputs

- The `CallSQLOutputs` class specifies the output format:
  - `results`: A list of dictionaries, where each dictionary represents a row from the query result set.

### 2. `typed.py`

Includes type definitions for inputs and outputs using `TypedDict`, ensuring strict type checking for required and optional parameters.

### 3. `__init__.py`

An empty initializer file that signifies this directory as a Python package.

## Use Case

The `CallSQL` module is intended for scenarios where automated data retrieval and processing from various databases are required. By integrating into a pipeline workflow, it enables seamless and flexible database querying, leveraging SQLAlchemy's ORM capabilities for database interactions.

This module can be utilized by data engineers and developers who need to execute SQL queries as part of a larger data processing or ETL (Extract, Transform, Load) pipeline.
