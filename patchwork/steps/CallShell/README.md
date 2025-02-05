# Documentation for `CallShell` Module

This module defines a `CallShell` class within the `patchwork.steps.CallShell` package, which is used to execute shell scripts as part of a series of steps in the Patchwork framework.

## Overview

The `CallShell` class is designed to execute shell scripts provided by the user with customizable environment variables and working directory configurations. It leverages the Python `subprocess` module to run shell commands and capture their output. This step could be part of a pipeline where various scripts need to be executed in sequence.

## Usage

The `CallShell` class can be utilized wherever there is a need to run shell commands within a pipeline step. This might be particularly useful for automation tasks, such as deploying applications, running maintenance scripts, or performing batch-processing jobs.

## Inputs

The inputs to `CallShell` are defined through the `CallShellInputs` TypedDict, which supports the following attributes:

- **script** (str): The shell script or command to execute.
  
- **working_dir** (str, optional): The directory from which the script is executed. Defaults to the current working directory if not provided.
  
- **env** (str, optional): Environment variables to set for the execution context, specified as a semicolon-separated list of key-value pairs.
  
- **script_template_values** (dict, optional): A dictionary of values to be rendered into the script using a Mustache templating style.

## Outputs

The outputs from `CallShell` are captured in the `CallShellOutputs` TypedDict, which includes:

- **stdout_output** (str): The standard output produced by the executed shell script.
  
- **stderr_output** (str): The error output (standard error) produced by the executed shell script. This is returned in the dictionary from the `run` method but not explicitly defined in the TypedDict.

## How it Works

1. **Initialization**: When the `CallShell` step is initialized, it processes the given script with any templating values using Mustache rendering. It also parses any provided environment variables.

2. **Execution**: The `run()` method executes the shell script using `subprocess.run()`, capturing both stdout and stderr.

3. **Error Handling**: If the subprocess returns a non-zero exit code (indicating failure), the step status is set to `FAILED`.

4. **Logging and Output**: It logs the stdout and stderr to the standard logging system and returns them in the output dictionary.

This class is a part of a broader framework and assumes familiarity with Patchwork's step architecture and logging utilities. The user must ensure that the input data, particularly the shell script and any templating values, are correctly specified to avoid unexpected errors during execution.
