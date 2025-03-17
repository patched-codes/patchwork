# FileAgent Module Documentation

This documentation provides an overview of the `FileAgent` module, which is part of the `patchwork` project. The module consists of a primary class `FileAgent` and associated type definitions, utilizing the Python language for file handling and operations with structured data.

## Contents

- **FileAgent Functionality**
- **Inputs**
- **Outputs**

## FileAgent Functionality

The `FileAgent` class is designed for working with a set of files, particularly those in tabular formats such as CSV, XLS, or XLSX. It leverages an AI model (claude) for processing tasks, employs various tools to manipulate and analyze file data, and executes strategies to obtain desired file transformations and data summaries. Additionally, it offers a flexible configuration mechanism for API keys and task customization.

### Primary Components:
- **File Handling**: Utilizes tools like `FileViewTool`, `FindTextTool`, `CSVSQLTool`, and `In2CSVTool` to manage and convert files.
- **AI Strategy Execution**: Uses `AgenticStrategyV2` with a language model to execute tasks involving file contents.
- **Configuration**: Allows easy customization of tasks and API integration through input parameters.

## Inputs

The `FileAgent` class requires inputs as defined in the `FileAgentInputs` type:

- **task** (_str_): A string representation of the task to be executed.
- **base_path** (_str, optional_): The base directory path where files are located. Defaults to the current working directory.
- **prompt_value** (_Dict[str, Any], optional_): Additional data needed for rendering tasks with context.
- **max_llm_calls** (_int_): Configuration for the maximum number of large language model (LLM) calls allowed.
- **anthropic_api_key** (_str_): API key for Anthropic, necessary for accessing AI functionalities.

## Outputs

The outputs of the `FileAgent` class are specified by `FileAgentOutputs`:

- **request_tokens** (_int_): The number of tokens used in the file request.
- **response_tokens** (_int_): The number of tokens provided in the response.

## Usage Instruction

To utilize the `FileAgent` class, initialize it with a dictionary of inputs adhering to `FileAgentInputs`. Then, execute the `run` method to process the files as per the specified task. This procedure will convert and manipulate files, leveraging AI capabilities to achieve the task goals. Make sure API configurations and required paths are correctly set in the inputs.

This module is ideal for developers or data scientists who need to automate file processing and manipulation tasks, especially in projects involving multiple file formats and AI-driven tasks.
