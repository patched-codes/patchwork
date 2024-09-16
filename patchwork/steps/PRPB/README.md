# Documentation

## patchwork/steps/PRPB/PRPB.py

### Overview
This file contains the implementation of a `PRPB` step which extends the `Step` class. The `PRPB` class is designed to process pull request (PR) related inputs and manipulate modified files accordingly before passing them along to another `PR` step.

### Inputs
- `inputs`: Dictionary containing configuration and paths for modified files.
    - Required:
        - `modified_files`: List of dictionaries, each representing a modified file.
        - `path_key`: Key for accessing the file path in `modified_files`.
    - Optional:
        - `title_key`: Key for retrieving commit message title (mapped to `commit_message`).
        - `message_key`: Key for retrieving commit message body (mapped to `patch_message`).
        - Various configuration parameters as defined in `PRPBInputs`.

### Outputs
The class processes modified files based on the input `key_map` and `inputs`. The processed modified files are then passed to the `PR` class and the outputs from `PR` are returned.

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

---

## patchwork/steps/PRPB/typed.py

### Overview
This file defines types for inputs and outputs used by the `PRPB` step. These types enforce structure and provide annotations for configuration.

### Inputs
- `PRPBInputs`: Extends from `TypedDict` and includes:
    - Required:
        - `modified_files`: List of dictionaries with modification details.
        - `path_key`: Key used to access file paths.
    - Optional but Configurable:
        - `comment_title_key`: Key for commit message title.
        - `comment_message_key`: Key for commit message body.
        - Additional configuration parameters (e.g., branch name settings, PR header, SCM URL, API keys).

### Outputs
- `PRPBOutputs`: Typeddict defining required output fields:
    - `base_branch`: The branch from which the changes are made.
    - `target_branch`: The branch targeted by the PR.
    - `pr_body`: The body content of the PR.
    - `pr_url`: The URL of the created PR.

### Code
```python
from typing_extensions import Annotated, Dict, List, TypedDict
from patchwork.common.utils.step_typing import StepTypeConfig


class __PRPBInputsRequired(TypedDict):
    # CommitChangesInputs & PreparePRInputs
    modified_files: List[Dict]
    path_key: str


class PRPBInputs(__PRPBInputsRequired, total=False):
    comment_title_key: str
    comment_message_key: str
    # CommitChangesInputs
    disable_branch: Annotated[bool, StepTypeConfig(is_config=True)]
    force_branch_creation: Annotated[bool, StepTypeConfig(is_config=True)]
    branch_prefix: Annotated[str, StepTypeConfig(is_config=True)]
    branch_suffix: Annotated[str, StepTypeConfig(is_config=True)]
    # PreparePRInputs
    pr_header: Annotated[str, StepTypeConfig(is_config=True)]
    # CreatePRInputs
    pr_title: Annotated[str, StepTypeConfig(is_config=True)]
    force_pr_creation: Annotated[bool, StepTypeConfig(is_config=True)]
    disable_pr: Annotated[bool, StepTypeConfig(is_config=True)]
    scm_url: Annotated[str, StepTypeConfig(is_config=True)]
    gitlab_api_key: Annotated[str, StepTypeConfig(is_config=True)]
    github_api_key: Annotated[str, StepTypeConfig(is_config=True)]


class PRPBOutputs(TypedDict):
    # CommitChangesOutputs
    base_branch: str
    target_branch: str
    # PreparePROutputs
    pr_body: str
    # CreatePROutputs
    pr_url: str
```

---

## patchwork/steps/PRPB/__init__.py

### Overview
The `__init__.py` file in the `PRPB` package is an empty file, commonly used to mark the directory as a Python package.

### Code
```python

```