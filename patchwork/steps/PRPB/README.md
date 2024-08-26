# Documentation for PRPB Module

## Table of Contents
- [patchwork/steps/PRPB/typed.py](#patchworkstepsprpbtypedpy)
- [patchwork/steps/PRPB/__init__.py](#patchworkstepsprpb__init__py)
- [patchwork/steps/PRPB/PRPB.py](#patchworkstepsprpbprpbpy)

## File: patchwork/steps/PRPB/typed.py

- **Extension:** .py
- **Size:** 1348 bytes
- **Created:** 2024-08-26 18:49:15
- **Modified:** 2024-08-26 18:49:15

### Description
This file defines the input and output types for the PRPB step using Python’s `typing` module extensions. These types include all the necessary configurations for creating and managing pull requests, including configurations for branches and the source control management URLs.

### Inputs

- **PRPBInputs:**
  - `modified_files`: `List[Dict]` - List of files that have been modified.
  - `path_key`: `str` - Key for path mapping.
  - `comment_title_key`: `str` *(optional)* - Key for commit message title mapping.
  - `comment_message_key`: `str` *(optional)* - Key for commit message body mapping.
  - `disable_branch`: `bool` *(is_config=True, optional)* - Flag to disable branch creation.
  - `force_branch_creation`: `bool` *(is_config=True, optional)* - Flag to force branch creation.
  - `branch_prefix`: `str` *(is_config=True, optional)* - Prefix for the branch name.
  - `branch_suffix`: `str` *(is_config=True, optional)* - Suffix for the branch name.
  - `pr_header`: `str` *(is_config=True, optional)* - Header for the pull request.
  - `pr_title`: `str` *(is_config=True, optional)* - Title for the pull request.
  - `force_pr_creation`: `bool` *(is_config=True, optional)* - Flag to force PR creation.
  - `disable_pr`: `bool` *(is_config=True, optional)* - Flag to disable PR creation.
  - `scm_url`: `str` *(is_config=True, optional)* - URL for the source control management system.
  - `gitlab_api_key`: `str` *(is_config=True, optional)* - API key for GitLab.
  - `github_api_key`: `str` *(is_config=True, optional)* - API key for GitHub.

### Outputs

- **PRPBOutputs:**
  - `base_branch`: `str` - Base branch name.
  - `target_branch`: `str` - Target branch name.
  - `pr_body`: `str` - Body of the pull request.
  - `pr_url`: `str` - URL of the created pull request.

## File: patchwork/steps/PRPB/__init__.py

- **Extension:** .py
- **Size:** 0 bytes
- **Created:** 2024-08-26 18:49:15
- **Modified:** 2024-08-26 18:49:15

### Description
This file is an empty initializer for the `PRPB` directory. It ensures that the directory is treated as a package.

## File: patchwork/steps/PRPB/PRPB.py

- **Extension:** .py
- **Size:** 1629 bytes
- **Created:** 2024-08-26 18:49:15
- **Modified:** 2024-08-26 18:49:15

### Description
This file implements the `PRPB` step, a process for creating and managing pull requests. It integrates with the `PR` module and processes the input to map and convert the modified files for further steps in the pull request creation process.

### Usage

1. **Initialization:**
   The `PRPB` class is initialized with inputs as defined in `PRPBInputs`.

2. **Modified Files Mapping:**
   - Converts and maps the input modified files into a format required for creating a pull request.
   - Supports input as a list of dictionaries, a single dictionary, or a string representing the file path.

3. **Run Method:**
   - Instantiates the `PR` class with prepared inputs.
   - Executes the `run()` method from the `PR` class to process and create a pull request.
   - Returns the output from the `PR` class `run()` method, which includes the pull request URL and other details.
  
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