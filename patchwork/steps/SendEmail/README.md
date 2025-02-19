# Documentation: SendEmail Module

This module allows users to send emails using the SMTP protocol with customizable templates and email parameters.

## File: `SendEmail.py`

This file defines the main class `SendEmail`, which extends a base `Step` class, providing functionality to send an email through an SMTP server.

### Inputs

The `SendEmail` class expects the following inputs:

- **sender_email** (_str_): The email address that sends the email.
- **recipient_email** (_str_): The email address to receive the email.
- **smtp_username** (_str_): The username for the SMTP server.
- **smtp_password** (_str_): The password for the SMTP server.
- **email_template_value** (_dict_) [_Optional_]: Values to customize the email template.
- **subject** (_str_) [_Optional_]: The subject of the email. Defaults to "Patchwork Execution Email".
- **body** (_str_) [_Optional_]: The body content of the email. Defaults to "Patchwork Execution Email".
- **smtp_host** (_str_) [_Optional_]: The SMTP server host. Defaults to "smtp.gmail.com".
- **smtp_port** (_int_) [_Optional_]: Port for the SMTP server. Defaults to 25.
- **reply_message_id** (_str_) [_Optional_]: ID of the message being replied to.
- **is_smtp_ssl** (_bool_) [_Optional_]: Whether to use SSL for the SMTP connection. Defaults to `False`.

### Core Functionality

1. **Initialization**: The class initializes with the specified inputs and extracts necessary details for email configuration.
2. **Email Rendering**: The email's subject and body can use Mustache templates for dynamic content, customized by `email_template_value`.
3. **SMTP Connection**: The class handles both SSL-enabled and non-SSL SMTP connections, allowing secure email sending if necessary.
4. **Email Sending**: Logs into the SMTP server using provided credentials and sends the crafted email to the recipient.
5. **Header Management**: Optionally adds "Reference" and "In-Reply-To" headers if responding to a previous email.

### Outputs

The `SendEmail` class does not return any specific output upon execution, as indicated by the empty `SendEmailOutputs` dictionary.

## File: `typed.py`

This file defines the input and output structures used in the `SendEmail` class:

### Inputs

Defines the `SendEmailInputs`, which include both required inputs (as a subclass of `__SendEmailRequiredInputs`) and optional fields for email configurations.

### Outputs

Defines the `SendEmailOutputs`, which remains an empty `TypedDict` as no outputs are produced by the `SendEmail` step, indicating the module's execution results in side effects rather than data returns.

## Usage

Users are expected to instantiate the `SendEmail` class with a dictionary of inputs meeting the requirements noted above. The `run` method can be called to execute the email sending process. This configuration allows integrating this class in broader email automation workflows or job execution notifications.
