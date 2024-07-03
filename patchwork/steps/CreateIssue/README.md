# Patchwork CreateIssue Module

This module consists of three files related to the creation of issues on various source code management platforms.

## File: patchwork/steps/CreateIssue/CreateIssue.py

- Contains a class `CreateIssue` that inherits from `Step` and has functionality to create an issue on a repository.
- Initialization requires specific inputs like issue title, issue text, SCM URL, and API key for either Github or Gitlab.
- The `run` method uses Git operations to identify the repository and then calls the respective source code management client to create an issue.
- Outputs the URL of the created issue.

## File: patchwork/steps/CreateIssue/typed.py

- Defines the required input structure for `CreateIssue` as a typed dictionary `CreateIssueInputs`, including issue text, title, SCM URL, and API keys.
- Defines the output structure for `CreateIssue` as a typed dictionary `CreateIssueOutputs`, containing the URL of the created issue.

## File: patchwork/steps/CreateIssue/__init__.py

- An empty file serving as the package initializer for the CreateIssue module.