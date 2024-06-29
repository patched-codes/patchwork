# Documentation for Patchwork CreateIssue Module

## Inputs
- The `CreateIssue` class requires a dictionary input with keys:
  - `issue_title`: A string representing the title of the issue.
  - `issue_text`: A list of strings representing the text content of the issue.
  - `scm_url`: A string representing the URL for the source code management system.
  - `github_api_key` (optional): A string representing the API key for GitHub authentication.
  - `gitlab_api_key` (optional): A string representing the API key for GitLab authentication.

## Outputs
- The `run` method in the `CreateIssue` class returns a dictionary with a single key:
  - `issue_url`: A string representing the URL of the created issue.

## Overview
The `CreateIssue` class defines a step in a workflow that creates an issue in a source code management system (GitHub or GitLab) based on the provided inputs. It initializes the required components based on the provided input data, such as API keys and issue details, and then executes a `run` method to create the issue in the specified repository. The class also validates the presence of essential keys in the input dictionary.

## File Details
- `CreateIssue.py`:
  - This file contains the implementation of the `CreateIssue` class which creates an issue in a source code management system.
- `typed.py`:
  - This file defines the typed dictionary structures for inputs and outputs required by the `CreateIssue` class.
- `__init__.py`:
  - An empty file indicating the module directory for the `CreateIssue` step.