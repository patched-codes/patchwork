# Code Documentation

## Inputs

- **PRInputs**: Typed dictionary class defining the required and optional inputs for the PR step. It includes attributes related to CommitChangesInputs, PreparePRInputs, and CreatePRInputs.

## Outputs

- **PROutputs**: Typed dictionary class defining the expected outputs of the PR step. It includes attributes related to CommitChangesOutputs, PreparePROutputs, and CreatePROutputs.

### File: patchwork/steps/PR/PR.py

- This file contains a Python class `PR` that represents a step in a workflow.
- The class is initialized with required inputs and raises an error if any required input is missing.
- The `run` method executes the CommitChanges, PreparePR, and CreatePR steps, collects their outputs, and returns a refined dictionary.

### File: patchwork/steps/PR/typed.py

- This file defines the typed dictionary classes for inputs and outputs related to the PR step.
- It includes the required inputs, optional inputs, and expected outputs along with the relevant data types.
- The typing annotations and extensions are used to enhance type checking and clarity in the code.

### File: patchwork/steps/PR/__init__.py

- This file is empty and does not contain any code.