## PRPB Step Implementation

### Inputs
- The `typed.py` file defines the input and output structures for the PRPB step in the Patchwork framework.
- `PRPBInputs` class defines the required and optional inputs for the PRPB step including configuration options.
- Input structure includes data for CommitChanges, PreparePR, and CreatePR steps.
- Inputs include file modifications, comment titles/messages, branch-related configurations, and PR related information.

### Outputs
- `PRPBOutputs` class defines the expected output structure for the PRPB step, encompassing data for CommitChanges, PreparePR, and CreatePR steps.

### Usage
- The `PRPB` class in `PRPB.py` file is a subclass of `Step` and is used for PRPB step implementation in Patchwork.
- The constructor processes input data to prepare modified files for the PR process.
- `run` method initiates the PR step using the processed input information, generates a PR, and returns the PR outputs.

This documentation provides an overview of the input/output structure for the PRPB step and how it is utilized in the Patchwork framework.