# Documentation for Patchwork CreateIssue Module

## Inputs

- `issue_title`: A required string representing the title of the issue to be created.
- `issue_text`: A required list of strings containing the text of the issue to be created.
- `scm_url`: A required string representing the URL of the source control management platform.
- `github_api_key`: An optional string representing the API key for GitHub authentication.
- `gitlab_api_key`: An optional string representing the API key for GitLab authentication.

## Outputs

- `issue_url`: A string representing the URL of the created issue.

### File: patchwork/steps/CreateIssue/CreateIssue.py
This file contains a class `CreateIssue` that is a step in a workflow. It takes a set of inputs, validates them, and then creates an issue on a source control management platform (GitHub or GitLab) based on the provided input data. The `run` method returns a dictionary with the URL of the created issue.

### File: patchwork/steps/CreateIssue/typed.py
This file defines the types of inputs and outputs expected by the `CreateIssue` step. It uses `TypedDict` to specify the structure of the input and output data. Additionally, it includes `NotRequired` for the optional API keys.

### File: patchwork/steps/CreateIssue/__init__.py
This file is empty and does not contain any code.