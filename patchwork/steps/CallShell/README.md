# CallShell Module Documentation

## Overview

The `CallShell` module in the `patchwork` package is responsible for executing shell scripts within a specified environment. This is accomplished through the `CallShell` class which inherits from the `Step` class, enabling it to be used as a step in a larger workflow. The class takes in specific inputs, renders a script using the Mustache template engine, adjusts the environment and working directory accordingly, and executes the script, capturing its outputs.

## Files

### 1. CallShell.py

- **Language**: Python
- **Functionality**: Contains the main logic of the `CallShell` class for executing shell scripts.
- **Dependencies**: 
  - `os`, `shlex`, `subprocess`, `pathlib.Path`
  - Utilities from `patchwork` like `mustache_render`, `logger`, `Step`, `StepStatus`
  - Input and output definitions from `typed.py`.

### 2. __init__.py

- **Language**: Python
- **Purpose**: Acts as an initialization file for the `CallShell` module. This file is currently empty.

### 3. typed.py

- **Language**: Python
- **Functionality**: Defines input and output types for the `CallShell` class using `TypedDict`.

## CallShell Class Description

The `CallShell` class facilitates running shell scripts as part of a workflow.

### Inputs

- **script**: `str` - Required input representing the shell script to be executed.
- **working_dir**: `Annotated[str, StepTypeConfig(is_path=True)]` - Optional working directory where the command should be executed.
- **env**: `str` - Optional string for environment variable settings using `key=value` format.
- **script_template_values**: `dict[str, Any]` - Optional dictionary for mustache template variables to be replaced in the script.

### Outputs

- **stdout_output**: `str` - Captures the standard output produced by the script.
- **stderr_output**: `str` - Captures the error output produced by the script.

## Usage

To utilize the `CallShell` class, instantiate it with appropriate inputs. It automatically renders the script based on the provided template values, sets the working directory and environment, then executes the script and captures both standard and error outputs.

## Example Usage

```python
inputs = {
    "script": "echo 'Hello World!'",
    "working_dir": "/tmp",
    "env": "PATH=/usr/bin",
    "script_template_values": {}
}

call_shell_step = CallShell(inputs)
result = call_shell_step.run()

print("Standard Output:", result["stdout_output"])
print("Error Output:", result["stderr_output"])
```

This example instantiates a `CallShell` object with a simple script and prints its outputs, demonstrating basic usage within a workflow.

## Key Considerations

- Ensure that the provided script accounts for any necessary permissions and environment configurations.
- Use the `script_template_values` for scripts that require dynamic content, replacing placeholders with actual values before execution.
- Handle errors gracefully by using the `StepStatus` to manage failed script executions.
