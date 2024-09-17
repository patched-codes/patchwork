# Documentation for `patchwork/steps/PRPB`

## File: `patchwork/steps/PRPB/PRPB.py`

### Description
This Python file defines the `PRPB` class, which is a step in the patchwork pipeline that extends the base `Step` class. The purpose of the `PRPB` class is to handle the input data that includes information about modified files and mapping keys, and to pass this data to a `PR` step to perform the intended operation, likely related to pull requests (PR).

### Inputs
- **inputs**: A dictionary containing several key-value pairs required by the `PRPB` class and the `PR` class it interacts with.
  - `modified_files` (List\[Dict\] | Dict | str): A list of dictionaries, a single dictionary, or a string representing files that have been modified.
  - `path_key` (str): The key that maps the file path.
  - `title_key` (str, optional): The key that maps the commit message title.
  - `message_key` (str, optional): The key that maps the commit message content.

### Outputs
- **run()**: This method executes the `PR` step with the formatted input data.
  - **Returns**: The result of the `PR` step, which likely includes details of the created or modified PR.

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

## File: `patchwork/steps/PRPB/typed.py`

### Description
This file defines the typing for the inputs and outputs expected by the `PRPB` class. It uses Python's `TypedDict` and `Annotated` from `typing_extensions` to create structured types for input validation and configuration.

### Inputs
- `PRPBInputs`: Extends from `__PRPBInputsRequired` and adds several optional configuration fields.
  - `modified_files` (List\[Dict\]): A list of dictionaries indicating modified files.
  - `path_key` (str): Key for the file path.
  - Optional fields include `comment_title_key`, `comment_message_key`, as well as various boolean flags and configuration strings related to branch and PR handling.

### Outputs
- `PRPBOutputs`: A dictionary that defines the expected output keys and their types.
  - `base_branch` (str)
  - `target_branch` (str)
  - `pr_body` (str)
  - `pr_url` (str)

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

## File: `patchwork/steps/PRPB/__init__.py`

### Description
This is an empty initialization file to make the `PRPB` module a recognized Python package.

### Code
```python

```
