## GetTypescriptTypeInfo Code Documentation

### Inputs
The `GetTypescriptTypeInfo` class takes the following inputs in its constructor:
- `file_path` (str): The path to the TypeScript file to analyze.
- `variable_name` (str): The name of the variable to get type information for.

### Outputs
The `run()` method of the `GetTypescriptTypeInfo` class returns a dictionary with the following key:
- `type_information` (str): A string containing the type information of the specified variable.

### Usage
The `GetTypescriptTypeInfo` step is used to analyze TypeScript files and extract type information for specified variables. It utilizes the `tsx` command to run a TypeScript script (`get_type_info.ts`) that performs the actual type analysis.

1. The step first constructs the full file path and the path to the `get_type_info.ts` script.
2. It then runs the `tsx` command with the `get_type_info.ts` script, passing the file path and variable name as arguments.
3. The script writes the type information to a temporary file (`temp_output_declaration.txt`).
4. The step reads this temporary file to get the type information.
5. Finally, it cleans up by removing the temporary file and returns the type information.

This step is useful for static analysis of TypeScript code, allowing you to programmatically extract detailed type information for variables in your TypeScript projects.
