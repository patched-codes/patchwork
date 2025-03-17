from __future__ import annotations

import smtplib
from email.message import EmailMessage

from patchwork.common.utils.utils import mustache_render
from patchwork.step import Step
from patchwork.steps.SendEmail.typed import SendEmailInputs, SendEmailOutputs


class SendEmail(Step, input_class=SendEmailInputs, output_class=SendEmailOutputs):
    def __init__(self, inputs):
        super().__init__(inputs)
        self.email_template_value = inputs.get("email_template_value", dict())
        self.subject = inputs.get("subject", "Patchwork Execution Email")
        self.body = inputs.get("body", "Patchwork Execution Email")
        self.sender_email = inputs["sender_email"]
        self.recipient_email = inputs["recipient_email"]
        self.smtp_host = inputs.get("smtp_host", "smtp.gmail.com")
        self.smtp_username = inputs["smtp_username"]
        self.smtp_password = inputs["smtp_password"]
        self.smtp_port = int(inputs.get("smtp_port", 25))
        self.reply_message_id = inputs.get("reply_message_id")
        self.is_ssl = bool(inputs.get("is_smtp_ssl", False))

    def run(self) -> dict:
        msg = EmailMessage()
        msg.set_content(mustache_render(self.body, self.email_template_value))
        msg["Subject"] = mustache_render(self.subject, self.email_template_value)
        msg["From"] = self.sender_email
        msg["To"] = self.recipient_email
        if self.reply_message_id is not None:
            msg.add_header("Reference", self.reply_message_id)
            msg.add_header("In-Reply-To", self.reply_message_id)

        smtp_clazz = smtplib.SMTP
        if self.is_ssl:
            smtp_clazz = smtplib.SMTP_SSL

        with smtp_clazz(host=self.smtp_host, port=self.smtp_port) as mailserver:
            mailserver.login(self.smtp_username, self.smtp_password)
            mailserver.send_message(msg)
        return dict()
