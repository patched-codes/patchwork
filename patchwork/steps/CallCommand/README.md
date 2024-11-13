# Documentation: CallCommand Module

## Overview
The `CallCommand` module is part of the `patchwork.steps` package, designed to execute shell commands as part of a workflow. This module provides classes to define inputs and outputs for command execution, manage execution logic, and handle command environments and working directories.

### Files
- **`typed.py`**: Defines input and output data structures using Python's `TypedDict`.
- **`__init__.py`**: Acts as an initializer for the module, currently empty.
- **`CallCommand.py`**: Contains the main `CallCommand` class, responsible for executing the command using the specified configurations.

## Components

### `typed.py`

#### Inputs

- **`CallCommandInputs`**: This dictionary specifies the necessary input types for the command:
  - `command`: Required (`str`), the command to execute.
  - `command_args`: Optional (`str`), additional arguments for the command.
  - `working_dir`: Optional (`str`), the working directory for execution, specified as a path.
  - `env`: Optional (`str`), the environment variables, specified as a semicolon-separated string of key-value pairs.

#### Outputs

- **`CallCommandOutputs`**: This dictionary defines the output structure:
  - `stdout_output`: (`str`), capturing the standard output of the executed command.

### `CallCommand.py`

#### Class: `CallCommand`

The `CallCommand` class inherits from `Step` and manages the execution of the specified command within the context of a workflow step.

- **Initialization**: Accepts a dictionary containing the inputs defined in `CallCommandInputs`.
  - Validates the presence of the command in the system's PATH.
  - Parses command arguments and environment variables.

- **Method: `run()`**: Executes the command.
  - Constructs the command with its parameters and desired environment.
  - Uses `subprocess.run` to execute and capture output.
  - Handles errors, logs appropriate messages for failed executions.

## Usage Example

To use the `CallCommand` module within the `patchwork.steps` workflow:

```python
from patchwork.steps.CallCommand.CallCommand import CallCommand

# Define inputs
inputs = {
    "command": "echo",
    "command_args": "Hello World",
    "working_dir": "/path/to/dir",
    "env": "VAR1=value1;VAR2=value2"
}

# Create instance of CallCommand
command_step = CallCommand(inputs)

# Execute command
outputs = command_step.run()

# Access standard output
stdout = outputs.get("stdout_output")
```

This module is useful in automation scripts or applications where command-line operations need to be integrated as discrete steps within a workflow, allowing execution control, logging, and error handling.
