# Overview of CallShell Module

This module provides functionality to execute shell scripts within a structured framework, useful for orchestrating tasks that require shell command execution. It is implemented in a Python package and consists of three main files: `typed.py`, `CallShell.py`, and an empty `__init__.py`.

## Files Information
- **patchwork/steps/CallShell/typed.py**: Defines structured inputs and outputs for shell script calls using TypedDict for type safety.
- **patchwork/steps/CallShell/CallShell.py**: Implements the actual logic for executing shell scripts with customized environment variables and working directories.
- **patchwork/steps/CallShell/__init__.py**: An empty initializer for the package.

---

## File: patchwork/steps/CallShell/typed.py

### Inputs

- **script**: (Required) A plain string representing the shell script to be executed.
- **working_dir**: An optional string specifying the working directory path for the script. Annotated to indicate it's a path.
- **env**: An optional string for specifying environment variables.
- **script_template_values**: A dictionary for parameters to be injected into the script template.

### Outputs

- **stdout_output**: A string capturing the standard output of the executed script.

This file is crucial for defining the structure of the inputs and outputs, ensuring that the system interacting with shell executions uses predefined contract models.

---

## File: patchwork/steps/CallShell/CallShell.py

### Inputs

This implementation builds on the structures defined in `typed.py` to initialize and process shell script executions. It expects inputs in the form of a dictionary structured according to `CallShellInputs`.

### Outputs

- The script run results are captured and returned in a dictionary format, with at least `stdout_output`.

### Functionality

The main class `CallShell` provides a `run` method that:

1. **Parses Environment Variables**: Converts environment variable strings into a dictionary format.
2. **Executes Shell Scripts**: Uses the `subprocess.run` method to run the provided shell script, handling any potential errors during execution.
3. **Logging**: Outputs logs for both standard output and error streams for diagnostics purposes.

This component is key in running scripted tasks using pre-defined parameters, and it is expected to log outcomes effectively and return execution results or errors.

---

### Usage

**CallShell** is typically used in scenarios where automated shell command execution is integrated into a larger system, such as data processing pipelines or deployment automation workflows. The structured input-output design helps it mesh well with frameworks expecting typed contracts, ensuring predictability and error management.

---

## File: patchwork/steps/CallShell/__init__.py

An empty file that allows Python to recognize this directory as a package, enabling the import of the module's classes and functions.
