# Patchwork PreparePR Module

## Inputs

- `modified_code_files`: A list of modified code files.

## Outputs

- `pr_body`: A formatted PR body that summarizes the changes made to the modified code files.

### Code

The `PreparePR` class is created to prepare a Pull Request body based on the modifications made to a set of code files. The class inherits from a `Step` class. It expects a dictionary of inputs, specifically a list of modified code files. If the required keys are missing, it raises a ValueError.

The `run` method of the class processes the modified code files, groups them by path, and generates a formatted PR body that includes information about the changes made in each file. The resulting PR body is returned as an output.