## Documentation: ReadIssues Step

### Inputs
- **Required Keys:** `issue_url`
- **Optional Keys:** `github_api_key`, `gitlab_api_key`, `scm_url`
- **Parameters:**
  - `inputs`: A dictionary containing required and optional keys for configuring the step.

### Outputs
- **Returns:**
  - A dictionary with the issue text extracted from the provided issue URL.

### Description
The `ReadIssues` step is a class that extends `Step` and is responsible for reading and extracting issue text from a specified issue URL on GitHub or Gitlab. It uses a SCM client based on the provided API key to access the issue information. The step filters out certain file extensions from the issues such as images and documents. The primary functionality includes initialization, checking input data, retrieving issue text, and providing the extracted issue text as output.