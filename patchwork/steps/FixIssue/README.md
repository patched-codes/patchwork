# Patchwork Fix Issue Documentation

This module is part of the Patchwork repository that offers a structured method to automate the fixing of code issues using AI. The primary functionality involves analyzing code repositories to identify problems based on a given description and implementing the necessary code changes.

## Overview

The module includes:

- Typed definitions for managing input and output structures (`typed.py`).
- The main logic to process issues (`FixIssue.py`).
- An initialization file (`__init__.py`).

## Files Description

### 1. `typed.py`

This file contains type definitions, ensuring structured handling of input and output data.

#### Inputs

- `FixIssueInputs`:
  - **issue_description** (str): A required field describing the issue to be fixed.
  - **base_path** (str): An optional file path where the repository exists.
  - **openai_api_key, anthropic_api_key, patched_api_key, google_api_key** (str): Optional API keys used to authenticate with AI services. The configuration supports multiple APIs for flexibility.

#### Outputs

- `FixIssueOutputs`:
  - **modified_files** (List[Dict]): A list of dictionaries detailing the files modified as part of the fix.

### 2. `FixIssue.py`

This file implements the core logic for analyzing and fixing code issues.

#### Functionality

- **Class `_ResolveIssue`**: 
  - Utilizes the AI client to analyze the repository structure and locate specific files and code sections needing modifications.
  - Provides structured templates for both analysis and implementation steps, ensuring comprehensible interaction with the AI model.

- **Class `FixIssue`**:
  - Extends from `Step`, using `FixIssueInputs` for inputs and `FixIssueOutputs` for outputs.
  - Initiates and runs the multiturn strategy to handle complex issues through a series of interactions with a Large Language Model (LLM).

#### Inputs

- Accepts comprehensive structured inputs as defined in `typed.py`.

#### Outputs

- Generates a list of modified files as output after executing the strategy to resolve the issue.

### 3. `__init__.py`

A placeholder for module initialization. Currently empty, serving as an indicator for the Python module structure.

## Usage

- **Setup**: Ensure API keys are configured for the available AI services.
- **Run**: Invoke the main `FixIssue` class with the necessary inputs, including a description of the issue and optional paths or API keys.
- **Output**: Receives a summary of the files that were modified as part of the problem-solving process.

This module is typically used by developers looking to leverage AI for automated code fixes in complex projects, particularly those using version control systems like Git. Integration with AI models like OpenAI or Anthropic ensures versatile problem-solving capabilities.
