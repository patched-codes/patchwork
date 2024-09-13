# Documentation

## patchwork/steps/PRPB/PRPB.py

### Overview
This script defines the `PRPB` class, which extends the `Step` class, and is intended to process pull request preparation and execution based on provided inputs. This class converts input data into a format suitable for creating pull requests and then uses the `PR` step class to execute the pull request creation.

### Inputs
The `PRPB` class uses inputs from the `PRPBInputs` class, which include:
- **required:** 
  - `path_key` (str): A key for the file path.
  - `modified_files` (List[Dict]): A list of dictionaries defining modified files.
- **optional:**
  - `comment_title_key` (str): A key for the comment title.
  - `comment_message_key` (str): A key for the comment message.
  - Other configuration options such as `disable_branch`, `branch_prefix`, `pr_header`, `pr_title`, `scm_url`, etc.

### Outputs
The `run` method of the `PRPB` class returns outputs defined in the `PRPBOutputs` class, including:
- `base_branch` (str)
- `target_branch` (str)
- `pr_body` (str)
- `pr_url` (str)

### Usage
Instantiate the `PRPB` class with the required and optional input parameters, then call the `run` method to execute the pull request creation process.

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

## patchwork/steps/PRPB/typed.py

### Overview
This file defines the input and output types for the `PRPB` class using Python's `TypedDict` and `Annotated` from `typing_extensions`. 

### Inputs
- **required:** 
  - `modified_files` (List[Dict]): List of dictionaries representing modified files.
  - `path_key` (str): Key for the file path.
- **optional:**
  - `comment_title_key` (str)
  - `comment_message_key` (str)
  - Other PR creation and branch configuration parameters (e.g., `pr_title`, `scm_url`, `disable_branch`, etc.)

### Outputs
The `PRPBOutputs` class defines expected outputs:
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

## patchwork/steps/PRPB/__init__.py

### Overview
This file is an empty `__init__.py` file, indicating that the `PRPB` directory can be treated as a module.

### Code
```python

```