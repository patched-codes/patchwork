# CallSQL Module Documentation

The `CallSQL` module is designed to facilitate interaction with a SQL database by executing SQL queries and fetching results. This functionality is particularly useful for integrating database operations within a larger data processing or ETL pipeline.

## Components

The `CallSQL` module consists of three primary components:

1. **CallSQL.py**: Contains the main logic for executing a SQL query and fetching results.
2. **\_\_init\_\_.py**: Initializes the module (empty in this case, can be used for package-level imports or initial setup).
3. **typed.py**: Defines input and output data structures using typed dictionaries.

## File: CallSQL.py

### Description

The `CallSQL` class inherits from the `Step` base class and is responsible for running a SQL query against a specified database. It uses SQLAlchemy to manage database connections and execute queries.

### Inputs

- **db_query**: (str) The SQL query to be executed.
- **db_dialect**: (str) The type of SQL dialect (e.g., 'postgresql', 'mysql').
- **db_driver**: (Optional[str]) The specific driver for the database dialect.
- **db_username**: (Optional[str]) Username for database authentication.
- **db_password**: (Optional[str]) Password for database authentication.
- **db_host**: (Optional[str]) Database host, default is 'localhost'.
- **db_port**: (Optional[int]) Port number for database connection, default is 5432.
- **db_database**: (Optional[str]) Name of the database to connect to.
- **db_params**: (Optional[dict[str, Any]]) Additional parameters for the database connection.
- **db_driver_args**: (Optional[dict[str, Any]]) Custom arguments for the database driver.
- **db_query_template_values**: (Optional[dict[str, Any]]) Values to render into the SQL query using Mustache templating.

### Outputs

- **results**: (list[dict[str, Any]]) A list of rows returned by the executed query, each represented as a dictionary.

## File: \_\_init\_\_.py

### Description

This file is included to initialize the package. It's empty, but serves as a placeholder for future expansions or to include package-level imports.

## File: typed.py

### Description

Defines typed dictionaries to ensure structured input and output data handling:

### Data Structures

- **__RequiredCallSQLInputs**: Contains required fields for executing the SQL query (`db_dialect`, `db_query`).
- **CallSQLInputs**: Extends `__RequiredCallSQLInputs` with optional fields like database connection details (`db_username`, `db_password`, etc.).
- **CallSQLOutputs**: Defines the structure of the output data, containing the `results` list.

## Usage

To use the `CallSQL` module, you need to provide a dictionary of inputs detailing the database connection parameters and the SQL query. The `run` method will execute the query and return the result set as a list of dictionaries.

### Example

```python
inputs = {
    "db_query": "SELECT * FROM users WHERE age > :age",
    "db_dialect": "postgresql",
    "db_username": "user",
    "db_password": "password",
    "db_host": "localhost",
    "db_port": 5432,
    "db_database": "example_db",
    "db_query_template_values": {
        "age": 21
    }
}

sql_step = CallSQL(inputs)
results = sql_step.run()
print(results)
```

This code sets up the required inputs, runs a SQL query to select users older than 21, and prints the results.
