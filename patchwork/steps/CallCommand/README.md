# Documentation for `CallCommand` Module

This document provides an overview and usage guide for the `CallCommand` module, including its structure, inputs, and outputs. This module is part of a larger project organized under the `patchwork.steps` package.

## Overview

The `CallCommand` module provides functionality to execute system commands programmatically through a defined step class. It is likely used in workflows where specific shell commands need to be executed as part of a larger automated process. This module integrates command execution within a pipeline, capturing output and handling errors.

### Module Structure

1. **`typed.py`**: Defines the input and output data structures used by the `CallCommand` class.
2. **`__init__.py`**: Initializes the module. It is currently empty, serving as a placeholder for package initialization.
3. **`CallCommand.py`**: Contains the primary class `CallCommand` which manages input parsing, command execution, and output processing.

## Inputs

The inputs for the `CallCommand` class are defined in `typed.py` and include:

- **command**: (Required) A `str` indicating the system command to execute. This command must be available in the system's PATH.
  
- **command_args**: (Optional) A `str` containing arguments for the command. These are processed and split into a list format for execution.
  
- **working_dir**: (Optional) An `Annotated[str]` that specifies the working directory in which to run the command. It defaults to the current directory.

- **env**: (Optional) A `str` to define environment variables for the command execution, formatted as `key=value;` pairs.

## Outputs

The outputs for the `CallCommand` class are defined in `typed.py`:

- **stdout_output**: A `str` capturing the standard output of the executed command. This is useful for debugging or logging the command's behavior.

## Usage

To use the `CallCommand` class, an instance must be created with a dictionary of inputs. The `run` method executes the command, and its standard output can be accessed via the `stdout_output`.

### Example

```python
from patchwork.steps.CallCommand.CallCommand import CallCommand

inputs = {
    "command": "ls",
    "command_args": "-la",
    "working_dir": "/home/user/directory",
    "env": "VAR1=value1;VAR2=value2;"
}

command_step = CallCommand(inputs)
output = command_step.run()

print(output["stdout_output"])
```

### Error Handling

If the command fails, the `run` method will catch the exception, log an error message, and return an empty `stdout_output`. The step status is updated to `FAILED`, providing diagnostic information.

This approach allows for robust execution of shell commands within Python applications, supporting complex workflows and automation tasks.
