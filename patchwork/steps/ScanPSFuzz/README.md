# Patchwork ScanPSFuzz Module Documentation

This module is part of the `patchwork` library and is located in the `steps/ScanPSFuzz` package. The primary functionality revolves around using the `prompt-security-fuzzer` tool to process input files with a specified API key. Below are detailed descriptions of each file contained within this module, including their inputs, outputs, and functionality.

## Overview

The module consists of three main files:
- `typed.py`: Defines structured input and output types for the ScanPSFuzz step.
- `ScanPSFuzz.py`: Implements the ScanPSFuzz step functionality using `prompt-security-fuzzer`.
- `__init__.py`: Initialization file for the package.

---

## `typed.py`

This file defines the required and optional input types, as well as the outputs for the `ScanPSFuzz` step.

### Inputs

- **`prompt_file_path`** (`Annotated[str]`): Required input, represents the file path to the prompt file that `prompt-security-fuzzer` will process. It's a path type.
  
- **`openai_api_key`** (`Annotated[str]`): Required input, represents the OpenAI API key needed to execute commands. It's a configuration type.
  
- **`working_dir`** (`Annotated[str]`): Optional input, specifies the working directory for the command execution. It's a path type.

### Outputs

- **`stdout_output`** (`str`): The output of the command execution captured from standard output.

---

## `ScanPSFuzz.py`

This file contains the main `ScanPSFuzz` class, which extends the `Step` class and uses the `CallCommand` for executing the `prompt-security-fuzzer`.

### Functionality

- **Initialization**:
  - Checks if `prompt-security-fuzzer` is installed.
  - Constructs command arguments using inputs.
  - Initializes an inner step `CallCommand` with the constructed command details.

- **`__is_ps_fuzz_installed`**: Static method checking if the `prompt-security-fuzzer` tool is installed via a subprocess call.

- **Run**:
  - Executes the command with the provided inputs using the `Run` method.
  - Sets the status based on the execution result, returning a `DataPoint`.

### Usage

This class is used in a pipeline to process prompt files with `prompt-security-fuzzer`, leveraging OpenAI's API, and capture the output for further processing.

---

## `__init__.py`

This file serves as an initialization file for the `ScanPSFuzz` package. It is currently empty and serves as a placeholder to allow Python to recognize the directory as a package.

---

### Additional Information

To use the `ScanPSFuzz` step, ensure that the `prompt-security-fuzzer` tool is installed. Instructions for installation are provided within the class, highlighting the need for `pipx` and potentially `setuptools`.
