# ReadEmail Module Documentation

This documentation provides an overview of the `ReadEmail` module, which is responsible for reading and extracting data from `.eml` files. The module processes email files, extracting headers, body content, and attachments, and making them accessible for further processing.

## File Overview

- **`__init__.py`**: An initialization file for the package (empty).
- **`ReadEmail.py`**: Contains the core logic for reading and parsing email data.
- **`typed.py`**: Defines input and output data structures using `TypedDict`.

## `ReadEmail.py`

### Functionality

`ReadEmail.py` provides functionality to parse `.eml` files. It uses the `EmlParser` library to decode emails and extract important components such as headers, body, and attachments.

### Class: Parsed Models

1. **ParsedHeader**
   - Parses email headers like `subject`, `from`, `to`, and `date`.
   
2. **ParsedBody**
   - Represents email body content and content type.
   
3. **AttachmentHeader**
   - Captures header details of attachments, including content disposition, encoding, and type. 

4. **ParsedAttachment**
   - Handles the actual attachments, storing filenames, raw data, and headers.

5. **ParsedEmail**
   - Combines the header, body, and attachments into a cohesive structure.

### Class: ReadEmail

This class processes the `.eml` file and extracts data using the defined models.

#### Inputs

- **`eml_file_path`**: Path to the `.eml` file to be processed.
- **`base_path`** (optional): Base path for saving extracted attachments.

#### Main Method: `run()`

- **Email parsing**: Utilizes `EmlParser` to decode email content.
- **Data extraction**: Extracts subject, sender, attachments, bodies, and message ID.
- **Attachment handling**: Decodes and saves attachments to the specified `base_path`.

#### Helper Method: `__decode()`

- Used for decoding the content based on `content-transfer-encoding` (e.g., `base64`, `quoted-printable`).

### Outputs

- **`subject`**: Email subject line.
- **`datetime`**: The date/time the email was sent.
- **`from`**: Sender of the email.
- **`attachments`**: List of attachments with file paths.
- **`body`**: Concatenated body content of the email.
- **`message_id`**: Unique message identifier.

## `typed.py`

### Input Definitions

- **`ReadEmailInputs`**: Specifies required `eml_file_path` and optional `base_path` for attachments.

### Output Definitions

- **`ReadEmailOutputs`**: Structure for the expected output, including email `subject`, `from`, `body`, `message_id`, and `attachments`.

## Usage

To use the `ReadEmail` module, instantiate the `ReadEmail` class with appropriate inputs and call the `run` method to extract email information. This will return a structured dictionary containing the parsed email components, providing an easy way to access email content and attachments. This module is useful for applications involving email processing, archiving, or automated responses based on email content.
