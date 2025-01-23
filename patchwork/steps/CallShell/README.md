# CallShell Module Documentation

The CallShell module is a part of the `patchwork.steps` package and is designed to execute shell commands from within Python using specified template values, environment variables, and a working directory. It primarily handles shell script execution, captures its output, and handles errors appropriately. 

## Contents

- `CallShell.py`: Main implementation file for the `CallShell` class.
- `__init__.py`: Initialize the CallShell package.
- `typed.py`: Contains type definitions for CallShell inputs and outputs.

## File: CallShell.py

### Description

The `CallShell.py` file contains the `CallShell` class, which inherits from a `Step` in the `patchwork` framework. The class is used to run shell scripts with specific inputs, environment configurations, and working directories. Outputs from the shell command are captured and logged, and errors are managed gracefully.

### Inputs

- **script**: The shell script to be executed. This script can include templates that need to be rendered using mustache syntax.
- **script_template_values**: A dictionary of values to be filled into the script template.
- **working_dir**: Specifies the working directory where the script will run. Defaults to the current working directory.
- **env**: String representation of environment variable assignments to modify the shell environment. Uses `shlex` to parse and override current environment variables.

### Outputs

- **stdout_output**: Captures standard output from the shell execution.
- **stderr_output**: Captures standard error output from the executed shell command.

### Functionality

- **Initialization**: Sets up the shell script, prepares the working directory, and sets up environment variables.
- **run()**: Executes the script using `subprocess.run` while capturing both standard output and error output. If the script execution fails, it logs an error and sets the step status to failed.

### Logging

Logging is managed using the `patchwork.logger` to track stdout and stderr during the execution of the shell command.

## File: typed.py

### Description

This file contains type definitions for the `CallShell` class inputs and outputs using Python's `TypedDict` and annotations.

### Types

- **CallShellInputs**: Defines the structure and optional parameters required to initialize and run a `CallShell` step.
  - Required: `script`
  - Optional: `working_dir`, `env`, `script_template_values`
- **CallShellOutputs**: Defines the expected output structure.
  - Returns: `stdout_output`

## How to Use

1. **Create an instance of `CallShell`**, providing necessary input parameters like `script`, `working_dir`, `env`, and `script_template_values` in a dictionary.
2. **Call the `run` method** to execute the shell script with the specified environment and working directory settings.
3. **Collect the execution results**, which will be returned as a dictionary containing `stdout_output` and `stderr_output`.

This module is ideal for scenarios where complex shell command execution needs to be automated within a Python application, accommodating dynamic script configurations and environment setups.
