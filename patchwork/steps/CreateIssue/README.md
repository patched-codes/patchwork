# Code Documentation for CreateIssue Step

## Inputs
- The `CreateIssue` class accepts a dictionary of inputs containing keys:
  - `issue_title`: Title of the issue to be created.
  - `issue_text`: Description text for the issue.
  - `scm_url`: URL for the source code management system.
  - `github_api_key`: API key for GitHub (optional).
  - `gitlab_api_key`: API key for GitLab (optional).

## Outputs
- The `run` method of the `CreateIssue` class returns a dictionary containing:
  - `issue_url`: URL of the created issue.

The code snippet mainly defines a `CreateIssue` step that creates an issue on a source code management platform like GitHub or GitLab. It initializes the step with required data, validates input keys, and uses provided API keys to interact with the specified platform for creating an issue based on the inputs provided. The `run` method utilizes GitPython library to extract repository information and calls methods from `GithubClient` or `GitlabClient` to create an issue with the specified title and text.