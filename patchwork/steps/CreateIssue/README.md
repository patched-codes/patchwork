## CreateIssue Step Module

### Inputs
- The "CreateIssue" class in the "CreateIssue.py" file requires a dictionary input with keys:
  - "issue_title": Title of the issue to be created.
  - "issue_text": Text content of the issue to be created.
  - "scm_url": URL of the source control management system.
  - "github_api_key" or "gitlab_api_key": Depending on the source control platform selected.

### Outputs
- The "CreateIssue" class in the "CreateIssue.py" file contains a method named "run" that runs the step and returns a dictionary with a key "issue_url" containing the URL of the created issue.

### Usage
- The module is designed to create an issue on the source control platform specified in the input data with the provided issue title and text.
- The source control platform's API key needs to be provided based on whether it's GitHub or GitLab.
- The step utilizes the input data to create an issue and returns the URL of the created issue.