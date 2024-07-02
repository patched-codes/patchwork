# Documentation for Patchwork Create Issue Module

## Inputs

### File: patchwork/steps/CreateIssue/typed.py
- **CreateIssueInputs**:
  - `issue_text`: list of strings
  - `issue_title`: string
  - `scm_url`: string
  - `gitlab_api_key`: optional string
  - `github_api_key`: optional string

## Outputs

### File: patchwork/steps/CreateIssue/typed.py
- **CreateIssueOutputs**:
  - `issue_url`: string

### File: patchwork/steps/CreateIssue/CreateIssue.py
- Defines a class "CreateIssue" that extends a generic "Step" class.
- Constructor validates and initializes required inputs for creating an issue.
- The "run" method fetches the remote URL of a Git repository, extracts the slug, and then uses a specific SCM client to create an issue with the provided title and text.
- Returns the URL of the newly created issue as a dictionary with key "issue_url".

This code seems to be a part of a larger system that automates creating issues in repositories hosted on platforms like GitHub and GitLab by providing required inputs and generating the corresponding outputs.