# Documentation for `SendEmail` Module

This documentation outlines the `SendEmail` module which is part of a codebase under the directory `patchwork/steps/SendEmail`. The module is designed for sending emails using SMTP, specifically configured for Gmail by default. This module can be reused and adapted to send custom email messages in applications that require email communication.

## Overview

The `SendEmail` module is implemented using Python and functions as a step within a larger workflow system called Patchwork. It uses Simple Mail Transfer Protocol Secure (SMTPS) to send emails securely. Users can customize the email contents using mustache-style templates for both the body and subject of the email.

### Structure

- **File: `patchwork/steps/SendEmail/__init__.py`**
  - This file is empty with placeholders for package initialization.
  
- **File: `patchwork/steps/SendEmail/SendEmail.py`**
  - This file contains the main implementation of the `SendEmail` class.
  
- **File: `patchwork/steps/SendEmail/typed.py`**
  - This file defines typed input and output interfaces for the `SendEmail` class.

## Inputs

The `SendEmail` class accepts a set of input parameters to configure and send an email:

- **`sender_email` (str):** The email address from which the email will be sent.
- **`recipient_email` (str):** The email address to which the email will be sent.
- **`sender_email_password` (str):** Password for authenticating the sender's email account.
- **`email_template_value` (dict, optional):** A dictionary of values to replace variables in the email's body and subject (`default: {}`).
- **`subject` (str, optional):** The subject line of the email (`default: "Patchwork Execution Email"`).
- **`body` (str, optional):** The content/body of the email (`default: "Patchwork Execution Email"`).
- **`smtp_host` (str, optional):** SMTP host server address (`default: "smtp.gmail.com"`).
- **`smtp_port` (int, optional):** Port number for SMTP server (`default: 465`).
- **`reply_message_id` (str, optional):** Message ID for threading emails.

These parameters are encapsulated within the `SendEmailInputs` typed dictionary.

## Outputs

Currently, the class does not produce any outputs, represented by an empty `SendEmailOutputs` typed dictionary.

## Usage

### Initializing and Running `SendEmail`

To use the `SendEmail` class, instantiate it with an `inputs` dictionary containing the necessary parameters. The `run()` method is used to execute the email sending operation:

```python
from patchwork.steps.SendEmail.SendEmail import SendEmail

inputs = {
    "sender_email": "example@gmail.com",
    "recipient_email": "recipient@example.com",
    "sender_email_password": "yourpassword",
    "subject": "Subject of the Email",
    "body": "This is the body of the email.",
    "email_template_value": {"name": "Recipient Name"},
}

email_sender = SendEmail(inputs)
email_sender.run()
```

### Customization

- Email content can be dynamically generated using the `mustache_render` method from `patchwork.common.utils.utils`, allowing for template variables in the email body and subject.
- The class supports SMTP SSL by default, using Gmail's SMTP server. Modifications would be needed to support other SMTP configurations.

### Security Note

- The sender's email password is required to authenticate with the SMTP server. Ensure this information is securely managed, potentially using environment variables or encrypted vaults.

This module provides a mechanism for sending emails within an application, facilitating automated messaging capabilities integrated into Python applications using Patchwork.
