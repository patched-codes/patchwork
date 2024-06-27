# Code Documentation

## File: patchwork/steps/CreateIssue/CreateIssue.py

- This Python module defines a `CreateIssue` class that is a subclass of `Step`.
- The class expects specific input keys (`"issue_title"`, `"issue_text"`, `"scm_url"`) when initialized.
- It checks for the presence of API keys for Github or Gitlab and instantiates the corresponding platform client.
- The `run()` method uses git to get the repo details, creates an issue comment via the SCM client, and returns the issue URL in a dictionary.

## File: patchwork/steps/CreateIssue/typed.py

- This file defines the `CreateIssueInputs` and `CreateIssueOutputs` TypedDicts for type hinting.
- The `CreateIssueInputs` includes typed keys for issue related details and optional Github/Gitlab API keys.
- The `CreateIssueOutputs` specifies the output structure with just the issue URL of type `str`.

## File: patchwork/steps/CreateIssue/__init__.py

- An empty Python file with no significant content.

This code seems to be a part of a larger project involving creating issues on SCM platforms like Github or Gitlab. The `CreateIssue` step is designed to facilitate this process with the specified inputs and outputs. Type hints in `typed.py` offer clarity on the expected data structure for inputs and outputs.