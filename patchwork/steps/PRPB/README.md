# Documentation: patchwork/steps/PRPB

## File: patchwork/steps/PRPB/typed.py

### Overview

This file defines the input and output types for the PRPB step using Python's `typing` features, specifically `TypedDict` and annotations.

### Code Summary

- **Imports**: Imports from `typing_extensions` and other utility modules.
- **Input Class (`PRPBInputs`)**:
  - Inherits from `__PRPBInputsRequired` which includes required fields.
  - Optional fields are added using the `Annotated` type from `typing_extensions`, with meta-information provided by `StepTypeConfig`.
  - Configuration fields for branch handling (`disable_branch`, `force_branch_creation`, etc.), PR creation (`pr_title`, `force_pr_creation`, `disable_pr`, etc.), and SCM integration (`scm_url`, `gitlab_api_key`, `github_api_key`).
- **Output Class (`PRPBOutputs`)**:
  - Defines the expected outputs of the PRPB step, including branch information and PR details.

### Inputs

#### Required

- `modified_files`: List of dictionaries containing file modification details.
- `path_key`: A string key representing the path in the modified file dictionary.

#### Optional

- `comment_title_key`: Key for the comment title.
- `comment_message_key`: Key for the comment message.
- `disable_branch`, `force_branch_creation`, `branch_prefix`, `branch_suffix`, `pr_header`: Various branch and PR configuration strings or booleans.
- `pr_title`, `force_pr_creation`, `disable_pr`, `scm_url`, `gitlab_api_key`, `github_api_key`: Configuration for creating a PR and integrating with SCMs.

### Outputs

- `base_branch`: The base branch name.
- `target_branch`: The target branch name.
- `pr_body`: The body text of the PR.
- `pr_url`: URL of the created PR.

## File: patchwork/steps/PRPB/__init__.py

### Overview

This is an empty placeholder file. It indicates that the PRPB module is a package.

### Code Summary

No code content, just an empty file.

## File: patchwork/steps/PRPB/PRPB.py

### Overview

This file defines the main PRPB step, implementing the logic to process inputs, convert modified files into the required format, and run the PR step.

### Code Summary

- **Imports**: Imports required modules and classes.
- **Class (`PRPB`)**:
  - Inherits from `Step` and uses `PRPBInputs` for inputs and `PRPBOutputs` for outputs.
  - **`__init__` Method**: Initializes the class, processes inputs to convert modified files into the required format.
    - Processes modifications whether they're given as lists, dictionaries, or strings.
    - Maps keys for commit and patch messages if provided.
  - **`run` Method**: Creates a PR using the processed input data.
    - Instantiates a `PR` object with the modified files and other inputs.
    - Runs the `PR` and returns its outputs.

### Inputs

- Format as defined by `PRPBInputs`.

### Outputs

- The `run` method returns the output of the `PR` step, which aligns with `PRPBOutputs`.

### Usage

A user of this code would primarily:
1. Instantiate the `PRPB` class with appropriate inputs.
2. Call the `run` method to process the step and obtain the outputs.

Example:
```python
inputs = {
    "modified_files": [{"path": "file1.py", "change": "modified"}],
    "path_key": "path",
    # other configuration keys...
}
prpb_step = PRPB(inputs)
outputs = prpb_step.run()
```