# Documentation for PRPB Step

## Overview

The `PRPB` step in this module is designed for managing and preparing pull requests (PRs) with specific annotated configurations and types. It extends the `Step` class and offers a structured way to input and output data related to PR processes, leveraging the `PRPBInputs` and `PRPBOutputs` types.

## File Locations

- **PRPB Step:** `patchwork/steps/PRPB/PRPB.py`
- **Typed Definitions:** `patchwork/steps/PRPB/typed.py`
- **Initialization:** `patchwork/steps/PRPB/__init__.py`

## File: patchwork/steps/PRPB/PRPB.py

### Inputs

The class `PRPB` takes inputs which include:
- **path_key:** A key for the path of modified files.
- **title_key (optional):** Key for the commit message title.
- **message_key (optional):** Key for the patch message.
- **modified_files:** A list, dictionary, or string representing files that have been modified.

### Outputs

The main output from the `run` method is a dictionary that contains the outputs from the `PR` step's `run` method, which would typically include details pertinent to PRs like URLs and branch information.

### Code Summary

```python
class PRPB(Step, input_class=PRPBInputs, output_class=PRPBOutputs):
    def __init__(self, inputs):
        ...
        # initializing modified files based on inputs
        ...

    def run(self):
        pr = PR({ ... , "modified_code_files": self.modified_files})
        pr_outputs = pr.run()
        return pr_outputs
```

### Usage

The `PRPB` class is utilized by initializing it with input parameters, processing modified files as per given keys, and then running the step to handle the PR creation or preparation through the `PR` step.

---

## File: patchwork/steps/PRPB/typed.py

### Inputs

Definitions of input types for the `PRPB` step:
- **modified_files (List[Dict]):** A list of dictionaries representing files.
- **path_key (str):** Key used for file paths.
- **comment_title_key (str, optional):** Key used for the commit message title.
- **comment_message_key (str, optional):** Key used for patch messages.
- **Additional Configurations (Annotated):** Configurations such as `disable_branch`, `force_branch_creation`, and others for detailed customization.

### Outputs

Definitions of output types for the `PRPB` step:
- **base_branch (str):** The base branch name.
- **target_branch (str):** The target branch name.
- **pr_body (str):** The body content of the PR.
- **pr_url (str):** The URL of the created PR.

### Code Summary

```python
class PRPBInputs(__PRPBInputsRequired, total=False):
    # Various annotated configurations
    ...

class PRPBOutputs(TypedDict):
    base_branch: str
    target_branch: str
    pr_body: str
    pr_url: str
```

### Usage

These TypedDict classes provide structured and clear definitions of the inputs and outputs for the `PRPB` step, used for ensuring type safety and clarity in the PR handling processes.

---

## File: patchwork/steps/PRPB/__init__.py

This file initializes the PRPB module in the patchwork steps, which is currently empty, indicating no immediate initialization code is required.

```python

```

---

### Conclusion

The `PRPB` step offers a robust framework for managing pull requests with configurable inputs and structured outputs. It integrates tightly with the `PR` step and leverages typed dictionaries for clarity. This setup can be easily used and extended for various PR automation needs in continuous integration (CI) pipelines.