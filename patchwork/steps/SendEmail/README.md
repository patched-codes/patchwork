# SendEmail Package Documentation

This documentation provides an overview of the `SendEmail` package used within the `patchwork` project. The package consists of Python scripts for sending emails with customizable templates and SMTP configurations.

## Overview

The `SendEmail` package includes three files:

1. **`__init__.py`** – an empty file indicating that the directory is a Python package.
2. **`SendEmail.py`** – contains the main logic for sending emails using SMTP.
3. **`typed.py`** – defines typed structures for inputs and outputs of the email sending step.

## File Contents

### 1. `__init__.py`

- **Purpose**: Marks the directory as a Python package.
- **Contents**: No code content, serves structural purposes.

### 2. `SendEmail.py`

#### Description

This file implements the `SendEmail` class, which inherits from the `Step` class. It manages the creation and sending of emails using SMTP with optional SSL support. It utilizes Jinja-like templating (`mustache_render`) for the email content.

#### Inputs

The `SendEmail` class requires several inputs to be specified:

- **`sender_email`** *(str)*: The email address from which the email will be sent.
- **`recipient_email`** *(str)*: The recipient's email address.
- **`smtp_username`** *(str)*: SMTP server username.
- **`smtp_password`** *(str)*: Password for the SMTP server.
- **Optional Parameters**:
  - `email_template_value` *(dict)*: Key-value pairs for templating email content.
  - `subject` *(str)*: Subject of the email. Default is "Patchwork Execution Email".
  - `body` *(str)*: Body content of the email. Default is "Patchwork Execution Email".
  - `smtp_host` *(str)*: SMTP host to connect to. Default is "smtp.gmail.com".
  - `smtp_port` *(int)*: Port for the SMTP server. Default is port 25.
  - `reply_message_id` *(str)*: Reference message ID for replies.
  - `is_smtp_ssl` *(bool)*: Use SSL for SMTP if set to `True`.

#### Outputs

- Returns an empty dictionary as a placeholder for outputs.

#### Usage

A user can instantiate the `SendEmail` class by providing a dictionary with the required input parameters, and then call the `run` method to send an email.

### 3. `typed.py`

#### Description

Defines the typed structures for input and output to ensure type safety and clarity.

#### Classes

- **`__SendEmailRequiredInputs`** *(TypedDict)*: Specifies required email parameters: `sender_email`, `recipient_email`, `smtp_username`, and `smtp_password`.
- **`SendEmailInputs`** *(TypedDict)*: Extends required inputs with optional fields.
- **`SendEmailOutputs`** *(TypedDict)*: Placeholder dictionary with no fields.

## Conclusion

The `SendEmail` package in Patchwork provides a robust framework for sending templated emails using a customizable SMTP setup, supporting both SSL and non-SSL connections. It can be easily integrated into automated workflows for sending execution notifications or other types of emails defined by the user.
