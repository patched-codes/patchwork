# Code Style Guidelines

## 1. Naming Conventions
- Use snake_case for function and variable names in Python
- Use camelCase for function and variable names in JavaScript and Java
- Use PascalCase for class names

## 2. Code Structure
- Organize imports at the beginning of the file, sorted alphabetically
- Use isort for import sorting
- Use separate files for different aspects of a component (e.g., input/output type definitions, main logic)
- Use __init__.py files for package initialization
- Use dataclasses for structured data
- Use TypedDict for defining input and output types
- Separate required and optional inputs in class and TypedDict definitions
- Add a newline at the end of files

## 3. Documentation
- Include detailed README.md files for each component or module, with a Table of Contents
- Use docstrings for functions, methods, and classes
- Include parameter descriptions and return value information in docstrings
- Use language-specific docstring formats (e.g., JSDoc for JavaScript, Javadoc for Java, and Google-style for Python)
- Use Markdown format for README files
- Include clear titles, input/output specifications, and usage instructions in documentation

## 4. Error Handling
- Implement proper error handling and logging
- Use try-except blocks for import operations and potential errors
- Provide specific error messages for missing dependencies
- Use default values for potentially None attributes
- Add input validation for optional parameters
- Handle potential exceptions within signal handlers to improve robustness

## 5. Performance
- Use list comprehensions for simple transformations

## 6. Security
- Avoid using untrusted user input directly in importlib.import_module()
- Use whitelists to restrict module imports
- Avoid using dynamic values in import_module() to prevent arbitrary code execution

## 7. Code Quality
- Follow PEP 8 style guidelines for Python
- Use Black for code formatting
- Use type hints for function parameters and return values
- Use f-strings consistently for string formatting
- Use constants for configuration values
- Use autoflake for removing unused imports

## 8. Dependency Management
- Use Poetry for managing Python package dependencies and publishing
- Update dependencies to newer versions to address vulnerabilities
- Use specific version ranges for dependencies (e.g., '~2.32.0', '^1.5.0')

## 9. Version Control
- Follow semantic versioning conventions
- Update version number in pyproject.toml for new releases
- Use workflow_dispatch with a version input for releases instead of tag-based triggers
- Use 'poetry version' command to set version dynamically in CI/CD pipeline

## 10. Testing
- Implement unit tests for new functions and methods

## 11. Logging
- Use logging to provide information about successful imports and debugging information for failed imports
- Use logger.info() for logging important events
- Use appropriate logging levels (debug, info) for different scenarios