# Code Style Guidelines

## 1. Naming Conventions
- Use snake_case for function and variable names in Python, camelCase for JavaScript and Java
- Use PascalCase for class names
- Use descriptive and clear names for variables, functions, and classes

## 2. Code Structure
- Use modular structure, class inheritance, and separate files for components
- Organize imports with standard library imports first
- Use relative imports for internal modules
- Implement proper limits and pagination for data retrieval functions

## 3. Documentation
- Use markdown for README files, including a Table of Contents
- Provide clear documentation for inputs, outputs, and functionality
- Use docstrings for functions, methods, and classes
- Follow language-specific documentation formats (JSDoc for JavaScript, Javadoc for Java, Google-style for Python)
- Include parameter descriptions and return types in docstrings
- Keep code documentation and comments up-to-date with changes

## 4. Error Handling
- Implement proper error handling and logging
- Use specific exception handling instead of broad except clauses
- Provide clear and informative error messages

## 5. Performance
- Use list comprehensions for concise list creation in Python
- Prefer 'get' method for dictionary access to avoid KeyError

## 6. Security
- Use whitelist approach for module imports to prevent running untrusted code
- Avoid using untrusted user input in importlib.import_module()
- Use spec_from_file_location() and module_from_spec() for safer module imports
- Ensure proper security measures for API keys and secrets

## 7. Code Quality
- Use type hints and annotations (TypedDict, Annotated) for function and class definitions
- Follow PEP 8 style guidelines for Python
- Use Black for code formatting and isort for import sorting
- Use static type checking (mypy)
- Simplify complex logic and improve code readability

## 8. Dependency Management
- Use specific version ranges for dependencies
- Keep dependencies up-to-date
- Use semantic versioning
- Use Poetry for dependency management in Python projects

## 9. Version Control
- Follow versioning conventions for development versions

## 10. Testing
- Thoroughly test code changes, especially for substantial modifications