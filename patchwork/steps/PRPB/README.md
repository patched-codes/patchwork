# Documentation for `patchwork/steps/PRPB`

## Files Included
- [typed.py](#file-typedpy)
- [__init__.py](#file-__init__py)
- [PRPB.py](#file-prpbpy)

## File: typed.py

### Overview
This file defines the input and output data structures for the `PRPB` step using `TypedDict` from the `typing_extensions` module. It also uses the `Annotated` type to specify configurations.

### Inputs
1. **Required Inputs**
   - `modified_files`: A list of dictionaries representing the files that have been modified.
   - `path_key`: A string key to access file paths in `modified_files`.

2. **Optional Inputs**
   - PR Comment Keys:
     - `comment_title_key`: String key for the title of the commit message.
     - `comment_message_key`: String key for the message of the commit.
   - Commit Change Configurations:
     - `disable_branch`: Boolean to disable branch creation.
     - `force_branch_creation`: Boolean to force branch creation.
     - `branch_prefix`: String prefix for the branch name.
     - `branch_suffix`: String suffix for the branch name.
   - PR Preparation Configurations:
     - `pr_header`: String header for the PR.
   - Create PR Configurations:
     - `pr_title`: String title for the PR.
     - `force_pr_creation`: Boolean to force PR creation.
     - `disable_pr`: Boolean to disable PR creation.
     - `scm_url`: String URL for source control management.
     - `gitlab_api_key`: String API key for GitLab.
     - `github_api_key`: String API key for GitHub.

### Outputs
- **CommitChangesOutputs**
  - `base_branch`: The base branch name.
  - `target_branch`: The target branch name.
- **PreparePROutputs**
  - `pr_body`: Body of the PR.
- **CreatePROutputs**
  - `pr_url`: URL of the created PR.

## File: __init__.py

### Overview
This is an empty file, typically used to mark the directory as a Python package.

## File: PRPB.py

### Overview
This file defines the `PRPB` class, which is a specialized `Step` that integrates with PR steps and handles specific input and output structures.

### Key Components
1. **Class Definition**
   - The `PRPB` class inherits from `Step` and uses `PRPBInputs` for its inputs and `PRPBOutputs` for its outputs.

2. **Initialization (`__init__` method)**
   - Maps keys for modified files.
   - Converts input `modified_files` into a standardized format, ensuring each file has a `path`.

3. **Run Method (`run` method)**
   - Instantiates a `PR` object with the prepared `inputs` and `modified_files`.
   - Executes the `run` method of the `PR` object.
   - Returns the outputs from the `PR` step.

### Example Usage
```python
inputs = {
    "modified_files": [{"path": "file1.txt"}],
    "path_key": "path",
    "pr_title": "New PR Title",
    "scm_url": "https://github.com/example/repo",
    "github_api_key": "examplekey123",
    # additional config inputs...
}

prpb = PRPB(inputs)
outputs = prpb.run()
print(outputs["pr_url"])  # URL of the created PR
```

This documentation provides an overview of the purpose and usage of each file within the `patchwork/steps/PRPB` directory, facilitating a better understanding for developers interacting with this module.