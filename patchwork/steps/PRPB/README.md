# Documentation

## Module: `patchwork/steps/PRPB`

This module is a part of the `patchwork` system and provides functionality related to Pull Request (PR) preparation and creation. The key components of this module are defined in the following three files:

1. [`typed.py`](#file-patchworkstepsprpbtypedpy)
2. [`__init__.py`](#file-patchworkstepsprpb__init__py)
3. [`PRPB.py`](#file-patchworkstepsprpbprpbpy)

### File: `patchwork/steps/PRPB/typed.py`

#### Description

This file defines the input and output data structures for the `PRPB` step using Python's type hinting and `TypedDict` from the `typing_extensions`.

#### Inputs

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
- **`modified_files`**: List of dictionaries representing modified files.
- **`path_key`**: Key to identify file path in modified files.
- **Optional Fields**: Include various configurations for branch and pull request creation such as `disable_branch`, `force_branch_creation`, `branch_prefix`, `branch_suffix`, `pr_header`, `pr_title`, `force_pr_creation`, `disable_pr`, `scm_url`, `gitlab_api_key`, `github_api_key`.

#### Outputs

```python
class PRPBOutputs(TypedDict):
    base_branch: str
    target_branch: str
    pr_body: str
    pr_url: str
```
- **`base_branch`**: The base branch for the pull request.
- **`target_branch`**: The target branch for the pull request.
- **`pr_body`**: The body content of the pull request.
- **`pr_url`**: The URL of the created pull request.

### File: `patchwork/steps/PRPB/__init__.py`

#### Description

This is an empty file that signifies the `PRPB` directory as a Python package. It is essential for the module system but does not contain any executable code or definitions.

### File: `patchwork/steps/PRPB/PRPB.py`

#### Description

This file defines the `PRPB` class, which is a step in the `patchwork` system. This class utilizes the data structures defined in `typed.py` and extends the `Step` class from `patchwork`.

#### Class Definition

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

#### Methods

- **`__init__(self, inputs)`**: Initializes the `PRPB` step with the provided inputs. It processes the `modified_files` input to generate a standardized list of modified files.
- **`run(self)`**: Runs the `PR` step with the processed inputs and returns the pull request outputs.

#### Usage

The `PRPB` class is used to prepare and create a pull request based on the provided input configurations and modified files. It would likely be used within a larger system for continuous integration or automated code management workflows.