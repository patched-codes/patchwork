# Documentation for CallShell Implementation

## Overview

The code in this directory, `patchwork/steps/CallShell`, defines a Python package for executing shell scripts within a specified working directory and environment. This is done through the `CallShell` class, which extends a `Step` class. The implementation leverages templates for scripts and manages logging outputs.

## Files

### 1. CallShell.py

This is the primary file implementing the `CallShell` class responsible for executing shell scripts.

#### Inputs

- **script**: A shell command or script to be executed.
- **working_dir (Optional)**: A working directory where the command will be executed. Defaults to the current working directory.
- **env (Optional)**: Environment variables for the script, specified as a string.
- **script_template_values (Optional)**: A dictionary providing templating values for the script using Mustache format.

#### Outputs

- **stdout_output**: Standard output from running the shell script.
- **stderr_output**: Standard error output from running the shell script.

#### Usage

The `CallShell` class is initialized with a dictionary of inputs. The script is executed using Python's subprocess module, with the possibility to specify environment variables and a working directory. Script output and errors are logged, and the status of the execution is noted in case of failure.

### 2. __init__.py

- Currently contains no code but is necessary for Python to recognize the directory as a package.

### 3. typed.py

This file defines the input and output types for `CallShell`.

#### Input Types (`CallShellInputs`)

- **script**: Mandatory script to execute.
- **working_dir**: String specifying the path to the working directory (annotated to indicate it's a path).
- **env**: String of environment variable assignments.
- **script_template_values**: A dictionary for rendering script templates.

#### Output Types (`CallShellOutputs`)

- **stdout_output**: String of the standard output captured from the shell execution.

## Recommended Usage

The `CallShell` module is intended for situations where one needs automated execution of shell scripts in various environments with precise control over the working directory and environmental context. It is useful for integrating shell operations into larger Python applications, especially those using the Patchwork framework for automation tasks.
