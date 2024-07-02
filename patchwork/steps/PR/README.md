## Code Documentation

### Inputs
- The code defines a class `PR` that takes inputs related to pull request creation:
  - `modified_code_files`: List of `ModifiedCodeFile` objects
  - `disable_branch`
  - `force_branch_creation`
  - `branch_prefix`
  - `branch_suffix`
  - `pr_header`
  - `pr_title`
  - `force_pr_creation`
  - `disable_pr`
  - `scm_url`
  - `gitlab_api_key`
  - `github_api_key`

### Outputs
- The `PR` class in the code runs multiple sub-steps related to pull request creation and returns a dictionary containing the following outputs:
  - `base_branch`: Base branch used for the pull request
  - `target_branch`: Target branch for the pull request
  - `pr_url`: URL of the created pull request
  - `pr_number`: Number of the created pull request
  - `pr_title`: Title of the pull request
  - `pr_body`: Body/content of the pull request

### Usage
- The `PR` class initializes with required inputs and then runs three sub-steps: `CommitChanges`, `PreparePR`, and `CreatePR`.
- The outputs from these sub-steps are aggregated and returned as a dictionary from the `run` method of the `PR` class.
- This code snippet can be utilized as part of a larger system or workflow to automate the process of creating pull requests based on modified code files.