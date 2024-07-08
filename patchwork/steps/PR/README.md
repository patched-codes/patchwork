## File: patchwork/steps/PR/PR.py
### Inputs
- The `PR` class requires certain inputs based on the `PRInputs` class.
### Outputs
- The `run` method of the `PR` class returns a dictionary containing information related to commit changes, preparing PR, and creating PR. The dictionary excludes any `None` values.

## File: patchwork/steps/PR/typed.py
### Inputs
- Defines the required input types for the `PR` class, including configurations related to commit changes, preparing PR, and creating PR.
### Outputs
- Defines the expected output types for the `PR` class, including details about the base branch, target branch, PR body, and PR URL.

## File: patchwork/steps/PR/__init__.py
### Inputs
- No specific inputs.
### Outputs
- No specific outputs.