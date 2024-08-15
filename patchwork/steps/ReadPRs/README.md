# Documentation for ReadPRs Module

## Inputs
- **File**: patchwork/steps/ReadPRs/typed.py
  - `repo_slug`: A required string input for the repository slug.
  - `pr_ids`: An optional string input for PR IDs.
  - `pr_state`: An optional string input for the state of PRs.
  - `scm_url`: An annotated string input for the SCM URL, configured for step type.
  - `gitlab_api_key`: An annotated string input for the GitLab API key, configured for step type.
  - `github_api_key`: An annotated string input for the GitHub API key, configured for step type.

## Outputs
- **File**: patchwork/steps/ReadPRs/typed.py
  - `title`: Title of the PR.
  - `body`: Body content of the PR.
  - `comments`: List of comments on the PR.
  - `diffs`: List of dictionaries containing file path and related diff content.

## Usage
1. The `ReadPRs` class in `ReadPRs.py` creates a step for reading PRs from GitLab or GitHub.
2. Construct the step object by passing `DataPoint` inputs for repository slug, PR IDs, PR state, SCM URL, and API keys.
3. Run the step using the `run()` method to fetch PRs based on the provided inputs.
4. The step filters PRs based on ID if specified, and generates data points with PR information like title, body, comments, and diffs.
5. Use the generated data points for further processing or analysis related to the PRs.