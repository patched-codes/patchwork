# ReadEmail Module Documentation

This documentation describes the ReadEmail module, which is structured to facilitate the reading and parsing of email files encoded in the `.eml` format. The module is divided across three main source files: `__init__.py`, `ReadEmail.py`, and `typed.py`. Below, we describe the functionalities of these components, including input and output specifications.

---

## 1. Overview

The ReadEmail module is designed to read `.eml` files, parse the email headers, body, and attachments, and return this data in a structured form. It's intended for applications where email processing and analysis are required, such as in email clients, document processing systems, or automated data extraction tasks.

---

## 2. Files

### 2.1. `__init__.py`

This file is an empty file created to make the directory a Python package. It contains no code or logic.

### 2.2. `ReadEmail.py`

This file contains the main logic of the ReadEmail module. Below is a breakdown of its components.

#### 2.2.1. Classes

- **ParsedHeader**: Represents the parsed email header with fields such as `subject`, `from`, `to`, and `date`.
- **ParsedBody**: Represents the content and content type of the email body.
- **AttachmentHeader**: Contains fields related to the attachment's header such as content disposition and encoding.
- **ParsedAttachment**: Represents an attachment with fields including `filename`, `raw` content, and `content_header`.
- **ParsedEmail**: Combines all parsed data (header, body, attachment).
- **ReadEmail**: Inherits from the `Step` class and contains the core functionality for running the email parsing task.

#### 2.2.2. Key Methods

- **`__decode`**: Decodes the email content based on its encoding, e.g., `base64` or `quoted-printable`.
- **`run`**: Executes the parsing process using `EmlParser`, processes email data, attaches parsed data, and decodes attachments.

### 2.3. `typed.py`

This file defines the input and output types used by the `ReadEmail` class.

#### 2.3.1. Inputs

- `eml_file_path`: Path to the `.eml` email file to be processed.
- `base_path`: (Optional) Base directory path where attachments should be saved.

#### 2.3.2. Outputs

- `subject`: Email subject.
- `datetime`: Date and time the email was sent.
- `from_`: Sender's email.
- `body`: Full body text of the email.
- `message_id`: Unique message identifier.
- `attachments`: List of attachments with file paths.

---

## 3. Usage

To utilize the ReadEmail module effectively, instantiate the `ReadEmail` class with the required inputs and execute the `run` method. The `run` method will parse the email and return a dictionary containing the parsed data.

### Example

```python
inputs = {
    "eml_file_path": "path/to/email.eml",
    "base_path": "path/to/save/attachments"
}

read_email = ReadEmail(inputs)
parsed_data = read_email.run()

print(parsed_data["subject"])
print(parsed_data["body"])
for attachment in parsed_data["attachments"]:
    print(attachment["path"])
```

This example will print out the email subject, body, and paths to any attachments extracted from the specified `.eml` file.

---

By following this guide, users can effectively integrate and utilize the ReadEmail module for processing and extracting information from `.eml` files in their applications.
