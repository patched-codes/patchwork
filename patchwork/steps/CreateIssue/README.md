# Documentation for CreateIssue Step

This code includes a `CreateIssue` class that is used as a part of a larger system. The purpose of this class is to create an issue on source control platforms like GitHub or GitLab. It requires specific information like issue title, issue text, and source control management (SCM) URL to function properly.

## Inputs
The `CreateIssue` class takes a dictionary as inputs with the following keys:
- `issue_title` (str): Title of the issue to be created.
- `issue_text` (list of str): Body text of the issue.
- `scm_url` (str): URL of the source control management system.
- `github_api_key` (optional str): API key for GitHub authentication.
- `gitlab_api_key` (optional str): API key for GitLab authentication.

## Outputs
The `run` method of the `CreateIssue` class returns a dictionary with the following key:
- `issue_url` (str): URL of the created issue.

---
**Files:**
- [patchwork/steps/CreateIssue/CreateIssue.py](#patchworkstepsCreateIssueCreateIssue.py)
- [patchwork/steps/CreateIssue/typed.py](#patchworkstepsCreateIssuetyped.py)
- [patchwork/steps/CreateIssue/__init__.py](#patchworkstepsCreateIssue__init__.py)