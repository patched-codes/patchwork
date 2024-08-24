## Table of Contents
- [patchwork/steps/PRPB/typed.py](#patchworkstepsPRPBtyped.py)
- [patchwork/steps/PRPB/__init__.py](#patchworkstepsPRPB__init__.py)
- [patchwork/steps/PRPB/PRPB.py](#patchworkstepsPRPBPRPB.py)

### File: patchwork/steps/PRPB/typed.py
- Defines input and output data classes for the `PRPB` step.
- Input class `PRPBInputs` includes configuration options for various step types like CommitChangesInputs, PreparePRInputs, CreatePRInputs.
- Output class `PRPBOutputs` includes fields for CommitChangesOutputs and PreparePROutputs.

### File: patchwork/steps/PRPB/__init__.py
- Empty file.

### File: patchwork/steps/PRPB/PRPB.py
- Imports necessary libraries and classes.
- Defines the `PRPB` class inheriting from `Step` class with specific input and output classes.
- Initializes `PRPB` class with inputs and maps keys as needed.
- The `run` method creates an instance of `PR` (presumably another step), passes modified files and other inputs, and runs it to return the outputs.