## Overview
This documentation provides information about three Python files related to the creation of a Pull Request (PR) in a software development workflow using the Patchwork library.

---

## File: patchwork/steps/PR/PR.py

### Inputs
- Constructor takes `inputs` which should contain values for `modified_code_files`, `disable_branch`, `force_branch_creation`, `branch_prefix`, `branch_suffix`, `pr_header`, `pr_title`, `force_pr_creation`, `disable_pr`, `scm_url`, `gitlab_api_key`, and `github_api_key`.

### Outputs
- Upon running the `PR` class instance, it returns a dictionary with keys: `base_branch`, `target_branch`, `pr_url`, `pr_number`, `pr_title`, and `pr_body`. 

### Code Functionality
- The `PR` class orchestrates commits, prepares the PR details, and creates the PR using other related steps.
- It ensures the required keys are present in the inputs before proceeding.
- It fetches outputs from `CommitChanges`, `PreparePR`, and `CreatePR`, then constructs and returns the final result.

---

## File: patchwork/steps/PR/typed.py

### Code
- Defines TypedDictionaries for input and output structures related to the PR operation.
- Specifies the required and optional fields for `PRInputs` and the expected keys in the `PROutputs`.

---

## File: patchwork/steps/PR/__init__.py

### Code
- An empty file with no code.

---