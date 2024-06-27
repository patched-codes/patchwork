# Documentation for Create Issue Step

## Inputs
- `issue_text`: the content of the issue to be created, a list of strings.
- `issue_title`: the title of the issue to be created, a string.
- `scm_url`: the URL of the source code management system, a string.
- `gitlab_api_key`: API key for GitLab (optional), a string.
- `github_api_key`: API key for GitHub (optional), a string.

## Outputs
- `issue_url`: URL of the created issue.

### Functionality
This code defines a step named `CreateIssue` that is a part of the Patchwork library. The step is part of a workflow that automates certain tasks in code repositories. It takes input data consisting of issue title, issue text, SCM URL, and optionally GitHub or GitLab API keys. The `run` method creates an issue using the provided data and returns the URL of the created issue.