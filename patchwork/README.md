# Table of Contents for Patchwork

Patchwork is a tool that uses Large Language Models (LLMs) to automate various software engineering tasks. It consists of several modules and steps that can be combined to create "patchflows" for tasks like vulnerability fixing, dependency upgrades, and more.

## Modules

1. **logger.py**: Handles logging, including rich terminal output and progress bar integration.
2. **step.py**: Defines the base `Step` class and related types for the workflow steps.
3. **app.py**: Provides the command-line interface (CLI) for running patchflows.
4. **managed_files.py**: Defines the locations of various configuration and log files.
5. **common/**: Contains shared utility functions and client implementations for external services like Git, LLMs, and security scanning tools.
6. **steps/**: Defines the various steps that can be used in patchflows, such as code extraction, LLM calls, code modification, and pull request management.
7. **patchflows/**: Defines the pre-built patchflows for common tasks like vulnerability fixing, dependency upgrades, and more.

## Inputs and Outputs

The main inputs and outputs for the Patchwork tool are:

**Inputs**:
- Source code files
- Package manager files (e.g., `requirements.txt`, `package.json`)
- Issue/PR details (title, description, comments)
- Vulnerability/bug details
- LLM API keys and configuration

**Outputs**:
- Modified source code files with vulnerabilities/bugs fixed
- Updated package manager files with dependencies upgraded
- Pull requests with changes
- Issue/PR comments with analysis and suggestions
- Vulnerability/bug reports

The specific inputs and outputs for each step and patchflow are defined in the respective modules and documented using type annotations.

## Usage

Patchwork is primarily used as a command-line tool, with the main entry point being the `patchwork` command. Users can run pre-built patchflows or create their own custom workflows by combining the various steps.

Example usage:
```
patchwork run-patchflow AutoFix --github-token <token> --repository-url <repo_url>
```

This will run the `AutoFix` patchflow, which will automatically detect and fix vulnerabilities in the specified repository.

The tool can also be used as a library, with the various steps and patchflows being importable and customizable as needed.

## Extensibility

Patchwork is designed to be extensible, allowing users to create their own custom steps and patchflows. This is done by subclassing the `Step` class and implementing the required methods and inputs/outputs.

Additionally, Patchwork supports different LLM providers (OpenAI, Anthropic, Google) and can be extended to support additional providers as needed.

Overall, Patchwork is a powerful tool for automating various software engineering tasks using the capabilities of Large Language Models.