# Documentation for CreateIssue Step

## Inputs

### CreateIssue.py
- **Inputs**: A dictionary containing the following keys: "issue_title" (str), "issue_text" (str), "scm_url" (str), "github_api_key" (str) or "gitlab_api_key" (str).
- **Exceptions**: Raises a ValueError if any of the required keys are missing from the input dictionary.

### typed.py
- **Inputs**: 
    - Annotated dictionary with required keys: "issue_text" (str), "issue_title" (str), "scm_url" (str).
    - Optional keys: "gitlab_api_key" (str), "github_api_key" (str).

## Outputs

### CreateIssue.py
- **Returns**: A dictionary containing the URL of the created issue.

### typed.py
- **Outputs**: 
    - A dictionary with a single key: "issue_url" (str).

This documentation describes a class `CreateIssue` that is a step in a patchwork process. The class requires specific input data including issue details and a source control management (SCM) URL. The class can interact with GitHub or Gitlab based on the provided API key. Upon execution, the step creates an issue in the SCM platform and returns the URL of the created issue. The input and output data structures are defined in the `typed.py` file using TypedDict and annotations.