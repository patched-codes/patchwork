# PR Step Implementation

## Inputs
- The `PR` class requires specific input keys defined in `PRInputs`.
- The required keys involve details like modified code files, branch settings, PR header, PR title, API keys, etc.

## Outputs
- The `PR` class returns a dictionary containing base branch, target branch, PR URL, PR number, PR title, and PR body.
- These values are obtained by executing steps to commit changes, prepare a PR, and create a PR.

This code snippet shows the implementation of a `PR` step within a patchwork system that automates the process of creating a Pull Request (PR) for code changes. The `PR` class handles required inputs, runs necessary steps such as committing changes, preparing a PR, and creating a PR, and finally returns relevant information needed for the PR creation process.