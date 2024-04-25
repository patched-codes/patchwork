# PreparePR Class

The `PreparePR` class is a part of the patchwork.step module. It is used to prepare a Pull Request (PR) by taking in modified code files and formatting them appropriately for a PR.

## __init__ Method

The `__init__` method is a constructor that initializes the `PreparePR` object. It requires a dictionary as its input.

### Inputs

The input dictionary must include the following key:

- "modified_code_files": A list of modified code files. If the list is less than 1, the method will log a warning message.

Optionally, the input dictionary can also include the following key:

- "pr_header": A header for the pull request. By default, the header is determined by the number of issues fixed in 'modified_code_files'.

### Outputs

The `__init__` method does not directly return any output. However, it updates the object's instance variables including 'self.modified_code_files' and 'self.header' which can be accessed later.

## run Method

The `run` method is used to generate a pull request by grouping the modified code files by their paths and creating a formatted comment for each file. The method's functionality includes generating links for each file and its respective patches along with their commit messages and patch messages.

### Inputs

This method does not take any explicit inputs.

### Outputs

The `run` method returns a dictionary with the following key:

- "pr_body": A string consisting of the PR header, a divider, and a formatted comment for every modified file. The comment includes links to files and patches along with their commit messages and patch messages. If a commit message or patch message is missing for a given patch, then the comment's format will adapt accordingly.
