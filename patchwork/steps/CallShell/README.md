# CallShell Module Documentation

This module provides functionality to execute shell scripts from Python using a flexible input system. It is designed to encapsulate the execution of shell commands, making it easier to integrate and manage within a larger application pipeline, such as an automated data processing or deployment workflow.

## Files Overview

### 1. `CallShell.py`

This file contains the main logic for the `CallShell` class, which executes shell scripts based on provided inputs.

### 2. `__init__.py`

This file is currently empty and serves as an initializer for the `CallShell` package directory.

### 3. `typed.py`

Defines the input and output types used by the `CallShell` class, leveraging Python's type hints for improved clarity and error checking.

---

## CallShell.py

### Description

The `CallShell` class facilitates the execution of shell scripts with customizable environment settings and script parameters. It processes inputs to construct and run the script, capturing both standard output and error messages for review.

### Inputs

- `script`: A string containing the shell script to be executed. This is required.
- `working_dir`: An optional path indicating the directory in which the script should be executed. Defaults to the current working directory.
- `env`: An optional string of environment variable assignments, separated by semicolons, to set for the script execution.
- `script_template_values`: An optional dictionary for templating values used to render the script (using mustache syntax).

### Outputs

- **Standard Output**: Captures the standard output stream (`stdout`) of the script execution.
- **Standard Error**: Captures the standard error stream (`stderr`) of the script execution.

---

## Usage

### To Use the CallShell Class:

1. **Initialize the Class**: Create an instance of `CallShell` by providing a dictionary of inputs that conform to the `CallShellInputs` type described in `typed.py`.

    ```python
    inputs = {
        "script": "echo Hello, World!",
        "working_dir": "/my/directory",
        "env": "VAR1=value1;VAR2=value2",
        "script_template_values": {"key": "value"}
    }
    call_shell_instance = CallShell(inputs)
    ```

2. **Execute the Script**: Call the `run()` method to execute the provided shell script. This will return a dictionary containing the output and errors from the script execution.

    ```python
    outputs = call_shell_instance.run()
    print(outputs['stdout_output'])
    ```

### Error Handling

If the script fails to execute properly, the class sets the step status to `FAILED` and logs appropriate error messages. It does not raise exceptions directly but logs error details to facilitate troubleshooting.

### Environment Parsing

The class supports `;` separated environment variable assignments, rejecting any malformed entries with additional logging for clarity.

---

This module is particularly suited for use in systems that automate script-based tasks, allowing developers to embed command-line scripts within Python-driven workflows.
