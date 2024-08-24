# Code Style Guidelines

## 1. Naming Conventions
- Use snake_case for function and variable names in Python
- Use camelCase for function and variable names in JavaScript and Java
- Use PascalCase for class names
- Use descriptive names for variables, functions, and methods

## 2. Code Structure
- Organize imports at the beginning of the file, sorted alphabetically
- Use separate files for different aspects of a component
- Use modular structure and implement pagination where appropriate
- Add a newline at the end of files
- Use dataclasses for structured data
- Use TypedDict for defining input and output structures
- Separate input and output type definitions into a 'typed.py' file
- Use constants for frequently used string values or magic numbers

## 3. Documentation
- Include a detailed README.md file for each component or module, with a Table of Contents
- Use docstrings for functions, methods, and classes
- Include parameter descriptions, types, and return values in docstrings
- Use language-specific docstring formats (e.g., Google-style for Python, JSDoc for JavaScript, Javadoc for Java)
- Provide clear and concise comments to explain complex logic or new features

## 4. Error Handling
- Implement proper error handling and logging
- Use specific error messages for missing input data
- Handle exceptions appropriately when importing modules
- Implement exception handling for potential timeout errors in API requests
- Use specific exception types instead of general ones
- Check for None values before using variables

## 5. Performance
- Use list comprehensions for simple transformations
- Prefer 'get' method for dictionaries
- Add timeouts to API requests to prevent long-running operations

## 6. Security
- Avoid using dynamic values in importlib.import_module() to prevent code injection vulnerabilities
- Use whitelists to validate module names before importing
- Implement strict input validation for security-sensitive operations

## 7. Code Quality
- Follow PEP 8 style guidelines for Python
- Use Black for code formatting
- Use isort for import sorting
- Use type hints for function parameters and return values
- Use f-strings for string formatting
- Perform static type checking with mypy
- Use Path objects from pathlib for file operations

## 8. Dependency Management
- Use specific version ranges for dependencies (e.g., '~2.32.0', '^1.5.0')
- Keep dependencies up-to-date for security and compatibility
- Be cautious with dependency updates that may introduce breaking changes

## 9. Version Control
- Follow semantic versioning conventions
- Increment version number for bug fixes and improvements
- Update version numbers in pyproject.toml for new releases

## 10. Testing
- Thoroughly test code changes
- Implement unit tests for new functions and methods

## 11. CI/CD
- Use 'poetry version' command to set version dynamically in CI/CD pipeline
- Use workflow_dispatch with input for version in GitHub Actions