## Inputs and Outputs

### Inputs
- `repo_slug`: A string representing the repository slug.
- `pr_ids`: A string representing the pull request IDs.
- `pr_state`: A string representing the state of the pull request.
- `scm_url`: An annotated string representing the source control management URL.
- `gitlab_api_key`: An annotated string representing the Gitlab API key.
- `github_api_key`: An annotated string representing the GitHub API key.

### Outputs
- `title`: A string representing the title of the pull request.
- `body`: A string representing the body of the pull request.
- `comments`: A list of strings representing comments on the pull request.
- `diffs`: A list of dictionaries containing path and diff information for each file in the pull request.