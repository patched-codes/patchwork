# Patchwork Email Reader

This module provides functionality to read and parse email files in the `.eml` format. It decodes the email content, including headers, body, and attachments, and structures the data into easily manageable Python objects. The module is designed to be part of a larger application, potentially for systems that need to process or analyze email data programmatically.

## Files Overview

- `__init__.py`: An initializer file for the module (currently empty).
- `ReadEmail.py`: Contains the main logic for reading and parsing `.eml` files.
- `typed.py`: Defines the input and output data types using `TypedDict`.

---

## ReadEmail.py

### Inputs

- **eml_file_path** (str): Path to the `.eml` file to be read. This is a mandatory input.
- **base_path** (str, optional): The base directory where email attachments will be saved. Defaults to the current working directory.

### Outputs

- **subject** (str): The subject of the email.
- **datetime** (str): The timestamp indicating when the email was sent.
- **from** (str): Sender's email address. 
- **body** (str): The main content of the email.
- **message_id** (str): Unique identifier of the email message.
- **attachments** (List[Attachment]): List of attachments in the email, each described with a path to the saved file.

### How It Works

1. **Initialization:** The `ReadEmail` class is initialized with the inputs, which specify the location of the `.eml` file and the optional base path for saving attachments.
  
2. **Email Parsing:** The `run` method utilizes the `EmlParser` to decode the email file and extract relevant data.

3. **Header Decoding:** Extracts information such as subject line, sender, recipients, and timestamp from the email headers.

4. **Body and attachments:** Parses email bodies and decodes attachments, saving them to the specified directory.

5. **Output Construction:** Constructs and returns a dictionary containing all of the email's parsed information structured as defined by `ReadEmailOutputs`.

### Usage

This file is likely used as part of an email processing pipeline where `.eml` files are input and data needs to be stored or further processed. For example, it might be used in applications that archive emails, extract insights from email meta-data, or manage email attachments automatically.

---

## typed.py

### Inputs

- **ReadEmailInputs**: Specifies required and optional inputs for reading an email.
  - `eml_file_path`: Path to the `.eml` file.
  - `base_path` (optional): Directory for saving attachments.

### Outputs

- **ReadEmailOutputs**: Defines the structured data returned after parsing.
  - Consists of fields like `subject`, `datetime`, `from_`, `body`, `message_id`, and `attachments`.

### How It Works

This file provides type definitions that help ensure input and output data conforms to expected formats, improving reliability and maintainability of the system.

---

By leveraging this module, applications can effectively handle and manipulate email data in `.eml` format, with a clear structure to access various components of an email seamlessly.
