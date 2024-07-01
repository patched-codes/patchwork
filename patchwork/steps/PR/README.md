## Code Documentation: Steps for Pull Request Creation

### Inputs
- **File Name:** patchwork/steps/PR/typed.py
  -  Defines the typed input parameters for the Pull Request creation process, including required and optional fields.

### Outputs
- **File Name:** patchwork/steps/PR/PR.py
  - Defines a class `PR` that handles the logic for creating a Pull Request (PR) by utilizing other steps (`CommitChanges`, `CreatePR`, `PreparePR`). 
  - Validates required input parameters using the defined `PRInputs`.
  - Executes substeps and retrieves their outputs to finally return a dictionary containing relevant PR details like branches, URL, number, title, and body.