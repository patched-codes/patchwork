## AnalyzeImpact Code Documentation

### Inputs
The `AnalyzeImpact` module includes a function `find_dependency_usage()` which takes the following inputs:
- `directory` (str): The root directory of the project.
- `dependency` (str): The name of the dependency to search for.
- `language` (str): The programming language (e.g., 'python', 'java', 'javascript', 'typescript', 'go').
- `methods` (list of str): A list of method names to search for in the usage context of the specified dependency.

### Outputs
The function `find_dependency_usage()` returns a dictionary mapping file paths to lists of method names from the specified list that are called in the file.

### Usage
The code analyzes the impact of a specified dependency on a project by searching for its usage in relevant files based on the programming language. It identifies if any of the specified methods associated with the dependency are called within those files. The `AnalyzeImpact` class processes extracted responses related to impacted methods, and then utilizes `find_dependency_usage()` to generate a list of impacted files and their relevant method info. The information is saved to a JSON file for further analysis and processing.