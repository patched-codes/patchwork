# CreateIssue Step in Patchwork

## Inputs
- The `CreateIssue` step accepts a dictionary of inputs containing the following keys: `issue_title`, `issue_text`, `scm_url`, `github_api_key`, and `gitlab_api_key`.
- At least `issue_title`, `issue_text`, and `scm_url` are required inputs.

## Outputs
- The `run` method of the `CreateIssue` step returns a dictionary with the key `issue_url`, containing the URL of the created issue.

## Description
The `CreateIssue` step is part of the Patchwork application and is used to create an issue on a version control system platform like GitHub or GitLab. It initializes the required data, including connection through an API key, and creates an issue using the provided input data. This step is structured with error handling for missing input data and utilizes classes and functions from different modules within the Patchwork application for SCM interaction and logging.