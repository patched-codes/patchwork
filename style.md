# Code Style Guidelines

## 1. Code Structure
- Use type annotations for function parameters and return values
- Separate variable assignment from dictionary creation for clarity
- Use list comprehension for concise code

## 2. Error Handling
- Use try-except blocks for import operations
- Use default values for potentially None attributes

## 3. Security
- Use whitelists to restrict module imports

## 4. Documentation
- Use logger for debugging and info messages

## 5. Dependency Management
- Keep dependencies up-to-date
- Use specific version constraints for dependencies

## 6. Version Control
- Use workflow_dispatch with version input for release automation
- Use 'poetry version' command to update version before publishing
- Update version in pyproject.toml to reflect development status

## 7. Configuration
- Use TOML format for project configuration