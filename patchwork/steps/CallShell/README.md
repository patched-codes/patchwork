# Documentation for CallShell Module

## Overview

The `CallShell` module is part of a Python project, designed to execute shell scripts within a controlled environment. It can modify the working directory and environment variables as specified by the inputs, and it utilizes mustache templates for script customization. This module is likely to be used in scenarios where execution of shell commands or scripts is necessary from within a Python application, such as automation scripts or deployment routines.

## File Structure

- **CallShell.py**: Contains the main logic for executing shell scripts.
- **typed.py**: Defines the input and output types for `CallShell`.
- **\_\_init\_\_.py**: Marks the directory as a Python package (empty file).

## File: CallShell.py

### Inputs

- **`inputs: dict`**: Dictionary containing configuration for executing the shell script.
  - `script`: The shell script to be executed, possibly using mustache placeholders.
  - `script_template_values`: (Optional) Dictionary of values to replace placeholders in the script.
  - `working_dir`: (Optional) The directory in which to execute the script, defaults to the current working directory.
  - `env`: (Optional) A string defining additional environment variables, separated by semicolons.

### Outputs

- **`dict`**: Returns a dictionary containing:
  - `stdout_output`: The standard output captured from running the shell script.
  - `stderr_output`: The standard error captured from running the shell script.

### Functionality

1. **Initialize**: Constructs the `CallShell` object, sets up the script with mustache rendering if needed, sets the working directory, and parses environment variables from text input.
2. **Environment Parsing**: Splits and parses the environment variable string into a dictionary, ensuring each variable has a valid assignment.
3. **Execute**: Runs the provided shell script using the `subprocess.run` method, captures output, and logs results. If the script fails, it will set the status to failed and log relevant error messages.

## File: typed.py

### Types

- **`CallShellInputs`**: A TypedDict that defines the expected inputs for the `CallShell` class. Requires `script` and optionally accepts `working_dir`, `env`, and `script_template_values`.
- **`CallShellOutputs`**: A TypedDict that defines the expected outputs from the `CallShell` class, specifying standard output as `stdout_output`.

## Usage Examples

The module can be used to execute shell scripts dynamically from a Python environment, particularly when these scripts need to be adjusted or templated according to different runtime environments or configurations. Here’s a simple example of how you might configure and run a script using the module:

```python
from patchwork.steps.CallShell.CallShell import CallShell

inputs = {
    "script": "echo Hello, World!",
    "working_dir": "/path/to/execute",
    "env": "VAR1=value1;VAR2=value2",
}

call_shell_step = CallShell(inputs)
outputs = call_shell_step.run()
print(outputs['stdout_output'])
```

This will execute the script `"echo Hello, World!"` in the given working directory with the specified environment variables.
