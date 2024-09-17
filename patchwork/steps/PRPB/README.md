# patchwork/steps/PRPB Documentation

## Table of Contents
- [patchwork/steps/PRPB/PRPB.py](#patchworkstepsPRPBPRPB.py)
- [patchwork/steps/PRPB/typed.py](#patchworkstepsPRPBtyped.py)
- [patchwork/steps/PRPB/__init__.py](#patchworkstepsPRPB__init__.py)

---

## File: patchwork/steps/PRPB/PRPB.py

- **Extension**: .py
- **Size**: 1629 bytes
- **Created**: 2024-09-17 10:06:22
- **Modified**: 2024-09-17 10:06:22

### Description
This file defines the `PRPB` class, which inherits from `Step` and integrates functionalities for handling pull requests (PRs). It uses the `PRPBInputs` and `PRPBOutputs` classes for defining its inputs and outputs. The class converts input data into a format suitable for the PR operations and then runs PR-related functionalities.

### Inputs
#### PRPBInputs Class
- **Required:**
  - `modified_files`: List of dictionaries representing modified files.
  - `path_key`: String key used for the path in `modified_files`.

- **Optional:**
  - `comment_title_key`: String key for the commit message title.
  - `comment_message_key`: String key for the commit message.
  - **Commit Changes Configs:**
    - `disable_branch`: Boolean flag to disable branch creation.
    - `force_branch_creation`: Boolean flag to force branch creation.
    - `branch_prefix`: String for branch prefix.
    - `branch_suffix`: String for branch suffix.
  - **PR Preparation Configs:**
    - `pr_header`: String for PR header.
  - **PR Creation Configs:**
    - `pr_title`: String for PR title.
    - `force_pr_creation`: Boolean flag to force PR creation.
    - `disable_pr`: Boolean flag to disable PR.
    - `scm_url`: String for Source Control Management URL.
    - `gitlab_api_key`: String for GitLab API key.
    - `github_api_key`: String for GitHub API key.

### Outputs
#### PRPBOutputs Class
- **Commit Changes Outputs:**
  - `base_branch`: String representing the base branch name.
  - `target_branch`: String representing the target branch name.
  
- **PR Preparation Outputs:**
  - `pr_body`: String for the body of the PR.
  
- **PR Creation Outputs:**
  - `pr_url`: String representing the URL of the created PR.

### Key Functionalities
1. **Initialization**: Initializes the PRPB instance and converts input data for PR operations.
2. **Run Method**: Executes the PR-related operations and returns the outputs.

---

## File: patchwork/steps/PRPB/typed.py

- **Extension**: .py
- **Size**: 1348 bytes
- **Created**: 2024-09-17 10:06:22
- **Modified**: 2024-09-17 10:06:22

### Description
This file defines typed dictionaries for the inputs and outputs of the `PRPB` step. These are used to strongly type the configuration for PRPB operations.

### PRPBInputs Class
- **Inherits**: `TypedDict`
- **Required**: 
  - `modified_files`: List of dictionaries.
  - `path_key`: String.
- **Optional Configurations**:
  - *Commit*: disable_branch, force_branch_creation, branch_prefix, branch_suffix.
  - *PR Preparation*: pr_header.
  - *PR Creation*: pr_title, force_pr_creation, disable_pr, scm_url, gitlab_api_key, github_api_key.
  
### PRPBOutputs Class
- **Inherits**: `TypedDict`
- **Defined Fields**:
  - `base_branch`: String.
  - `target_branch`: String.
  - `pr_body`: String.
  - `pr_url`: String.

---

## File: patchwork/steps/PRPB/__init__.py

- **Extension**: .py
- **Size**: 0 bytes
- **Created**: 2024-09-17 10:06:22
- **Modified**: 2024-09-17 10:06:22

### Description
This is an empty file generally used to mark the directory as a package. No specific logic or functionalities are defined.

---

### Usage
To use the `PRPB` class in the context of a PR workflow:
1. **Instantiate** `PRPB` with the required inputs.
2. **Run** the instance to execute the PR-related tasks.
3. Collect the **outputs** which provide information about the PR operation results.