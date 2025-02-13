# ReadEmail Module Documentation

This documentation provides an overview of the `ReadEmail` module, which consists of three Python files: `__init__.py`, `ReadEmail.py`, and `typed.py`. This module is designed to process `.eml` files, extract email data, and handle email attachments. It is primarily used within a larger workflow for handling email data.

## Overview

The `ReadEmail` module is part of a larger framework called Patchwork, which is used to build workflows by defining steps. This module specifically focuses on reading and processing email files and exposes functionality to extract valuable information such as subject, sender, recipients, body content, and attachments from the email.

## `__init__.py`

This file is empty, serving as the initializer for the Python package, enabling import statements for the module components.

## `ReadEmail.py`

### Description

The `ReadEmail.py` file contains the core logic for reading and parsing `.eml` files using the `eml_parser` library. It defines several data models to represent different parts of an email, such as headers, bodies, and attachments. The `ReadEmail` class, which derives from a base `Step` class, manages the main workflow for processing the email file and extracting its contents.

### Inputs

- **`eml_file_path`** (required): The file path to the `.eml` file that needs to be processed.
- **`base_path`** (optional): The directory path where email attachments will be stored. Defaults to the current working directory if not specified.

### Outputs

- **`subject`**: The subject of the email.
- **`datetime`**: The datetime when the email was sent.
- **`from_`**: The sender of the email.
- **`body`**: The main body content of the email.
- **`message_id`**: A unique identifier for the email message.
- **`attachments`**: A list of dictionaries containing the paths and content of any attachments.

### How It Works

1. **Initialization**: The class is initialized with the required input paths for processing.
2. **Email Parsing**: Utilizes `EmlParser` to decode the email file, extracting the email structure into data models.
3. **Attachment Handling**: Decodes and writes email attachments to the specified directory.
4. **Return Values**: The run method returns a dictionary with structured email data, making it easy to integrate with other parts of an application or workflow.

## `typed.py`

### Description

This file defines the expected input and output types for the `ReadEmail` step, leveraging Python's type hinting and `TypedDict` to provide clear contracts for interacting with the `ReadEmail` class.

### Inputs

- **`__ReadEmailRequiredInputs`**: Defines mandatory inputs like `eml_file_path`.
- **`ReadEmailInputs`**: Extends the required inputs to include optional ones like `base_path`.

### Outputs

- **`Attachment`**: Specifies the structure of an attachment.
- **`ReadEmailOutputs`**: Enumerates the expected output fields with types such as `subject`, `datetime`, `from_`, `body`, `message_id`, and `attachments`.

This module can be used wherever there is a need to automate the extraction of data from email files, making it particularly useful for systems designed to process and analyze email content automatically.
