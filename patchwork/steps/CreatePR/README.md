# Create Pull Request Module

## Inputs
- `inputs: dict`: Required data for creating a pull request including:
  - `target_branch`: Target branch for the pull request
  - `github_api_key` or `gitlab_api_key`: API key for the corresponding platform
  - `scm_url`: URL for the source control management platform
  - `disable_pr`: Flag to disable pull request creation
  - `pr_body`: Body content for the pull request
  - `pr_title`: Title for the pull request
  - `force_pr_creation`: Flag to force creation of the pull request
  - `base_branch`: Base branch for the pull request
  - `issue_url`: GitHub Issue URL to link the PR to (optional). When provided, adds "Resolves #<ISSUE_NUMBER>" to PR description

## Outputs
- `run() -> dict`: Method to run the pull request creation process with the following output:
  - `pr_url`: URL of the created pull request

This module provides functionality to create a pull request on a source control management platform (Github or Gitlab) based on the input data provided. It includes methods for checking required data, handling platform-specific API keys, setting up the pull request parameters, and executing the pull request creation process. The `create_pr` method within the module helps in finding or creating a pull request with necessary details and descriptions, including the ability to link PRs to GitHub issues. The module also logs information throughout the process for tracking and verification purposes. This module is used by both PR and PRPB (Pull Request Patch Builder) steps, where PRPB is an alias for PR defined in `patchwork/steps/__init__.py`.
