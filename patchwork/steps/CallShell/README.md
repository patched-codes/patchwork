# CallShell Module Documentation

This documentation provides an overview of the `CallShell` module, which is part of the Patchwork project. The module allows for the execution of shell scripts from within a Python application, capturing and returning the output for further processing.

## Overview

The `CallShell` module consists of three main files:

- `typed.py`: Defines the input and output type annotations for the shell execution step.
- `CallShell.py`: Implements the core functionality to run shell scripts, manage execution environment, and capture outputs.
- `__init__.py`: An empty file indicating the package structure.

## File: typed.py

### Functionality

The `typed.py` file defines the input and output data structures for the `CallShell` step using Python's `TypedDict`. It includes:

- **Inputs**:
  - `script`: A required string that specifies the shell script to execute.
  - `working_dir`: (Optional) A string representing the working directory where the script should run.
  - `env`: (Optional) A string for additional environment variables.
  - `script_template_values`: (Optional) A dictionary for rendering the script with dynamic values.

- **Outputs**:
  - `stdout_output`: A string capturing the standard output from the shell script.

### Likely Usage

Users defining a shell execution step will instantiate `CallShellInputs` to ensure correct typing and input verification for the `CallShell` process.

## File: CallShell.py

### Functionality

This file contains the `CallShell` class, a subclass of `Step`, which is responsible for the execution of shell commands. The class initializes with user-provided inputs, parses additional environment variables if specified, and runs the script within a subprocess. Key features include:

- **Environment Handling**: Parses and merges custom environment variables with the system environment.
- **Script Rendering**: Supports template rendering for dynamic script values.
- **Execution and Output Capture**: Executes the script and captures both standard output and error output, logging them for review.

### Inputs

Inputs are provided through the `CallShellInputs` structure defined in `typed.py`, allowing for detailed configuration of the script execution context.

### Outputs

Outputs include a dictionary with:

- `stdout_output`: Captured stdout from the script.
- `stderr_output`: Captured stderr from the script for diagnostic purposes.

### Likely Usage

This is designed for situations requiring integration with shell-level operations from a Python codebase, such as deploying applications, running maintenance scripts, or integrating various systems.

## File: __init__.py

### Functionality

This is an empty file serving as an initializer for the `CallShell` package, allowing imports to recognize it as a cohesive module.

### Likely Usage

Maintains the structure of the package and does not contribute functional code.
