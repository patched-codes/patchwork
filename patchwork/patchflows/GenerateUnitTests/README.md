## Code Documentation

### Inputs
- The code reads default inputs from a YAML file (`defaults.yml`) and a JSON file (`default_prompt.json`).
- The code takes user inputs and updates the default inputs accordingly.
- The code expects inputs like `folder_path`, `prompt_template_file`, `language`, `test_file_extension`, etc.

### Outputs
- The code generates unit tests based on the provided inputs.
- It creates a new test file with the specified extension.
- The code updates various parameters in the inputs dictionary during its execution.
- The final output includes the modified inputs after running the unit test generation process.
