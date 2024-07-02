## File: patchwork/steps/CreateIssue/CreateIssue.py

### Inputs
- The class `CreateIssue` requires a dictionary `inputs` with keys `issue_title`, `issue_text`, and `scm_url`.
- Optional input keys are `github_api_key` and `gitlab_api_key` based on which the appropriate SCM client is initialized.

### Outputs
- The `run` method in the `CreateIssue` class returns a dictionary with the key `issue_url` containing the URL of the created issue.

### Description
- This file contains a Python class `CreateIssue` that inherits from `Step`.
- It initializes with required input values and uses the input SCM URL to create an issue using the appropriate SCM client.
- The run method finds the remote URL of the Git repository, creates an issue comment, and returns the URL of the created issue.

## File: patchwork/steps/CreateIssue/typed.py

### Description
- This file defines typed annotations for the `CreateIssue` step inputs and outputs.
- It defines required input types for `issue_text`, `issue_title`, and `scm_url`.
- It indicates additional optional input keys for `github_api_key` and `gitlab_api_key`.
- The output type is defined as a dictionary with the key `issue_url` of type string.

### Code
```python
from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class __CreateIssueRequiredInputs(TypedDict):
    issue_text: Annotated[str, IS_CONFIG]
    issue_title: Annotated[str, IS_CONFIG]
    scm_url: Annotated[str, IS_CONFIG]


class CreateIssueInputs(__CreateIssueRequiredInputs, total=False):
    gitlab_api_key: Annotated[str, IS_CONFIG]
    github_api_key: Annotated[str, IS_CONFIG]


class CreateIssueOutputs(TypedDict):
    issue_url: str

```

## File: patchwork/steps/CreateIssue/__init__.py

### Description
- This file is empty and seems to be a placeholder init file.