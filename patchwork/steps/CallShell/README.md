# CallShell Module Documentation

## Overview

The CallShell module is part of the Patchwork project, designed for executing shell commands within a Python application. It is structured to allow for templated scripts execution, accommodate custom working directories, and handle environment variables effectively. The module includes three main components: the CallShell core functionality, the input-output type definitions, and an initialization file.

## How It Works

Users can instantiate the `CallShell` class with specific inputs defining the script to be executed, template values for script customization, working directory, and environment variables. When executed, the script runs in a subprocess, capturing both the standard output and error streams.

## Input and Output

### Inputs

The module leverages the `CallShellInputs` TypedDict for its input configuration. The key input fields include:

- `script` (required): A string containing the shell script to be executed.
- `working_dir` (optional): The directory from which the script should be run. Defaults to the current working directory.
- `env` (optional): A string of environment variable assignments. These are parsed and applied during script execution.
- `script_template_values` (optional): A dictionary of values used to render the script template, allowing for dynamic script content.

### Outputs

The outputs are defined by the `CallShellOutputs` TypedDict:

- `stdout_output`: Captures the standard output (stdout) produced by the script execution.
- `stderr_output`: Captures the standard error (stderr) output.

## Structure

### Files

1. **CallShell.py**: Contains the core implementation of the `CallShell` class, handling the setup and execution of shell scripts and processing standard output and errors.

2. **__init__.py**: An empty initialization file necessary for Python package recognition. 

3. **typed.py**: Provides type definitions for input and output data structures, implementing support for required and optional parameters using TypedDict.

## Usage

To use the `CallShell` class, a user needs to supply a dictionary matching the `CallShellInputs` structure. Once instantiated, calling the `run()` method will execute the configured shell script and return a dictionary containing the standard output and error information.

## Example

```python
from patchwork.steps.CallShell.CallShell import CallShell

inputs = {
    "script": "echo 'Hello, World!'",
    "working_dir": "/path/to/directory",
    "env": "VAR1=value1; VAR2=value2",
    "script_template_values": {}
}

call_shell_step = CallShell(inputs)
outputs = call_shell_step.run()

print(outputs["stdout_output"])
print(outputs["stderr_output"])
```

This example sets up a simple shell command to print "Hello, World!" and captures its output. Environment variables and working directory adjustments show how flexible this utility can be.
