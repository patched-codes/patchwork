# Documentation: patchwork/steps/PRPB

## File: patchwork/steps/PRPB/typed.py

### Description
Defines the input and output types for the PRPB step, leveraging Python's type annotations for better clarity and type safety.

### Inputs
- **PRPBInputs**:
  - **Required**:
    - `modified_files`: List of dictionaries detailing the modified files.
    - `path_key`: A string key representing the path.
  - **Optional**:
    - `comment_title_key`: A string key for the comment title.
    - `comment_message_key`: A string key for the comment message.
    - **CommitChangesInputs**:
      - `disable_branch`: Boolean flag indicating if branch creation should be disabled.
      - `force_branch_creation`: Boolean flag to force branch creation.
      - `branch_prefix`: String prefix for branch names.
      - `branch_suffix`: String suffix for branch names.
    - **PreparePRInputs**:
      - `pr_header`: String header for Pull Request (PR).
    - **CreatePRInputs**:
      - `pr_title`: String title for the PR.
      - `force_pr_creation`: Boolean flag to force PR creation.
      - `disable_pr`: Boolean flag to disable PR.
      - `scm_url`: URL for Source Control Management (SCM).
      - `gitlab_api_key`: GitLab API key.
      - `github_api_key`: GitHub API key.

### Outputs
- **PRPBOutputs**:
  - **CommitChangesOutputs**:
    - `base_branch`: Base branch name as a string.
    - `target_branch`: Target branch name as a string.
  - **PreparePROutputs**:
    - `pr_body`: Body text for the PR.
  - **CreatePROutputs**:
    - `pr_url`: URL of the created PR.

## File: patchwork/steps/PRPB/__init__.py

### Description
An empty initialization file for the PRPB module. This file is used to mark the directory as a Python package.

### Inputs
- None

### Outputs
- None

## File: patchwork/steps/PRPB/PRPB.py

### Description
Implements the PRPB (Pull Request Preparation & Branching) step, which integrates various functionalities related to commit changes, preparing, and creating pull requests.

### Inputs
- Initializes with an **inputs** dictionary conforming to `PRPBInputs`.

### Outputs
- Returns a dictionary conforming to `PRPBOutputs` after executing the `run` method.

### Code Functionality
- **Initialization (`__init__` method)**:
  - Maps input keys to their respective values based on provided keys.
  - Handles different types of input formats (`list`, `dict`, `str`) for modified files and converts them to a unified format.
- **Execution (`run` method)**:
  - Creates a `PR` instance with the modified inputs.
  - Executes the PR step and returns its outputs.

### Usage
Users can create an instance of `PRPB` by providing an appropriate `PRPBInputs` dictionary. They can then call the `run` method to perform the steps related to preparing and creating a Pull Request.

```python
from patchwork.steps.PRPB.PRPB import PRPB

inputs = {
    "modified_files": [{"path": "file_path", "key": "value"}],
    "path_key": "path",
    "comment_title_key": "title",
    "comment_message_key": "message",
    # Other optional input fields...
}

prpb_instance = PRPB(inputs)
outputs = prpb_instance.run()
print(outputs)
```

This setup ensures that all required preparations and actions for a Pull Request are systematically carried out, returning useful outputs like the PR URL and branch details.