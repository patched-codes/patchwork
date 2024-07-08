## File: patchwork/steps/PR/PR.py

### Inputs
- `inputs`: Dictionary containing various parameters required for the PR process.

### Outputs
- `run`: Executes the PR process which involves calling other steps to commit changes, prepare PR, and create PR. Returns a dictionary containing details like base branch, target branch, PR URL, PR number, PR title, and PR body.

### Description
This Python script defines a class `PR` that represents the Pull Request (PR) step in a software release process. It ensures that all required input keys are provided, runs the commit changes, prepare PR, and create PR steps, and finally returns relevant details about the PR process.

---

## File: patchwork/steps/PR/typed.py

### Description
This Python script defines the data types for inputs and outputs related to the Pull Request (PR) step. It includes definitions for required inputs like modified code files and optional inputs for different stages of the PR process. The outputs are defined as TypedDict specifying the expected keys and their associated data types.

---

## File: patchwork/steps/PR/__init__.py

### Description
This file is empty and acts as an initialization module for the PR step in the software release process. There is no specific code in this file.