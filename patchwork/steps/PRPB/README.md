# PRPB Module Documentation

## Contents
- [File: patchwork/steps/PRPB/PRPB.py](#file-patchworkstepsprpbprpbpy)
- [File: patchwork/steps/PRPB/typed.py](#file-patchworkstepsprpbtypedpy)
- [File: patchwork/steps/PRPB/__init__.py](#file-patchworkstepsprpb__init__py)

## File: patchwork/steps/PRPB/PRPB.py

### Description
This script defines the `PRPB` class that extends the `Step` class. Its main functionality is to manage the process of preparing and handling pull requests and patches. It takes various inputs to customize the commit messages, paths, and other PR-related attributes. After processing the input data, it uses an instance of the `PR` class to perform the actual PR operations.

### Code
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

### Inputs
- **`path_key`** (`str`): Key used to map the path of modified files.
- **`comment_title_key`** (`str`, optional): Key for mapping commit message titles.
- **`comment_message_key`** (`str`, optional): Key for mapping patch messages.
- **`modified_files`** (`list` | `dict` | `str`): List, dictionary, or string denoting modified files.

### Outputs
- The output is derived from the `PR` class and encapsulated by `PRPBOutputs`.

### Usage
Use this class in a workflow where you need to process and manage pull requests that involve multiple modified files and custom commit messages.

## File: patchwork/steps/PRPB/typed.py

### Description
This script defines the input and output type definitions for the `PRPB` class. It uses `TypedDict` from `typing_extensions` to specify required and optional fields for inputs and outputs.

### Code
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

### Inputs
#### Required
- **`modified_files`** (`List[Dict]`): List of dictionaries describing modified files.
- **`path_key`** (`str`): Key to identify paths in the modified files.

#### Optional
- **`comment_title_key`** (`str`): Key for commit message titles.
- **`comment_message_key`** (`str`): Key for commit message bodies.
- **`disable_branch`** (`bool`): Flag to disable branch creation.
- **`force_branch_creation`** (`bool`): Flag to force branch creation.
- **`branch_prefix`** (`str`): Prefix for branch names.
- **`branch_suffix`** (`str`): Suffix for branch names.
- **`pr_header`** (`str`): Header for the pull request.
- **`pr_title`** (`str`): Title for the pull request.
- **`force_pr_creation`** (`bool`): Flag to force PR creation.
- **`disable_pr`** (`bool`): Flag to disable PR creation.
- **`scm_url`** (`str`): SCM URL.
- **`gitlab_api_key`** (`str`): GitLab API key.
- **`github_api_key`** (`str`): GitHub API key.

### Outputs
- **`base_branch`** (`str`): Base branch name.
- **`target_branch`** (`str`): Target branch name.
- **`pr_body`** (`str`): Body content of the pull request.
- **`pr_url`** (`str`): URL of the pull request.

### Usage
These type definitions should be used to validate and ensure the integrity of the inputs and outputs for the `PRPB` class.

## File: patchwork/steps/PRPB/__init__.py

### Description
This is an empty file, likely serving as an initializer for the `patchwork.steps.PRPB` module.

### Code
```python

```

### Usage
Include this file to mark the directory as a package for easier module imports.