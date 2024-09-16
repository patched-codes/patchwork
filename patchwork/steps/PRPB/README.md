# Documentation for Patchwork PRPB Module

## Overview

This module is designed to facilitate creating a set of modified files and executing a Pull Request (PR) creation process. It includes classes and types to ensure precise handling of inputs and outputs.

### Structure

- `patchwork/steps/PRPB/PRPB.py`: Main logic for preparing and processing Pull Requests.
- `patchwork/steps/PRPB/typed.py`: Defines typed dictionaries for input and output formats.
- `patchwork/steps/PRPB/__init__.py`: Initializes the PRPB package (empty).

---

## Patchwork PRPB Step Class Implementation

### File: `patchwork/steps/PRPB/PRPB.py`

#### Overview

This file contains the definition of the `PRPB` class, which extends the `Step` class to manage the preparation and running of a PR creation process.

#### Inputs

The `PRPB` class requires the following inputs:
- `path_key` (str): Key to map the file path.
- `modified_files` (list): A list of dictionaries containing modified file data.
- Optional keys for commit messages: `title_key`, `message_key`.
  
Additional configuration inputs can be:
- Branch-related configurations (`disable_branch`, `force_branch_creation`, `branch_prefix`, `branch_suffix`).
- PR-related configurations (`pr_header`, `pr_title`, `force_pr_creation`, `disable_pr`, `scm_url`, `gitlab_api_key`, `github_api_key`).

#### Outputs

The `PRPB.run` method provides the following outputs:
- `base_branch` (str): The base branch name.
- `target_branch` (str): The target branch name.
- `pr_body` (str): The body content of the PR.
- `pr_url` (str): The URL of the created pull request.

### Example Usage

First, initialize the `PRPB` class with the required inputs:

```python
inputs = {
    "path_key": "path/to/modified/file",
    "modified_files": [{"path": "file1.py"}, {"path": "file2.py"}],
    "title_key": "Update title",
    "message_key": "Detailed commit message",
    "disable_branch": True,
    "pr_title": "New PR Title"
    # other optional inputs...
}

prpb_instance = PRPB(inputs)
```

Then, execute the PR creation process:

```python
pr_outputs = prpb_instance.run()
print(pr_outputs)
```

---

## Patchwork PRPB Typed Definitions

### File: `patchwork/steps/PRPB/typed.py`

#### Overview

Defines typed dictionaries for structured inputs and outputs used by the `PRPB` class.

#### Classes

- `PRPBInputs`: Extended typed dictionary defining all required and optional inputs for PRPB.
- `PRPBOutputs`: Typed dictionary defining the expected outputs.

#### Example of Input Definition

```python
class PRPBInputs(__PRPBInputsRequired, total=False):
    comment_title_key: str
    comment_message_key: str
    disable_branch: Annotated[bool, StepTypeConfig(is_config=True)]
    force_branch_creation: Annotated[bool, StepTypeConfig(is_config=True)]
    branch_prefix: Annotated[str, StepTypeConfig(is_config=True)]
    branch_suffix: Annotated[str, StepTypeConfig(is_config=True)]
    pr_header: Annotated[str, StepTypeConfig(is_config=True)]
    pr_title: Annotated[str, StepTypeConfig(is_config=True)]
    force_pr_creation: Annotated[bool, StepTypeConfig(is_config=True)]
    disable_pr: Annotated[bool, StepTypeConfig(is_config=True)]
    scm_url: Annotated[str, StepTypeConfig(is_config=True)]
    gitlab_api_key: Annotated[str, StepTypeConfig(is_config=True)]
    github_api_key: Annotated[str, StepTypeConfig(is_config=True)]
```

#### Example of Output Definition

```python
class PRPBOutputs(TypedDict):
    base_branch: str
    target_branch: str
    pr_body: str
    pr_url: str
```

---

## Initialization File

### File: `patchwork/steps/PRPB/__init__.py`

This is an empty initialization file to mark the directory as a package.

```python

```

This modular approach ensures that user inputs are validated and correctly formatted before being processed, and the outputs provide necessary information about the PR creation process.