# Patchwork CreateIssue Module

## Inputs
- The `CreateIssue` class takes a dictionary `inputs` with the following required keys: `issue_title`, `issue_text`, and `scm_url`. It additionally checks for either `github_api_key` or `gitlab_api_key` in the inputs.
- In the `typed.py` file, the `CreateIssueInputs` class defines the structure of the input dictionary required for `CreateIssue` with type annotations.
  
## Outputs
- Upon running the `CreateIssue` class using the `run` method, it returns a dictionary with the `issue_url` where the issue was created.
- The `typed.py` file specifies the structure of the output dictionary as `issue_url`.

This code snippet shows a module (`CreateIssue`) for creating issues in a source control management system based on the input data provided. The module interacts with SCM platforms using tokens such as `github_api_key` or `gitlab_api_key`, creates an issue with a specific title and text, and returns the URL of the created issue. The module is integrated into a larger application for managing development workflows.