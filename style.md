# Code Style Guidelines

## 1. Naming Conventions
- Use snake_case for Python functions and variables
- Use PascalCase for classes
- Use camelCase for JavaScript/Java variables and functions

## 2. Code Structure
- Organize imports at the beginning of the file, sorted alphabetically
- Use separate files for different aspects of a component (e.g., typed.py for type definitions)
- Use modular structure and implement pagination where appropriate
- Use TypedDict for defining input and output structures

## 3. Documentation
- Include a detailed README.md file for each component or module
- Use docstrings for function and class documentation
- Include @param and @return tags in function documentation
- Provide detailed descriptions for parameters and return values
- Use consistent formatting for docstrings across different languages
- Use markdown for README files

## 4. Error Handling
- Implement proper error handling and logging
- Use specific error messages for missing input data
- Handle exceptions appropriately when importing modules
- Implement exception handling for potential timeout errors in API requests

## 5. Performance
- Use list comprehensions for simple transformations
- Prefer 'get' method for dictionaries
- Add timeouts to API requests to prevent long-running operations

## 6. Security
- Avoid using dynamic values in importlib.import_module() to prevent code injection vulnerabilities
- Use whitelists to validate module names before importing

## 7. Code Quality
- Use type hints for function parameters and return values
- Use f-strings for string formatting
- Follow PEP 8 style guide for Python code
- Use Black for code formatting
- Use isort for import sorting
- Perform static type checking

## 8. Dependency Management
- Use specific version ranges for dependencies (e.g., '~2.32.0', '^1.5.0')
- Keep dependencies up-to-date for security and compatibility
- Be cautious with dependency updates that may introduce breaking changes

## 9. Version Control
- Follow versioning conventions
- Include a newline at the end of each file

## 10. Testing
- Thoroughly test code changes

## 11. Null Safety
- Use default values for potentially null fields (e.g., 'title = issue.title or "[No Title]"')

## 12. CI/CD
- Use 'poetry version' command to set version dynamically in CI/CD pipeline
- Use workflow_dispatch with input for version in GitHub Actions
- Update version number in pyproject.toml for new releases# Code Style Guidelines

## 1. Naming Conventions
- Use snake_case for function names in Python
- Use camelCase for function names in JavaScript and method names in Java
- Use clear and descriptive naming conventions

## 2. Code Structure
- Follow a modular structure with separate files for different components
- Use class inheritance for organizing related components
- Use separate files for typed inputs/outputs, main functionality, and initialization
- Include an __init__.py file in each module, even if empty
- Import new modules in __init__.py and update the __all__ list

## 3. Documentation
- Include a README.md file for each module or component, providing:
  - Brief overview of contents and purpose
  - Table of contents for easy navigation
  - Usage instructions and context
  - Clear input and output specifications
- Use markdown formatting for documentation, including headers and lists
- Add docstrings to functions with detailed descriptions, including:
  - Parameters and their types
  - Return values and their types
  - Brief description of function purpose
- Use consistent docstring formats for each language (e.g., Google-style for Python, JSDoc for JavaScript, Javadoc for Java)

## 4. Error Handling
- Handle exceptions properly when importing modules
- Provide specific error messages for missing dependencies, including installation instructions

## 5. Security
- Use spec_from_file_location() and module_from_spec() instead of import_module() for dynamic imports
- Implement a whitelist approach for allowed module imports
- Avoid using f-strings with untrusted user input

## 6. Typing
- Use TypedDict for defining input and output structures
- Use Annotated for StepTypeConfig
- Use type annotations for improved code clarity
- Use type hints for function parameters and return values

## 7. Dependency Management
- Keep dependencies up-to-date with specified version ranges
- Use semantic versioning for dependencies (e.g., ^1.5.0, ~2.32.0)
- Pin transitive dependencies

## 8. Code Formatting
- Use Black for code formatting
- Use isort for import sorting
- Use consistent double quotes for dictionary keys

## 9. Version Control
- Follow versioning conventions for development versions (e.g., X.X.X.devX)
