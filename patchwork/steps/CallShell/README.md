# Documentation: CallShell Module

This module consists of three primary Python files that together facilitate the execution of shell scripts within a Python environment as part of a step in the Patchwork system.

## Overview

The `CallShell` module is designed to execute shell scripts using a Python interface. It is built upon a class extending the existing `Step` class from the Patchwork system. This module allows users to specify the script, working directory, environment variables, and template values, executing the script using these parameters.

### Contents

- **File: CallShell.py**: The main functionality for running shell scripts.
- **File: __init__.py**: Initializes the module (currently empty).
- **File: typed.py**: Defines input and output types for the `CallShell` class.

## CallShell.py

### What It Does

- **Script Execution**: Executes a shell script within a given context, including a specific working directory and environment variables.
- **Template Rendering**: Uses the `mustache` templating engine to render the script text with provided template values.

### Inputs

- **`script`** (str): The shell script to be executed.
- **`working_dir`** (str): Optional. Specifies the working directory for the script.
- **`env`** (str): Optional. Environment variables formatted as a string. Utilizes `shlex` for parsing.
- **`script_template_values`** (dict): Optional. Values used to replace placeholders in the script.

### Outputs

- **`stdout_output`** (str): The standard output from executing the script.
- **`stderr_output`** (str): The error output from executing the script.

### Usage

After instantiating with the required inputs, calling the `run` method executes the script and returns outputs containing the standard and error outputs.

## __init__.py

This file is currently empty and serves to initialize the `patchwork.steps.CallShell` package.

## typed.py

### What It Does

Defines the structured data types for inputs and outputs to be used by the `CallShell` class.

### Data Types

- **`__RequiredCallShellInputs`**: Ensures `script` is provided.
- **`CallShellInputs`**: Supports additional optional fields like `working_dir`, `env`, and `script_template_values`.
- **`CallShellOutputs`**: Specifies that the outputs include `stdout_output`.

---

This module is likely to be used in the context of a larger workflow management system, where shell operations need to be automated and managed programmatically.
