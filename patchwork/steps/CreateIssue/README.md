## Code Documentation

### Inputs
- The code defines a class `CreateIssue` with the following required input keys in the constructor:
  - `issue_title` (str): Title of the issue to be created.
  - `issue_text` (list[str]): Text/content of the issue to be created.
  - `scm_url` (str): URL of the source code management platform.
  - `github_api_key` (str, optional): API key for GitHub if the SCM platform is GitHub.
  - `gitlab_api_key` (str, optional): API key for GitLab if the SCM platform is GitLab.

### Outputs
- The `CreateIssue` class has a `run` method that returns a dictionary with the following output key:
  - `issue_url` (str): URL of the created issue on the specified SCM platform.

### Usage
1. This code can be used to automate the process of creating an issue on GitHub or GitLab from Python scripts.
2. The `CreateIssueInputs` and `CreateIssueOutputs` classes in `typed.py` provide type hints for the inputs and outputs respectively.
3. Users need to provide necessary input data (as mentioned above) to create an instance of the `CreateIssue` class and then call its `run` method to create the issue.