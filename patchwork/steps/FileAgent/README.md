# Documentation: FileAgent Module

The `FileAgent` module is designed to facilitate file processing tasks using a combination of advanced strategies and tools. It is structured into multiple Python files that define the types of inputs and outputs, as well as the main agent class that carries out the tasks. The module can handle tasks associated with various file types, especially tabular formats such as CSV, XLS, and XLSX.

## Files and Overview

### File: `typed.py`

This file defines the input and output types for the `FileAgent`.

#### Inputs

- **`task`** (str): The primary task to be performed by the agent.
- **`base_path`** (str, optional): The base directory path where files are located.
- **`prompt_value`** (Dict[str, Any], optional): Values for dynamic task prompts.
- **`max_llm_calls`** (int): Maximum number of LLM (Language Learning Model) calls allowed. This is a configuration parameter.
- **API Keys** (str): OpenAI, Anthropic, and Google API keys are configured with mutual exclusions to ensure one is always provided:
  - **`openai_api_key`**
  - **`anthropic_api_key`**
  - **`google_api_key`**

#### Outputs

- **`request_tokens`** (int): The number of tokens used in request.
- **`response_tokens`** (int): The number of tokens received in response.

### File: `FileAgent.py`

This file contains the main `FileAgent` class implementing the file processing strategy.

#### Inputs

The class accepts the `FileAgentInputs` data structure defined in `typed.py` as its inputs.

#### Outputs

The class outputs are in the form of `FileAgentOutputs` structure, which includes token usage during the communication process.

#### Functionality

- **Initialization**: Sets the base path and derives the task to be executed.
- **Strategies and Tools**: 
  - Uses `AgenticStrategyV2` to dictate agent behavior.
  - Integrates tools such as CSV converters and text finders.
  - Configures specific agent settings, including model specifications and prompt templates.
- **Execution**: 
  - Creates and manipulates temporary directories.
  - Executes strategies using defined tools.
  - Returns processed results including token usage.

### File: `__init__.py`

This file currently serves as a placeholder and does not contain any specific logic or definitions.

## Usage

This module primarily suits developers building systems that require automated file handling, particularly with tabular data formats. By setting up an appropriate configuration and providing the necessary API keys, the `FileAgent` can be used to handle complex file processing tasks automatically, integrating machine learning models and multi-turn strategies to refine outcomes.

### Prerequisites

- Installation of dependencies related to AI models and file processing.
- Valid API keys for OpenAI, Anthropic, or Google services.
- Basic knowledge of Python for setting up configurations and invoking the `FileAgent`.

This documentation provides a comprehensive overview of the module, highlighting its capabilities and integration points for effective utilization in automated file handling scenarios.
