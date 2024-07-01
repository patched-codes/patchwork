
# PR Step

This section includes code for a PR (Pull Request) step that facilitates creating and managing pull requests. The step requires specific input data and produces output related to pull request creation.

## Inputs:
- `modified_code_files`: A list of ModifiedCodeFile objects representing the changed files.
- `disable_branch`: Boolean flag to disable branch creation.
- `force_branch_creation`: Boolean flag to force branch creation.
- `branch_prefix`: Prefix for branch names.
- `branch_suffix`: Suffix for branch names.
- `pr_header`: Header for the pull request.
- `pr_title`: Title for the pull request.
- `force_pr_creation`: Boolean flag to force pull request creation.
- `disable_pr`: Boolean flag to disable pull request creation.
- `scm_url`: URL for version control system.
- `gitlab_api_key`: API key for Gitlab.
- `github_api_key`: API key for GitHub.

## Outputs:
- `base_branch`: Base branch for the changes.
- `target_branch`: Target branch for the changes.
- `pr_url`: URL of the created pull request.
- `pr_number`: Number of the created pull request.
- `pr_title`: Title of the created pull request.
- `pr_body`: Body of the created pull request.

The `PR` class within `PR.py` file extends the `Step` class and defines required input keys. It checks for missing keys and runs several sub-steps (`CommitChanges`, `PreparePR`, `CreatePR`) to gather necessary information and create a pull request. The final output includes details for the newly created pull request.