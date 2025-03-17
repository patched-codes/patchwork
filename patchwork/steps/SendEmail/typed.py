from typing_extensions import Any, TypedDict, Annotated

from patchwork.common.utils.step_typing import StepTypeConfig


class __SendEmailRequiredInputs(TypedDict):
    sender_email: str
    recipient_email: str
    smtp_username: str
    smtp_password: str


class SendEmailInputs(__SendEmailRequiredInputs, total=False):
    email_template_value: dict[str, Any]
    subject: str
    body: str
    smtp_host: str
    smtp_port: int
    reply_message_id: str
    is_smtp_ssl: str
    reply_eml_file_path: Annotated[str, StepTypeConfig(is_path=True)]


class SendEmailOutputs(TypedDict):
    pass
