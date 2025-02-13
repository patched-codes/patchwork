# Documentation: CallShell Module

## Overview
The `CallShell` module is part of a larger framework aimed at executing shell scripts within a Python application context. This component provides a structured way to run shell commands, handle environment variables, and capture command output. It is primarily used in situations where scripts need to be executed programmatically with dynamic parameters.

## Files
The module consists of three primary files:

1. `CallShell.py`
2. `__init__.py`
3. `typed.py`

### `CallShell.py`
This file contains the core logic for executing shell commands.

#### Class: `CallShell`
The `CallShell` class inherits from `Step` with specified input and output classes, `CallShellInputs` and `CallShellOutputs`.

#### Inputs
- `script`: A string containing the shell script to be executed.
- `working_dir`: An optional directory path where the script is executed. Defaults to the current working directory.
- `env`: A string that defines environment variables.
- `script_template_values`: A dictionary for rendering the script with dynamic values.

#### Outputs
- `stdout_output`: Captures the standard output from the shell execution.
- `stderr_output`: Captures the standard error from the shell execution.

#### Methods
- `__init__`: Initializes the command to be executed, the working directory, and environment variables.
- `__parse_env_text`: Parses the `env` string to create a dictionary of environment variables.
- `run`: Executes the shell script, manages exceptions, and logs outputs.

### Usage
To use the `CallShell` class, create an instance with a dictionary of inputs, call the `run` method to execute the shell command, and collect outputs through the returned dictionary.

### `__init__.py`
This file is empty, serving as a namespace initializer for Python packages.

### `typed.py`
Defines input and output typing for the `CallShell` class using Python's `TypedDict` for type hinting.

#### `CallShellInputs` 
- Inherits from `__RequiredCallShellInputs` and is marked 'total=False' to make additional fields optional.

#### `CallShellOutputs`
Defines types for the output fields, ensuring the API consistency.

---

This module is ideal for developers needing programmatic access to shell command execution within larger Python workflows. It offers flexibility through templated scripts, customizable environment variables, and detailed logging of command outputs.
