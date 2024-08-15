# Documentation: ReadPRs Step

## Inputs
- **repo_slug**: Required string input indicating the repository slug.
- **pr_ids**: Optional string input for specifying PR IDs.
- **pr_state**: Optional string input for PR state.
- **scm_url**: Annotated string input for SCM URL configurations.
- **gitlab_api_key**: Annotated string input for Gitlab API key configurations.
- **github_api_key**: Annotated string input for Github API key configurations.

## Outputs
- **title**: String output representing PR title.
- **body**: String output representing PR body.
- **comments**: List of strings representing PR comments.
- **diffs**: List of dictionaries representing PR diffs with keys for path and diff text.

This code defines a step called ReadPRs that reads pull requests (PRs) from either Github or Gitlab based on provided configuration inputs. It validates the required inputs, sets up SCM client based on detected API key, fetches PR data based on specified repository slug, PR IDs, and PR state, and then processes the fetched PR data to return structured data points containing PR details like title, body, comments, and diffs.