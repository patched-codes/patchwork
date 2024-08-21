## patchwork/steps/PRPB/typed.py
### Inputs
- Defines input types for `PRPB` step including CommitChangesInputs, PreparePRInputs, and CreatePRInputs.
### Outputs
- Defines output types for `PRPB` step including CommitChangesOutputs, PreparePROutputs, and CreatePROutputs.

## patchwork/steps/PRPB/PRPB.py
### Inputs
- Inherits `PRPBInputs` class for the step.
### Outputs
- Returns output from `PR` step after running `PRPB` step's defined logic.