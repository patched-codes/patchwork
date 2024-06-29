## Contents of the Code

The provided code consists of three main files related to a step called "CreateIssue":
1. `CreateIssue.py` defines a class named `CreateIssue` that inherits from `Step`. It requires specific keys (`issue_title`, `issue_text`, `scm_url`) in the input data. It initializes a client based on whether it's for GitHub or GitLab, and then creates an issue using the provided data and the client's relevant method. It also provides a `run` method that returns the URL of the created issue.
   
   - **Inputs:** Dictionary containing `issue_title`, `issue_text`, `scm_url`, and either `github_api_key` or `gitlab_api_key`.
   - **Outputs:** Dictionary with the `issue_url`.

2. `typed.py` contains type hints for the input and output of the `CreateIssue` step in the form of `TypedDict`.
   
3. `__init__.py` is an empty file.