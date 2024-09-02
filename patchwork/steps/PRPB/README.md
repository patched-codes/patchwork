# Module: patchwork/steps/PRPB

## File: patchwork/steps/PRPB/typed.py

### Description
The `typed.py` file contains type definitions for the inputs and outputs of the PRPB (Pull Request Preparation and Branching) step. These type definitions help in validating and enforcing the correct structure of input and output data used by the PRPB step.

### Input Types
- **PRPBInputs:** Inherits from `__PRPBInputsRequired` and contains configuration parameters such as commit message keys, branch configuration settings, PR settings, and SCM (Source Control Management) credentials.

#### Required Inputs
```python
class __PRPBInputsRequired(TypedDict):
    modified_files: List[Dict]
    path_key: str
```

#### Optional Inputs
```python
class PRPBInputs(__PRPBInputsRequired, total=False):
    comment_title_key: str
    comment_message_key: str
    disable_branch: Annotated[bool, StepTypeConfig(is_config=True)]
    force_branch_creation: Annotated[bool, StepTypeConfig(is_config=True)]
    branch_prefix: Annotated[str, StepTypeConfig(is_config=True)]
    branch_suffix: Annotated[str, StepTypeConfig(is_config=True)]
    pr_header: Annotated[str, StepTypeConfig(is_config=True)]
    pr_title: Annotated[str, StepTypeConfig(is_config=True)]
    force_pr_creation: Annotated[bool, StepTypeConfig(is_config=True)]
    disable_pr: Annotated[bool, StepTypeConfig(is_config=True)]
    scm_url: Annotated[str, StepTypeConfig(is_config=True)]
    gitlab_api_key: Annotated[str, StepTypeConfig(is_config=True)]
    github_api_key: Annotated[str, StepTypeConfig(is_config=True)]
```

### Output Types
- **PRPBOutputs:** Defines the structure of the data output by the PRPB step, which includes branch and PR-related information.

```python
class PRPBOutputs(TypedDict):
    base_branch: str
    target_branch: str
    pr_body: str
    pr_url: str
```

### Usage
This file is used to ensure that the input and output data structures for the PRPB step are well-defined and consistent.

## File: patchwork/steps/PRPB/__init__.py

### Description
The `__init__.py` file is an empty file that indicates that the directory it resides in is a Python package. This file allows the containing folder to be importable as a package module.

## File: patchwork/steps/PRPB/PRPB.py

### Description
The `PRPB.py` file defines the PRPB step that encompasses the creation and preparation of branches and pull requests. This step integrates existing functionalities for creating and managing pull requests.

### Class: PRPB
The `PRPB` class inherits from the `Step` class and uses the `PRPBInputs` and `PRPBOutputs` types defined in `typed.py` for input validation and output structure.

#### Initialization
The `__init__` method takes the input parameters, processes the `modified_files` input to convert it into the required format, and initializes the necessary attributes.

```python
def __init__(self, inputs):
    # Code for initialization and conversion of modified files
```

#### Method: run
The `run` method creates a PR (Pull Request) object using the inputs and returns the outputs of the PR.

```python
def run(self):
    pr = PR({**self.inputs, "modified_code_files": self.modified_files})
    pr_outputs = pr.run()
    return pr_outputs
```

### Usage
This file would be used to create an instance of the `PRPB` class with the necessary input data, then call the `run` method to execute the step and obtain the resulting outputs.