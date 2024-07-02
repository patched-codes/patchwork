# CreateIssue Step Implementation

## Inputs
The `CreateIssue` class takes a dictionary `inputs` containing the following required keys:
- `issue_title`: A string representing the title of the issue to create.
- `issue_text`: A string representing the text content of the issue.
- `scm_url`: A string representing the URL for the Source Control Management platform.

Optionally, it can also take the following keys:
- `gitlab_api_key`: A string representing the GitLab API key.
- `github_api_key`: A string representing the GitHub API key.

## Outputs
The `run` method of the `CreateIssue` class returns a dictionary with a single key:
- `issue_url`: A string representing the URL of the created issue on the SCM platform.

The `typed.py` file defines the required inputs and outputs for the `CreateIssue` step using `TypedDict` and `Annotated` from the `typing_extensions` module.