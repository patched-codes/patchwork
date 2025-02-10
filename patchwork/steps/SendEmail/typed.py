from typing_extensions import Annotated, Any, Dict, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


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


class SendEmailOutputs(TypedDict):
    is_slack_message_sent: bool
