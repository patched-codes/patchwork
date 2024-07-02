# PR Steps Implementation

This code snippet provides the implementation for a PR (Pull Request) step as part of a larger framework. It is designed to automate the process of creating a PR on a version control system. The code is structured into different files in the `patchwork/steps/PR/` directory.

## Inputs
- The main PR class takes inputs defined in `PRInputs` from `typed.py`. These inputs include information required for creating a PR such as modified code files, branch details, PR title, and other configuration options.

## Outputs
- The `PR` class implements a `run` method that orchestrates the creation of a PR by invoking other steps like `CommitChanges`, `PreparePR`, and `CreatePR`. The output of running the PR step includes details like base branch, target branch, PR URL, PR number, PR title, and PR body.

The `PRInputs` and `PROutputs` structures defined in `typed.py` enforce the required inputs and expected outputs for the PR step, ensuring consistency and type safety in the workflow.