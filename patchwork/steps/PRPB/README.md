## File: `patchwork/steps/PRPB/typed.py`

### Inputs
- Defines classes for input and output types related to Pull Request Build and Publish (PRPB) steps.
- Includes various configuration options for PR creation, branch handling, and SCM URLs.

### Outputs
- Defines the expected output structure for the PRPB steps containing information about branches created, PR body, and PR URL.

## File: `patchwork/steps/PRPB/__init__.py`

- Empty file; no code present.

## File: `patchwork/steps/PRPB/PRPB.py`

### Code
- Implements the `PRPB` class which is a step for Pull Request Build and Publish.
- Inherits from `Step` and specifies the input and output class as `PRPBInputs` and `PRPBOutputs` from the typed module.
- Initializes the step by mapping input keys to the required format for further processing.
- Converts input modified files to a standardized format and runs a PR step using the modified files.
- Returns the output of the PR step.