# Documentation for Patchwork PRPB Module

## File: `patchwork/steps/PRPB/typed.py`

### Purpose
Defines typed dictionaries for specifying the input and output requirements of a "Pull Request Preparation and Branching" (PRPB) workflow.

### Inputs
- **Class: `PRPBInputs(LoggerRequired)`**
    - `modified_files`: List of dictionaries detailing modified files.
    - `path_key`: Key for accessing the path in the modified files.
    - Optional Keys for Commit, PR, and Branching:
        - `comment_title_key`
        - `comment_message_key`
        - `disable_branch`: Annotated as a configurable boolean.
        - `force_branch_creation`: Annotated as a configurable boolean.
        - `branch_prefix`: Annotated as a configurable string.
        - `branch_suffix`: Annotated as a configurable string.
        - `pr_header`: Annotated as a configurable string.
        - `pr_title`: Annotated as a configurable string.
        - `force_pr_creation`: Annotated as a configurable boolean.
        - `disable_pr`: Annotated as a configurable boolean.
        - `scm_url`: Annotated as a configurable string.
        - `gitlab_api_key`: Annotated as a configurable string.
        - `github_api_key`: Annotated as a configurable string.

### Outputs
- **Class: `PRPBOutputs`**
    - `base_branch`: Base branch name.
    - `target_branch`: Target branch name.
    - `pr_body`: Body of the PR.
    - `pr_url`: URL of the created PR.

---

## File: `patchwork/steps/PRPB/__init__.py`

### Purpose
This file is an initializer for the `PRPB` module. It is currently empty but can be used for module-level imports and initializations in the future.

---

## File: `patchwork/steps/PRPB/PRPB.py`

### Purpose
Implements the main functionality of the "Pull Request Preparation and Branching" workflow by transforming input data, executing a pull request operation, and returning the results.

### Inputs
- This class inherits from `Step` and utilizes `PRPBInputs` for its input schema.

### Outputs
- This class inherits from `Step` and utilizes `PRPBOutputs` for its output schema.

### Class: `PRPB`
- **Constructor `__init__(inputs)`**:
    - Takes `inputs` of type `PRPBInputs`.
    - Maps keys and processes the modified files based on input types (list, dict, or string).

- **Method `run()`**:
    - Initializes a `PR` step with the compiled inputs and modified files.
    - Executes the `PR` step.
    - Returns the outputs from the `PR` step.

### Usage
Users can create an instance of the `PRPB` class by providing the necessary inputs for PR creation and branching. The `run` method executes the PR process and returns the relevant outputs, such as the URL of the PR and details of branches created.

```python
from patchwork.steps.PRPB.PRPB import PRPB

inputs = {
    "modified_files": [{"path": "path/to/file", "key": "value"}],
    "path_key": "path",
    "comment_title_key": "commit_message",
    ...
}

prpb_instance = PRPB(inputs)
outputs = prpb_instance.run()
print(outputs)
```

---

This documentation covers the definitions, purpose, inputs, outputs, and potential usage of the "Pull Request Preparation and Branching" module located in the `patchwork/steps/PRPB` directory.