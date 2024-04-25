# ReadPRDiffs Class Overview

## Introduction

The ReadPRDiffs class is defined in `/Users/user/Documents/GitHub/patchwork/patchwork/steps/ReadPRDiffs/ReadPRDiffs.py` file. It is a step in the patchwork pipeline and is supposed to read the differences in a pull request (PR).

## Initialization

### Input

Init method of the class expects a dictionary as input that should contain the following keys:

- "pr_url" : URL of the pull request which diffs are to be read.
- "github_api_key" or "gitlab_api_key": API key of GitHub or GitLab respectively for SCM client authorization.

Optional key:

- "scm_url": The SCM URL to be set.

### Process

During the initialization, the SCM client is set up based on whether Github or Gitlab API key is provided. The pull request PR information is fetched from the SCM.

## Run Method

### Output 

The run method returns a dictionary with the following keys:

- "prompt_value_file" : Temporary file path where the pull request diffs not containing ignored file extensions have been stored in a JSON format.
- "prompt_values" : List of dictionaries where each dictionary has two keys, 'path' which is a path of the file in PR, and 'diff' which represents the diff of that file. Only files not containing ignored file extensions are considered.

### Process

The `run` method reads the file diffs in the pull request. Files with certain extensions (like .png, .jpg, .docx, and so on, mentioned in `_IGNORED_EXTENSIONS`) are ignored while reading the differences. These differences are then written to a temporary .json file. The path to this file, as well as the list of file diffs, are returned by the `run` method.