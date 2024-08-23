## Contents of the Code

### Inputs
- **File: patchwork/steps/PRPB/typed.py**
  - Defines input and output types for PRPB step including required and optional fields like modified_files, path_key, comment_title_key, etc.

### Outputs
- **File: patchwork/steps/PRPB/typed.py**
  - Defines output types for PRPB step including fields like base_branch, target_branch, pr_body, pr_url.

### Usage
- The code includes class definitions for input and output types for PRPB step.
- It implements a PRPB class that extends Step and processes input data to create a PR object and return its outputs.