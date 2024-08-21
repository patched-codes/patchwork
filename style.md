# Code Style Guidelines

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
