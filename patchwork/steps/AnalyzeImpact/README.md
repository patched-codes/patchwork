# AnalyzeImpact Code Documentation

This Python source code is part of `patchwork` project for analyzing the impact of specific library method usage in a project.

## Class Definition: AnalyzeImpact

This class extends Step class and plays a critical role in identifying method impacts within a specific library.

### __init__(self, inputs: dict) Method

The purpose of this method is to initialize the AnalyzeImpact object. 

#### Inputs

The method takes a dictionary with the following keys:

- extracted_responses: A list of extracted responses.
- library_name: The name of the library to analyze.
- platform_type: The type of platform.

#### Outputs

No explicit output but the method creates an instance of the AnalyzeImpact class.

### run(self) -> dict Method

This method identifies the methods in the given library that are used in the provided code.

#### Inputs

No extra input is expected aside from the initialized object instance.

#### Outputs

The run method returns a dictionary with the following keys:

- prompt_value_file: A temporary json file that includes the details of code section for the impacted methods.
- code_file: This also returns the same temporary json file.


## Function: find_dependency_usage(directory, dependency, language, methods)

This is a helper function defined outside the class definition.

#### Inputs

The function takes the following parameters:

- directory (str): The root directory of the project.
- dependency (str): The name of the dependency to search for.
- language (str): The programming language.
- methods (list of str): A list of method names to search for in the usage context of the specified dependency.

#### Outputs

It returns a dictionary that maps file paths to lists of method names from the specified list that are called in the file.
