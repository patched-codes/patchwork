# Documentation for Files in patchwork/steps/PRPB/

## File: patchwork/steps/PRPB/PRPB.py

### Description
This file contains the `PRPB` class that extends the `Step` class and integrates with Pull Requests (PR). It processes input data related to modified files and initializes a PR object to execute the corresponding actions.

### Inputs
- **`inputs`**: A dictionary containing input data.
  - `path_key`: Key to map the path of modified files.
  - `title_key` (optional): Key to map the commit message title.
  - `message_key` (optional): Key to map the commit message body.
  - `modified_files`: List, dict, or string representing files modified in the patch.

### Outputs
- The `run` method initializes a PR object with processed input data and executes it, returning the outputs of the PR object's `run` method.

### Usage
The `PRPB` class is used as a step in a process where code modifications need to be prepared for a PR. It takes inputs related to file modifications and PR configurations, processes them, and uses the `PR` class to execute the PR creation.

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

## File: patchwork/steps/PRPB/typed.py

### Description
This file contains type definitions for the inputs and outputs of the `PRPB` step. It uses `TypedDict` to structure the data types clearly.

### Inputs
- **`PRPBInputs`**:
  - **Required attributes**:
    - `modified_files`: List of dictionaries representing files.
    - `path_key`: Key mapping the path of modified files.
  - **Optional attributes**:
    - `comment_title_key`: Key for commit message title.
    - `comment_message_key`: Key for commit message body.
    - Various configuration keys for branch and PR preparation.

### Outputs
- **`PRPBOutputs`**:
  - `base_branch`: Base branch name.
  - `target_branch`: Target branch name.
  - `pr_body`: Body of the PR.
  - `pr_url`: URL of the created PR.

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

## File: patchwork/steps/PRPB/__init__.py

### Description
This file is an empty `__init__.py` file used to mark the directory as a Python package.

### Code
```python

```