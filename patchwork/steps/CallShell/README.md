# Documentation for CallShell Module

This documentation provides an overview of the `CallShell` module, explaining its purpose, how it can be used, and detailing its input and output parameters.

## Overview

The `CallShell` module is part of the `patchwork` library, designed to execute shell scripts from a Python context. It offers a structured way of defining the inputs necessary for running shell commands, handles output capture, and provides error logging.

This module can be particularly useful in automated pipelines or scenarios where shell interaction within a Python script is needed.

## Inputs

### Required Inputs

- **script** (`str`): The shell script or command to be executed.

### Optional Inputs

- **working_dir** (`str`): Specifies the working directory for executing the shell command. It can be provided as a path.
- **env** (`str`): A semi-colon separated string for setting environment variables in `KEY=VALUE` format.
- **script_template_values** (`dict[str, Any]`): A dictionary of values to be used in template rendering the script.

## Outputs

- **stdout_output** (`str`): Captures the standard output produced by the shell command.
- **stderr_output** (`str`): Captures the standard error output produced by the shell command. 

Note: While not explicitly defined in `typed.py`, `stderr_output` is captured in the `CallShell` class's `run()` method.

## Implementation Details

### Class: `CallShell`

This class inherits from the `Step` base class, using `CallShellInputs` as the input type and `CallShellOutputs` as the output type. It processes the specified script and runs it within a subprocess.

#### Methods

- **`__init__`**: Initializes the `CallShell` instance with given inputs, rendering the script if template values are provided, and preparing the environment.

- **`__parse_env_text`**: A static method to parse environment variable assignments from a text string.

- **`run`**: Executes the shell command, logs output and error details, and sets the status based on the execution outcome. Uses Python's `subprocess.run` for executing the command.

### Utility Imports and Logging

The module makes use of utility functions like `mustache_render` for template processing and leverages a `logger` for logging standard output and error messages during execution.

This integration is essential for efficiently managing and debugging shell script executions embedded within Python workflows.

## Usage

To use this module:

1. Instantiate the `CallShell` class with a dictionary of inputs.
2. Invoke the `run` method to execute the shell script.
3. Capture the outputs, particularly `stdout_output` and `stderr_output`, for further processing or analysis. 

```python
inputs = {
    "script": "echo Hello World",
    "working_dir": "/path/to/dir",
    "env": "VAR1=value1;VAR2=value2",
    "script_template_values": {"some_placeholder": "some_value"}
}

call_shell = CallShell(inputs)
outputs = call_shell.run()
print(outputs["stdout_output"])
```

This module provides a robust interface for handling shell commands within Python, ensuring that inputs are properly managed, and outputs are consistently captured and logged.
