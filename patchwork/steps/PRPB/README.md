# PRPB Module Documentation

## Overview

The `PRPB` module in the `patchwork.steps` package is designed to handle preparation and creation of Pull Requests (PRs) by extending the capabilities of the `Step` class. It processes the inputs to manage file modifications and initiates the PR creation process. This module includes several components distributed across different Python files.

## Files

### `patchwork/steps/PRPB/PRPB.py`

#### Contents

The primary class in this file is `PRPB`, which manages the operation of processing modified files and initiating a Pull Request.

#### Inputs

- `inputs`: An instance of `PRPBInputs`, which is a detailed dictionary allowing various configurations required for the PR process. This includes paths, commit messages, branch configurations, and API keys for GitHub or GitLab.

#### Outputs

- The `run` method returns an instance of `PRPBOutputs`, which includes details such as base and target branches, PR body, and PR URL.

#### Code Summary

```python
class PRPB(Step, input_class=PRPBInputs, output_class=PRPBOutputs):
    def __init__(self, inputs):
        super().__init__(inputs)
        # Mapping input keys to internal keys
        key_map = dict(path=inputs["path_key"])
        if inputs.get("title_key") is not None:
            key_map["commit_message"] = inputs["comment_title_key"]
        if inputs.get("message_key") is not None:
            key_map["patch_message"] = inputs["comment_message_key"]

        # Processing the modified files input
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
        self.set_status(pr.status, pr.status_message)
        return pr_outputs
```

### `patchwork/steps/PRPB/typed.py`

#### Contents

This file defines the structured types for the inputs and outputs used in the `PRPB` class.

#### Inputs

- `PRPBInputs`: This is a `TypedDict` that includes required fields such as `modified_files` and `path_key`, along with optional keys for commit messages, branch configurations, and SCM details.

#### Outputs

- `PRPBOutputs`: This `TypedDict` includes fields that capture the results of the PR operation, such as branch names, PR body, and PR URL.

#### Code Summary

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

class PRPBOutputs(TypedDict):
    base_branch: str
    target_branch: str
    pr_body: str
    pr_url: str
```

### `patchwork/steps/PRPB/__init__.py`

#### Contents

This file is currently an empty initializer for the `PRPB` module, ensuring that the parent directory is treated as a package.

#### Code Summary

```python

```

This documentation provides a comprehensive overview of the `PRPB` module, describing its purpose, key functions, inputs, and outputs, and summarizes the code and its components to help users understand how to utilize this module effectively.