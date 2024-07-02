# Patchwork CreateIssue Step

## Inputs
- The code defines a class `CreateIssue` which is a step to create an issue on either GitHub or Gitlab.
- The step expects the following inputs:
  - `issue_title` (title of the issue)
  - `issue_text` (content of the issue)
  - `scm_url` (URL of the source control management system)
- Optionally, the inputs can include:
  - `github_api_key` (API key for GitHub)
  - `gitlab_api_key` (API key for Gitlab)

## Outputs
- The `run()` method of the `CreateIssue` class returns a dictionary with the `issue_url` where the issue was created.

The code allows for creating issues on GitHub or Gitlab by providing the required inputs and API keys for authentication and access.