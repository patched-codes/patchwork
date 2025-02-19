# SendEmail Module Documentation

## Overview

The `SendEmail` module facilitates the sending of emails through specified SMTP server credentials. This module is designed to be used in the context of running steps within a system, likely a workflow or a script automation tool named Patchwork, by taking advantage of template rendering and configurable email server details. 

## Input Files

### 1. `__init__.py`

#### Description
This file is an initialization script for the `SendEmail` submodule, serving to recognize it as a package. Currently, it is empty but it is critical for package structure within the Python ecosystem.

### 2. `SendEmail.py`

#### Description
This is the main file for sending emails. It defines a `SendEmail` class responsible for configuring the email details and executing the sending process using Python's `smtplib`.

#### Inputs
- **sender_email (str)**: The email address from which the email would be sent.
- **recipient_email (str)**: The recipient's email address.
- **smtp_username (str)**: Username to log into the SMTP server.
- **smtp_password (str)**: Password to log into the SMTP server.
- **email_template_value (dict, optional)**: Values to substitute in the email body and subject when using templates.
- **subject (str, optional)**: Subject of the email. Defaults to "Patchwork Execution Email".
- **body (str, optional)**: Content of the email. Defaults to "Patchwork Execution Email".
- **smtp_host (str, optional)**: The SMTP server address. Defaults to "smtp.gmail.com".
- **smtp_port (int, optional)**: The port number for the SMTP server. Defaults to 25.
- **reply_message_id (str, optional)**: If provided, sets a reference and In-Reply-To headers.
- **is_smtp_ssl (bool, optional)**: If `True`, uses SSL connection to the SMTP server.

#### Outputs
- Returns an empty dictionary after sending the email, signaling completion without detailed status or errors.

#### Potential Workflow
1. Initialize the `SendEmail` class with the necessary inputs.
2. Call the `run()` method to execute sending the email. The email body and subject can be dynamically rendered using template values via `mustache_render`.
3. If `is_smtp_ssl` is true, an SSL connection is used. Otherwise, a standard SMTP connection is established.

### 3. `typed.py`

#### Description
Defines the input and output data structures using Python's `TypedDict`, serving to ensure type safety and clarity when using the `SendEmail` class.

#### Inputs
- **__SendEmailRequiredInputs**: Enforces required email configuration parameters.
- **SendEmailInputs**: Extends the required inputs to include optional configuration options for email specifics and server settings.

#### Outputs
- **SendEmailOutputs**: Currently an empty definition but provides a framework for potential future output enhancements.

## Usage

The `SendEmail` module enables seamless sending of emails with customizable templates and server configurations. It is primarily used in automated workflows to send status updates, alerts, or any predefined communications that leverage email.

### Steps to Use
1. Define the required input parameters including sender/recipient emails, SMTP server credentials.
2. Optionally, determine the email's dynamic content via templates by providing `email_template_value`.
3. Invoke the `run()` method to execute the email delivery.

This module is valuable in applications needing robust and flexible email notifications as part of their operational procedures.
