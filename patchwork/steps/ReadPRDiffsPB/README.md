## Code Summary
This code defines a `ReadPRDiffs` class that inherits from a `Step` class. The `ReadPRDiffs` class is initialized with a dictionary of inputs and checks for required keys. It then uses input data like API keys and URLs to communicate with either a GitHub or GitLab client to fetch pull request information. The `run` method retrieves file differences in the pull request, saves them to a temporary JSON file, and returns a dictionary containing the file path and diff details.

### Inputs
- Input dictionary containing keys:
  - "pr_url": URL of the pull request
  - "github_api_key" or "gitlab_api_key": API key for GitHub or GitLab
  - "scm_url": URL of the source code management system

### Outputs
- Returns a dictionary with the following keys:
  - "prompt_value_file": path to the temporary JSON file
  - "prompt_values": list of dictionaries containing file path and diff details