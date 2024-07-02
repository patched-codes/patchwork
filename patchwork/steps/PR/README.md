# Patchwork PR Module

## File: patchwork/steps/PR/PR.py

### Inputs
1. `PRInputs`: Required keys for PR instance.

### Outputs
1. Dictionary containing:
    - `base_branch`: Base branch for PR.
    - `target_branch`: Target branch for PR.
    - `pr_url`: URL of the created PR.
    - `pr_number`: Number of the created PR.
    - `pr_title`: Title of the created PR.
    - `pr_body`: Body of the created PR.

### Code
This Python file defines a class `PR` that extends a generic `Step` class. 
- It takes `inputs` as a parameter in its constructor, checks for missing keys, and then runs a series of steps involving `CommitChanges`, `PreparePR`, and `CreatePR` classes to create a new pull request (PR) in a repository.
- The `run` method orchestrates the execution of these steps and returns a dictionary with details of the PR created.


## File: patchwork/steps/PR/typed.py

### Inputs
1. `ModifiedCodeFile`: Annotated type for modified code files.

### Code
- This file contains definitions for `PRInputs`, `PROutputs`, and related types required for the PR process.
- `PRInputs` specifies required and optional inputs for the PR creation, including information related to CommitChanges, PreparePR, and CreatePR steps.


## File: patchwork/steps/PR/__init__.py

### Code
This file is empty and serves as an initialization point for the PR module.