# `patchwork/steps/PRPB` Code Documentation

## Files Overview

### [patchwork/steps/PRPB/typed.py](#patchworkstepsPRPBtyped.py)
This file comprises type definitions and annotations for the inputs and outputs related to preparing a pull request in a consistent and structured manner.

### [patchwork/steps/PRPB/__init__.py](#patchworkstepsPRPB__init__.py)
This file is an initialization module for the PRPB step. It doesn't contain any code but serves as a package marker.

### [patchwork/steps/PRPB/PRPB.py](#patchworkstepsPRPBPRPB.py)
This file defines the main `PRPB` class that extends a generic `Step` class, encapsulating the logic to prepare and manage pull requests using the inputs from the `typed.py` file.

## File: `patchwork/steps/PRPB/typed.py`

- **Extension**: .py
- **Size**: 1348 bytes
- **Created**: 2024-08-27 00:00:31
- **Modified**: 2024-08-27 00:00:31

### Contents

#### Import Statements
```python
from typing_extensions import Annotated, Dict, List, TypedDict
from patchwork.common.utils.step_typing import StepTypeConfig
```

#### Input Type Definitions
```python
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
```

#### Output Type Definitions
```python
class PRPBOutputs(TypedDict):
    base_branch: str
    target_branch: str
    pr_body: str
    pr_url: str
```

## File: `patchwork/steps/PRPB/__init__.py`

- **Extension**: .py
- **Size**: 0 bytes
- **Created**: 2024-08-27 00:00:31
- **Modified**: 2024-08-27 00:00:31

### Contents

This file is currently empty but serves as a package initializer.

```python

```

## File: `patchwork/steps/PRPB/PRPB.py`

- **Extension**: .py
- **Size**: 1629 bytes
- **Created**: 2024-08-27 00:00:31
- **Modified**: 2024-08-27 00:00:31

### Contents

#### Import Statements
```python
from patchwork.step import Step
from patchwork.steps import PR
from patchwork.steps.PRPB.typed import PRPBInputs, PRPBOutputs
```

#### `PRPB` Class Definition
```python
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

### How to Use

1. **Define Inputs**: Create a dictionary or input object consistent with `PRPBInputs` structure.
2. **Initialize**: Instantiate the `PRPB` class using the defined inputs.
3. **Run the Step**: Invoke the `run` method to perform the pull request handling and retrieve the outputs as defined in `PRPBOutputs`.

### Inputs

- **modified_files**: List of dictionaries containing file modifications metadata.
- **path_key**: Key string for the file path in the modified files.
- **comment_title_key**: (Optional) Key for comment title.
- **comment_message_key**: (Optional) Key for comment message.
- **disable_branch**: (Optional) Configuration to disable branch creation.
- **force_branch_creation**: (Optional) Force branch creation.
- **branch_prefix**: (Optional) Prefix for the branch name.
- **branch_suffix**: (Optional) Suffix for the branch name.
- **pr_header**: (Optional) Header for the pull request.
- **pr_title**: (Optional) Title for the pull request.
- **force_pr_creation**: (Optional) Force pull request creation.
- **disable_pr**: (Optional) Disable pull request generation.
- **scm_url**: URL for Source Code Management.
- **gitlab_api_key**: API key for GitLab.
- **github_api_key**: API key for GitHub.

### Outputs

- **base_branch**: Name of the base branch.
- **target_branch**: Name of the target branch.
- **pr_body**: Body content of the pull request.
- **pr_url**: URL to the created pull request.

### Notes

- The primary class `PRPB` extends `Step` and manages the creation and preparation of pull requests using a structured input configuration and outputs the relevant details.
- This module operates in contexts where automation of pull requests is required, likely integrating with systems like GitHub or GitLab.