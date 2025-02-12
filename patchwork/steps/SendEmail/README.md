# SendEmail Module Documentation

The `SendEmail` module is designed to provide an automated way to send emails using SMTP with SSL encryption. It employs mustache rendering for dynamic content in email bodies and subjects, integrating smoothly with the larger system it is part of.

## Inputs

The `SendEmail` class accepts a dictionary of inputs that configure the sending of an email. These inputs include:

- **sender_email** (str): Email address of the sender.
- **recipient_email** (str): Email address of the recipient.
- **sender_email_password** (str): Password of the sender's email account to authenticate the SMTP session.
- **email_template_value** (dict, optional): A dictionary used to render dynamic content in the email template.
- **subject** (str, optional): Subject of the email. Default is "Patchwork Execution Email".
- **body** (str, optional): Body content of the email. Default is "Patchwork Execution Email".
- **smtp_host** (str, optional): The SMTP server to use for sending emails. Default is "smtp.gmail.com".
- **smtp_port** (int, optional): The port used by the SMTP server. Default is 465.

These inputs are encapsulated in the `SendEmailInputs` TypedDict structure.

## Outputs

The `SendEmail` class currently returns an empty dictionary after the email is sent. Future enhancements could include sending receipt confirmations or error messages. The output structure is defined by the `SendEmailOutputs` TypedDict, which is currently empty.

## Usage

To use the `SendEmail` class, instantiate it with the required inputs as mentioned above, and then call the `run` method to execute the email sending process.

### Example

```python
email_inputs = {
    "sender_email": "example_sender@gmail.com",
    "recipient_email": "example_recipient@gmail.com",
    "sender_email_password": "securepassword",
    "subject": "Test Email",
    "body": "This is a test email.",
    "smtp_host": "smtp.example.com",
    "smtp_port": 465
}

email_step = SendEmail(inputs=email_inputs)
email_step.run()
```

### Note

Ensure that the SMTP credentials are secured and handled safely, as mistakes could compromise email accounts. Also, ensure that your SMTP provider allows for SSL connections on the specified port.

## Dependencies

- `smtplib`: For handling SMTP connections.
- `email.mime.text`: For composing the MIME email message.
- `patchwork.common.utils.utils.mustache_render`: For rendering dynamic templates in email content.
- `patchwork.step.Step`: The base class for steps, integrating this email step within a larger workflow.

This module is essential for applications requiring automated email notifications or communications as part of their processes.
