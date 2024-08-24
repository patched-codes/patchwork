## Table of Contents
- [patchwork/steps/PRPB/typed.py](#patchworkstepsPRPBtyped.py)
- [patchwork/steps/PRPB/__init__.py](#patchworkstepsPRPB__init__.py)
- [patchwork/steps/PRPB/PRPB.py](#patchworkstepsPRPBPRPB.py)

## patchwork/steps/PRPB/typed.py

### Inputs
- `modified_files`: List of dictionaries
- `path_key`: String
- `comment_title_key`: String
- `comment_message_key`: String
- Custom input fields for CommitChangesInputs, PreparePRInputs, CreatePRInputs

### Outputs
- `base_branch`: String
- `target_branch`: String
- `pr_body`: String
- `pr_url`: String

## patchwork/steps/PRPB/__init__.py

Empty file.

## patchwork/steps/PRPB/PRPB.py

### Inputs
- Inherits inputs from `PRPBInputs`

### Outputs
- Inherits outputs from `PRPBOutputs`

### Code
- Initializes a PRPB class that extends Step, with specified input and output classes.
- Maps input keys to expected keys for handling modified files data.
- Processes modified files data to ensure consistency.
- Initializes a PR class instance with modified files data as input and runs it.
- Returns the outputs of the PR instance.