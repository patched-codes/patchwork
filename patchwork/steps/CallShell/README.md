# Documentation: `patchwork.steps.CallShell` Module

The `patchwork.steps.CallShell` module consists of a set of Python scripts designed to execute shell scripts from within Python, handle their inputs and outputs, and integrate with other parts of a larger application using typed configurations and logging. This module is divided into three core files:

1. `typed.py`: Defines input and output typing for shell execution.
2. `CallShell.py`: Implements the logic for executing shell commands.
3. `__init__.py`: Initializes the module (currently empty).

---

## `typed.py`

### Description
This file contains type definitions for inputs and outputs involved with executing shell scripts. It uses the `TypedDict` from `typing_extensions` to ensure that inputs and outputs conform to expected shapes, which aids in type-checking and robustness.

### Inputs

- **CallShellInputs**: 
  - `script` (required): A string containing the shell script to be executed.
  - `working_dir` (optional): Directory in which to run the script.
  - `env` (optional): Environment variables for the shell in string format.
  - `script_template_values` (optional): A dictionary of values to render into the script.

### Outputs

- **CallShellOutputs**: 
  - `stdout_output`: Captured standard output from the executed script.

---

## `CallShell.py`

### Description
This script implements the core functionality of running a shell script as a step in a larger process. It uses Python's `subprocess` module to execute the script and log the outputs.

### How It Works

- Upon initialization, it renders the provided script using `mustache_render` considering any template values given.
- It sets the working directory and parses the environment variables.
- It executes the script using `subprocess.run`, capturing standard output and error.
- The `run` method executes the command and logs the outputs. If the command fails (non-zero exit status), it marks the step as failed.

### Inputs

- Accepts a dictionary of parameters (defined in `typed.py`) during initialization.

### Outputs

- Returns a dictionary containing:
  - `stdout_output`: Text captured from the script's standard output.
  - `stderr_output`: Text captured from the script's standard error.

---

## `__init__.py`

### Description
This file is currently empty but serves as a placeholder to initialize the `CallShell` submodule. It's common in Python projects to include an `__init__.py` file to facilitate imports and package discovery.

---

This module is useful for developers integrating shell script execution into their Python applications, particularly when there is a need for templating scripts, controlled environment setup, and structured input-output handling.
