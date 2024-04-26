# Documentation: CreateIssueComment Step

## Inputs

1. `inputs`: A dictionary containing the following keys:
    - `issue_url`: The URL of the issue to add a comment to.
    - `issue_text`: The text content of the comment to be added.
    - `github_api_key` or `gitlab_api_key`: The API key for the corresponding SCM platform.
    - `scm_url` (optional): The URL of the SCM platform.

## Outputs

- `run()`: A method that runs the step to create a comment on the specified issue. It returns a dictionary with the URL of the created comment.