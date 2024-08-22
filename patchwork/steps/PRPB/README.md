## PRPB Step in Patchwork

### Inputs
- `PRPBInputsRequired` class defines the required inputs for the PRPB step.
- `PRPBInputs` class extends `PRPBInputsRequired` and includes additional optional inputs for various configurations.
- `PRPBOutputs` class defines the expected output structure of the PRPB step.

### Usage
- The code includes type definitions for the required and optional inputs for the PRPB step in the `typed.py` file.
- The `PRPB` class in `PRPB.py` is a custom step that processes the input data and runs the PR step with modified code files.
- The `PRPB` class initializer maps input keys and processes modified files for PR.
- The `run` method initiates a PR step with the processed inputs and modified code files.

### File Details
- `typed.py`: Defines input and output data structures for the PRPB step.
- `PRPB.py`: Contains the `PRPB` class that processes inputs and triggers the PR step.
- `__init__.py`: An empty file indicating the initialization of the PRPB folder.