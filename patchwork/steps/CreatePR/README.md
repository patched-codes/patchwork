# CreatePR Class Documentation

This python class CreatePR facilitates the creation of a Pull Request (PR) in a given repository on GitHub or GitLab.

##  Inputs:

The initialization of the CreatePR class (`__init__`) requires a dictionary input, `inputs`, that must contain certain keys:

- `"target_branch"`: The target branch for the PR. [REQUIRED]
- `"disable_pr"`: A flag to disable the PR creation. If not provided, the default is FALSE.
- `"pr_body"`: The body for the PR. If not provided, an empty string will be used.
- `"pr_title"`: The title for the PR. If not provided, the default is "Patchwork PR".
- `"force_pr_creation"`: A flag to force the creation of the PR. If not provided, the default is FALSE.
- `"base_branch"`: The base branch for the PR. If not provided and PR creation is enabled, the PR creation will be skipped.
- `"github_api_key"`: API key for GitHub. Required if GitLab is not used.
- `"gitlab_api_key"`: API key for GitLab. Required if GitHub is not used.
- `"scm_url"`: URL of the Source Control Management platform. It's optional and can be set after initialisation using `set_url()`.

An error will be thrown if the `"target_branch"` is missing or neither `"github_api_key"` nor `"gitlab_api_key"` are provided.

## Outputs:

The `run` method outputs a dictionary with the following keys:

- `"pr_url"`: The URL of the created PR. This key is not present if the PR creation has been skipped or failed.

## Usage:

Below is a simple usage example:

```python
inputs = {"target_branch": "feature", "github_api_key": "ABC123", "base_branch": "main"}
obj = CreatePR(inputs)
result = obj.run()
```