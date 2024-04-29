## Patchwork ReadIssues Module

### Inputs
- The `ReadIssues` class in `ReadIssues.py` expects a dictionary `inputs` containing the following keys:
  - `issue_url`: URL of the issue
  - `github_api_key`: API key for GitHub (optional, can be provided if working with GitHub issues)
  - `gitlab_api_key`: API key for GitLab (optional, can be provided if working with GitLab issues)
  - `scm_url`: URL of the source code management platform

### Outputs
- The `ReadIssues` class provides a `run` method that returns a dictionary containing the issue text associated with the provided `issue_url`.

### Usage
- The `ReadIssues` class reads issues from a source code management platform (GitHub or GitLab) using the provided API keys and URL.
- It ensures the required input keys are present, selects the appropriate SCM client based on the provided API key, sets the SCM URL, and retrieves the issue text based on the provided issue URL.
- Users can initiate the `RunIssues` class by providing the necessary inputs and then executing the `run` method to obtain the issue text data.
