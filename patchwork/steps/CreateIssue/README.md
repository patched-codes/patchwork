# CreateIssue Step

This code defines a `CreateIssue` class that inherits from a `Step` class. The `CreateIssue` step is responsible for creating an issue/comment on a version control system platform (either Github or Gitlab). It takes inputs such as issue title, issue text, and the repository URL, along with optional API keys for Github or Gitlab. It then uses these inputs to create an issue/comment using the respective platform's API.

## Inputs
- `issue_title`: The title of the issue/comment.
- `issue_text`: The content of the issue/comment.
- `scm_url`: The URL of the repository on the version control system.
- `github_api_key` (optional): API key for Github authentication.
- `gitlab_api_key` (optional): API key for Gitlab authentication.

## Outputs
- `issue_url`: The URL of the created issue/comment.

Additionally, there is a `TypedDict` defined in `typed.py` that specifies the structure of the inputs and outputs accepted and returned by the `CreateIssue` step.