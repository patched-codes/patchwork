# Code Documentation

## Inputs
- `inputs`: Dictionary containing the following keys:
  - `modified_code_files`: List of modified code files.
  - `disable_branch`: Boolean indicating whether branch creation is disabled.
  - `force_branch_creation`: Boolean indicating whether to force branch creation.
  - `branch_prefix`: Prefix for the new branch name.
  - `branch_suffix`: Suffix for the new branch name.

## Outputs
- Dictionary containing the following keys:
  - `base_branch`: Name of the base branch.
  - `target_branch`: Name of the target branch.

### Description
This code module defines a class `CommitChanges` that inherits `Step` class. It includes methods for transition between branches, getting a branch slug from a remote URL, and committing changes with a provided message. The `CommitChanges` class is instantiated with input data about modified code files, branch creation settings, and more. Upon execution, the `run` method commits the changes to the repository based on the modified files, creating a new branch if enabled, and returns information about the base and target branches.