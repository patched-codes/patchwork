# PR Step Module

This module defines the `PR` class that represents the step for creating a Pull Request in a development workflow. The class takes inputs, runs necessary steps like committing changes and preparing the PR, and then creates the PR. It ensures all required data is present before proceeding with the operation.

## Inputs
- `inputs`: A dictionary containing various configuration parameters required for creating a PR. These parameters include details related to modified code files, branch settings, PR header, PR title, SCM URL, and API keys.

## Outputs
The `PR` class produces a dictionary with the following keys:
- `base_branch`: The base branch for the PR.
- `target_branch`: The target branch for the PR.
- `pr_url`: The URL of the created PR.
- `pr_number`: The number associated with the created PR.
- `pr_title`: The title of the created PR.
- `pr_body`: The body content of the created PR.

The class is dependent on other modules like `CommitChanges`, `CreatePR`, and `PreparePR`, and certain required keys and data structures defined in the `typed.py` module to execute the PR creation process correctly.