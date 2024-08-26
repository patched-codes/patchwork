# Documentation for `patchwork/steps/PRPB`

This documentation provides details for the Python files within the `patchwork/steps/PRPB` directory. The files include `typed.py`, `__init__.py`, and `PRPB.py`.

## File: `patchwork/steps/PRPB/typed.py`

### Description
Defines the type definitions and configurations for the PRPB step, including required and optional inputs, as well as the expected outputs.

### Inputs

- **`PRPBInputs (TypedDict)`**
  - **Required Fields:**
    - `modified_files`: A list of dictionaries representing modified files.
    - `path_key`: A string that serves as a key for the file path.
  - **Optional Fields:**
    - `comment_title_key`: A string key for the comment title.
    - `comment_message_key`: A string key for the comment message.
    - **Configuration Settings (as annotated in `StepTypeConfig`):**
      - `disable_branch`: Boolean.
      - `force_branch_creation`: Boolean.
      - `branch_prefix`: String.
      - `branch_suffix`: String.
      - `pr_header`: String.
      - `pr_title`: String.
      - `force_pr_creation`: Boolean.
      - `disable_pr`: Boolean.
      - `scm_url`: String.
      - `gitlab_api_key`: String.
      - `github_api_key`: String.

### Outputs

- **`PRPBOutputs (TypedDict)`**
  - `base_branch`: String representing the base branch.
  - `target_branch`: String representing the target branch.
  - `pr_body`: String representing the body of the PR.
  - `pr_url`: String representing the PR URL.

## File: `patchwork/steps/PRPB/__init__.py`

### Description
This is an empty file commonly used to mark a directory as a Python package directory.

### Additional Information
- **Type**: .py
- **Size**: 0 bytes

No code is present in the file.

## File: `patchwork/steps/PRPB/PRPB.py`

### Description
Implements the PRPB step logic that relies on the `PR` step to process the given inputs and produce the expected outputs. This is achieved by converting the input modified files into a format acceptable by the PR step and invoking it.

### Inputs
- Takes in the class `PRPBInputs` defined in `typed.py`.

### Outputs
- Returns instances of `PRPBOutputs` defined in `typed.py`.

### Code Description
- **Class `PRPB`:**
  - Inherits from `Step`.
  - Uses `PRPBInputs` for its inputs and `PRPBOutputs` for its outputs.
  - **`__init__` Method:**
    - Initializes the class with the provided inputs.
    - Maps the input keys to standardized keys for further processing.
    - Handles and converts the `modified_files` based on their input type (list, dict, or str).
  - **`run` Method:**
    - Creates an instance of `PR` using the processed inputs.
    - Runs the PR instance and returns its output.

### Usage
Someone using this module would instantiate the `PRPB` class with necessary inputs and invoke the `run` method to process the pull/merge request and its associated operations.

```
from patchwork.steps.PRPB.PRPB import PRPB

prpb_instance = PRPB(inputs)
outputs = prpb_instance.run()
```

This code takes care of preparing and handling the necessary steps to create and manage a pull/merge request from a set of modified files, along with the associated metadata.