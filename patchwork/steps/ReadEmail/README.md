# ReadEmail Module Documentation

## Overview
The ReadEmail module is designed to parse and extract data from email files in `.eml` format. This module decodes and retrieves email metadata, body content, and any attachments, then returns them in a structured form. It is likely used within workflows where emails need to be processed programmatically, such as automated sorting, storage, logging, or further analysis of email content.

## Structure
The module is organized into three Python files:

1. `__init__.py`: Initializes the module. This file is empty.
2. `ReadEmail.py`: Contains the main functionality of parsing emails.
3. `typed.py`: Defines the input and output data structures used by ReadEmail.

## File: ReadEmail/ReadEmail.py

### Functionality
- **Classes and Models**:
  - `InnerParsedHeader`, `ParsedHeader`, `ParsedBody`, `AttachmentHeader`, `ParsedAttachment`, `ParsedEmail`: Pydantic models that represent structured parts of an email, such as headers, bodies, and attachments.
  
- **ReadEmail Class**: 
  - Inherits from the `Step` class.
  - Uses `ReadEmailInputs` and `ReadEmailOutputs` for input and output definitions.
  - Contains a method called `run()`.

### Inputs
- `eml_file_path`: Path to the `.eml` file to be parsed.
- `base_path`: Optional base directory where attachments are saved (defaults to the current working directory).

### Outputs
- Returns a dictionary with the following keys:
  - `subject`: The subject of the email.
  - `datetime`: The date and time the email was sent.
  - `from`: The sender's email address.
  - `body`: The content of the email body.
  - `message_id`: Unique message identifier.
  - `attachments`: A list of attachments with their saved file paths.

### Usage
To use the `ReadEmail` step, instantiate it with a dictionary containing at least an `eml_file_path`, then run it to extract the information. This can be integrated into larger workflows for tasks like automated email processing.

## File: ReadEmail/typed.py

### Inputs
Defines the structure for accepted inputs using `TypedDict`:
- `ReadEmailInputs`: Contains:
  - `eml_file_path`: The mandatory path to the `.eml` file.
  - `base_path`: Optional directory path where the attachments are stored.

### Outputs
Defines the structure for output data:
- `ReadEmailOutputs`: Contains:
  - `subject`, `datetime`, `from_`, `body`, `message_id`.
  - `attachments`: List of `Attachment` dictionaries.

### Usage
The `typed.py` file is primarily meant for type checking and ensures that inputs and outputs adhere to defined data structures within the `ReadEmail` class. This helps maintain code integrity and readability in complex workflow applications.
