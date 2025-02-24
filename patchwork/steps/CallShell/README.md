# CallShell Module Documentation

## Overview

The `CallShell` module is a Python implementation that provides functionality for executing shell scripts within an application workflow. Using a combination of template rendering and environment configuration, it seamlessly integrates shell execution into Python processes.

This document details the components and functionalities of the `CallShell` module, which is a part of the larger `patchwork` framework.

## Components

The module consists of the following key files:

1. `CallShell.py` - Implements the main functionality for shell script execution.
2. `__init__.py` - This file is currently empty and serves as a package marker.
3. `typed.py` - Contains type definitions for inputs and outputs used by the `CallShell` class.

## File: CallShell.py

### Functionality

The `CallShell` class serves as the primary entry point for executing shell scripts. It allows users to specify a script, working directory, and environment variables. Here's a breakdown of how it works:

- **Script Rendering**: Templates within scripts can be dynamically rendered using provided values.
- **Environment Parsing**: Environment variables are parsed and set up appropriately for the script execution.
- **Script Execution**: The shell script is executed within a specified working directory with the configured environment.
- **Logging**: Outputs (stdout and stderr) from the script execution are logged for reference.

### Inputs

The `CallShell` class accepts the following inputs via a dictionary:

- `script` (str): The shell script to execute. Required.
- `script_template_values` (dict): Values to render within the script template.
- `working_dir` (str, optional): Directory where the script is executed.
- `env` (str, optional): String describing environment variables to set.

### Outputs

The `CallShell` class returns the following outputs in the form of a dictionary:

- `stdout_output` (str): Standard output from the executed script.
- `stderr_output` (str): Standard error output from the executed script.

### Logging

The execution results, including both stdout and stderr, are logged using the `patchwork` logger. This aids in debugging and tracking script execution.

## File: __init__.py

This file is a standard marker to indicate that the directory can be treated as a Python package. Currently, it does not contain any code or declarations.

## File: typed.py

### Definitions

The `typed.py` file is utilized to define the types of inputs and outputs for the `CallShell` class, helping to ensure type safety and clarity. It uses `TypedDict` from Python's typing extensions module to define these structures.

### Input Types

- `CallShellInputs`: Extends to include optional fields like `working_dir`, `env`, and `script_template_values` in addition to the required `script`.

### Output Types

- `CallShellOutputs`: Defines the structure with a single field `stdout_output` for capturing the script's output.

## Usage Scenario

The `CallShell` module is ideal for scenarios where shell scripts need to be dynamically executed within a Python application, particularly when the script requires specific environment variables or must be run within a certain directory context.

By accommodating template rendering and environment variable parsing, `CallShell` integrates well into pipelines and workflows where hybrid Python and shell script operations are necessary.
