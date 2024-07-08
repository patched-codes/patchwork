## patchwork/steps/CreateIssue/CreateIssue.py

### Inputs
- `inputs`: A dictionary containing keys `"issue_title"`, `"issue_text"`, and `"scm_url"`. Optionally, it may contain either `"github_api_key"` or `"gitlab_api_key"`.

### Outputs
- `run()`: Method that creates an issue comment in a source control management platform repository and returns the URL of the newly created issue.

### Code Summary
The `CreateIssue` class is a step in the Patchwork system that creates an issue in a repository hosted on either GitHub or GitLab. It requires specific input keys, validates the input, sets up the appropriate client for the SCM platform, and then creates an issue comment using the input data. The `run()` method encapsulates the process of creating the issue and returns the URL of the newly created issue.

---

## patchwork/steps/CreateIssue/typed.py

### Code Summary
This file contains type definitions for the required inputs and outputs of the `CreateIssue` step. It specifies the structure of the input data required for the step to function correctly and the output structure that will be returned after the `run()` method is executed. This helps in defining and enforcing the data structure used throughout the `CreateIssue` step.

---

## patchwork/steps/CreateIssue/__init__.py

### Code Summary
This file is empty and does not contain any code.