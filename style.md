# Code Style Guidelines

## 1. Naming Conventions
- Use snake_case for function and variable names in Python
- Use camelCase for function names in JavaScript and method names in Java
- Use PascalCase for class names
- Use UPPERCASE_WITH_UNDERSCORES for constants
- Use clear and descriptive names for all identifiers

## 2. Code Structure
- Follow a modular structure with separate files for different components
- Use class inheritance for organizing related components
- Organize imports logically and remove unused imports
- Include an __init__.py file in each Python module, even if empty
- Break down complex methods into smaller, well-defined functions
- Use TypedDict for defining input and output structures in Python
- Use type annotations for function parameters and return values
- Upgrade minimum Python version from 3.8 to 3.9 for newer language features

## 3. Documentation
- Include a README.md file for each module or component, providing:
  - Brief overview of contents and purpose
  - Table of contents for easy navigation
  - Usage instructions and context
  - Clear input and output specifications
- Use markdown formatting for documentation, including headers and lists
- Add comprehensive docstrings to all functions and methods, including:
  - Brief description of function purpose
  - Parameters and their types
  - Return values and their types
  - Usage examples where appropriate
- Use consistent docstring formats for each language (e.g., Google-style for Python, JSDoc for JavaScript, Javadoc for Java)
- Provide clear and concise comments for complex operations or security measures

## 4. Error Handling and Logging
- Implement proper error handling and logging, especially for edge cases and exceptions
- Use specific error types and provide informative error messages
- Handle exceptions properly when importing modules
- Use a logging mechanism (e.g., Python's logging module) for error reporting and debugging

## 5. Security
- Use spec_from_file_location() and module_from_spec() instead of import_module() for dynamic imports
- Implement a whitelist approach for allowed module imports to prevent arbitrary code execution
- Validate and sanitize user inputs, particularly for JSON schemas and API responses
- Avoid using f-strings with untrusted user input

## 6. Dependency Management
- Use package managers (e.g., Poetry for Python, npm/yarn for JavaScript) for dependency management
- Keep dependencies up-to-date with specified version ranges
- Use semantic versioning for dependencies (e.g., ^1.5.0, ~2.32.0)
- Pin transitive dependencies for reproducible builds
- Regularly update dependencies to address security vulnerabilities

## 7. Code Formatting and Style
- Use automated formatting tools (e.g., Black for Python, Prettier for JavaScript)
- Use static analysis tools (e.g., pylint, eslint) to enforce coding standards
- Maintain consistent indentation and line breaks
- Use consistent double quotes for string literals and dictionary keys
- Use isort or similar tools for sorting imports

## 8. Testing
- Write unit tests to cover functionality and edge cases
- Use mocking to isolate units in testing
- Aim for high test coverage
- Update and expand tests when adding new functionality or changing existing code

## 9. Version Control
- Follow semantic versioning conventions (MAJOR.MINOR.PATCH)
- Use descriptive commit messages
- Create feature branches for new development
- Use .gitignore to exclude unnecessary files from version control

## 10. Performance
- Use appropriate data structures and algorithms for efficient operations
- Implement caching mechanisms where applicable
- Optimize database queries and API calls
- Use asynchronous programming techniques when dealing with I/O-bound operations
