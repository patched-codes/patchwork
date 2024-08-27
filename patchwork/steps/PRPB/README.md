# Documentation for `patchwork/steps/PRPB`

## Introduction
The `patchwork/steps/PRPB` directory contains Python scripts integral to the PRPB (Pull Request and Patch Builder) process. This system is designed to automate the creation and management of pull requests, particularly focusing on the transformation of file modifications into a structured PR.

## Files Summary

### 1. File: `patchwork/steps/PRPB/typed.py`

#### Overview
This script defines the input and output types for the PRPB system using `TypedDict` from `typing_extensions` and `Annotated` from `patchwork.common.utils.step_typing`.

#### Inputs
Defined in `PRPBInputs`, these are composite data types derived from multiple PR-related inputs:
- **Required Inputs**
  - `modified_files`: A list of dictionaries representing the files modified.
  - `path_key`: A string indicating the key for the path.
- **Optional Inputs**
  - PR Comment Configuration:
    - `comment_title_key`: Key for the title in the comment.
    - `comment_message_key`: Key for the message in the comment.
  - Commit Changes Configuration:
    - `disable_branch`: Boolean to disable branch creation.
    - `force_branch_creation`: Boolean to force branch creation.
    - `branch_prefix`: Prefix for branch name.
    - `branch_suffix`: Suffix for branch name.
  - Prepare PR Configuration:
    - `pr_header`: Header for the Pull Request.
  - Create PR Configuration:
    - `pr_title`: Title of the Pull Request.
    - `force_pr_creation`: Boolean to force PR creation.
    - `disable_pr`: Boolean to disable PR creation.
    - `scm_url`: URL for Source Code Management.
    - `gitlab_api_key`: API key for GitLab.
    - `github_api_key`: API key for GitHub.

#### Outputs
Defined in `PRPBOutputs`, capturing the result details:
  - `base_branch`: Base branch name.
  - `target_branch`: Target branch name.
  - `pr_body`: Body content of the Pull Request.
  - `pr_url`: URL of the created Pull Request.

```python
from typing_extensions import Annotated, Dict, List, TypedDict
from patchwork.common.utils.step_typing import StepTypeConfig

class __PRPBInputsRequired(TypedDict):
    modified_files: List[Dict]
    path_key: str

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

class PRPBOutputs(TypedDict):
    base_branch: str
    target_branch: str
    pr_body: str
    pr_url: str
```

### 2. File: `patchwork/steps/PRPB/__init__.py`

#### Overview
This file appears to be an empty initialization script used to mark the directory as a Python package.

### Code
```python

```

### 3. File: `patchwork/steps/PRPB/PRPB.py`

#### Overview
This script is the main implementation of the PRPB system. It extends the `Step` base class to process the inputs, convert and validate modified files, and orchestrate the pull request creation using the `PR` class.

#### Inputs
- Named inputs from `PRPBInputs` covering modified files, branching, and PR configuration options.

#### Functionality
- **Initialization (`__init__` method)**:
  - Maps provided file keys to the expected structure.
  - Validates and transforms the `modified_files` to ensure it has the necessary fields.
  - Sets up the inputs for processing.

- **Execution (`run` method)**:
  - Creates an instance of the `PR` class with the appropriately transformed inputs.
  - Calls the `run` method on the `PR` instance to create the PR.
  - Returns the outputs from the `PR` runner.

#### Outputs
- The method returns outputs in the form of `PRPBOutputs` which includes branch names and PR details.

```python
from patchwork.step import Step
from patchwork.steps import PR
from patchwork.steps.PRPB.typed import PRPBInputs, PRPBOutputs

class PRPB(Step, input_class=PRPBInputs, output_class=PRPBOutputs):
    def __init__(self, inputs):
        super().__init__(inputs)
        key_map = dict(path=inputs["path_key"])
        if inputs.get("title_key") is not None:
            key_map["commit_message"] = inputs["comment_title_key"]
        if inputs.get("message_key") is not None:
            key_map["patch_message"] = inputs["comment_message_key"]

        self.modified_files = []
        input_modified_files = inputs.get("modified_files")
        if isinstance(input_modified_files, list):
            for modified_file in input_modified_files:
                converted_modified_file = {key: modified_file.get(mapped_key) for key, mapped_key in key_map.items()}
                if converted_modified_file.get("path") is None:
                    continue
                self.modified_files.append(converted_modified_file)
        elif isinstance(input_modified_files, dict):
            converted_modified_file = {key: input_modified_files.get(mapped_key) for key, mapped_key in key_map.items()}
            self.modified_files.append(converted_modified_file)
        elif isinstance(input_modified_files, str):
            converted_modified_file = {"path": input_modified_files}
            self.modified_files.append(converted_modified_file)
        self.inputs = inputs

    def run(self):
        pr = PR({**self.inputs, "modified_code_files": self.modified_files})
        pr_outputs = pr.run()

        return pr_outputs
```