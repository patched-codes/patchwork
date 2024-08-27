# Code Style Guidelines

## 1. Naming Conventions
- Use snake_case for function and variable names.

## 2. Code Structure
- Use Black for code formatting.
- Use isort for import sorting.
- Use autoflake for removing unused imports.
- Use list comprehension for creating lists.

## 3. Documentation
- Use logging for debugging and informational messages.

## 4. Error Handling
- Use try-except blocks for handling import errors.
- Use default values for potentially null or empty fields.

## 5. Security
- Implement a whitelist for module imports to prevent loading arbitrary code.

## 6. Dependency Management
- Keep dependencies up-to-date with specific version constraints.

## 7. Testing
- Use pytest for testing.

## 8. Version Control
- Use semantic versioning for package versions.
- Use 'poetry version' command to update version before publishing.

## 9. CI/CD
- Use workflow_dispatch for manual triggering of GitHub Actions workflows.