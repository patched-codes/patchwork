# Commit Changes Class

The CommitChanges class is part of a larger step-based pipeline and is designed to handle Git commits with specified modifications. It makes use of the GitPython package to perform these git operations.

## Class Initializer (__init__)

### Inputs

The initializer of the CommitChanges class expects a dictionary input with the following keys:

- `modified_code_files`: A list of dictionaries where each dictionary must contain a path to the modified file. For example,
  `{'modified_code_files': [{'path': 'path/to/file1'}, {'path': 'path/to/file2'}]}`
  
Optional keys include:
- `disable_branch`: A flag to disable the creation of new branches. Default is `False` if not provided.
- `force_branch_creation`: A flag to force the creation of the new branch. Default is `True` if not provided.
- `branch_prefix`: A string to prefix the new branch name. Default is an empty string if not provided.
- `branch_suffix`: A string to suffix the new branch name. Default is an empty string if not provided.

Set the `disable_branch` to `True` if you don't want to create any branches. If a new branch is needed, either `branch_prefix` or `branch_suffix` should be provided.

### Class Variables

Upon successful completion, `__init__` sets several class variables:

- `enabled`: A boolean indicating if branch creation is enabled.
- `modified_code_files`: The list of code files to be modified.
- `force`: The `force_branch_creation` value determine whether to force creating the new branch.
- `branch_prefix` and `branch_suffix`: The prefix and suffix for the new branch name.

## Class Method (run)

The `run` method performs the commit operation based on the class variables set during initialization. It gets the git repository from the current working directory and commits modified files to branches as per the defined configuration.

### Outputs

- If branch creation is disabled (`self.enabled` is `False`), the `run` method returns a dictionary with a single key:
  - `target_branch`: The name of the currently active branch.
- If branch creation is enabled (`self.enabled` is `True`), the `run` method returns a dictionary with:
  - `base_branch`: The name of the original branch.
  - `target_branch`: The name of the new branch to which commits have been made.