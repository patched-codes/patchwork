## Table of Contents
- [patchwork/steps/PRPB/typed.py](#patchworkstepsPRPBtyped.py) 
- [patchwork/steps/PRPB/__init__.py](#patchworkstepsPRPB__init__.py) 
- [patchwork/steps/PRPB/PRPB.py](#patchworkstepsPRPBPRPB.py)

### patchwork/steps/PRPB/typed.py
- This file defines data classes for inputs and outputs related to the PRPB (Pull Request Patchwork Builder) step.
- It contains typed annotations for input and output fields for a PRPB step, including fields related to CommitChangesInputs, PreparePRInputs, and CreatePRInputs.
- The `PRPBInputs` class includes various configuration options such as branch-related settings, PR creation options, and API keys.
- The `PRPBOutputs` class includes the expected output fields after running the PRPB step, including base branch, target branch, PR body, and PR URL.

### patchwork/steps/PRPB/__init__.py
- This file is empty and does not contain any code.

### patchwork/steps/PRPB/PRPB.py
- This file contains the implementation of the `PRPB` class, which is a step for creating or modifying Pull Requests.
- The `PRPB` class extends the `Step` class and has input and output classes defined as `PRPBInputs` and `PRPBOutputs`.
- In the constructor `__init__()`, the input keys are mapped and modified files are processed based on the input configuration.
- The `run()` method initiates the PR creation process by instantiating the `PR` class with the modified files and returning the PR outputs after execution.