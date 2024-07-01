## Contents of CreateIssue Module

### Inputs
- The `CreateIssue` class requires a dictionary of inputs with keys `'issue_title'`, `'issue_text'`, and `'scm_url'`. Additionally, it can also accept `'github_api_key'` or `'gitlab_api_key'` based on the SCM platform. 

### Outputs
- The `run` method of the `CreateIssue` class returns a dictionary with the key `'issue_url'` that contains the URL of the created issue.

### Usage
- The `CreateIssue` class is used to create an issue on either GitHub or Gitlab based on the provided input data. The necessary data is passed via a dictionary to the class, and then the `run` method is invoked to create the issue and return the URL.