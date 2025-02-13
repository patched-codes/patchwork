from typing_extensions import Any, TypedDict


class __SendEmailRequiredInputs(TypedDict):
    sender_email: str
    recipient_email: str
    sender_email_password: str


class SendEmailInputs(__SendEmailRequiredInputs, total=False):
    email_template_value: dict[str, Any]
    subject: str
    body: str
    smtp_host: str
    smtp_port: int
    reply_message_id: str


class SendEmailOutputs(TypedDict):
    pass
