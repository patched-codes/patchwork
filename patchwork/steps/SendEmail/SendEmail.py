from __future__ import annotations

import smtplib
from email.mime.text import MIMEText

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
        self.password = inputs["sender_email_password"]
        self.smtp_host = inputs.get("smtp_host", "smtp.gmail.com")
        self.smtp_port = int(inputs.get("smtp_port", 465))
        self.reply_message_id = inputs.get("reply_message_id")

    def run(self) -> dict:
        msg = MIMEText(mustache_render(self.body, self.email_template_value))
        msg["Subject"] = mustache_render(self.subject, self.email_template_value)
        msg["From"] = self.sender_email
        msg["To"] = self.recipient_email
        if self.reply_message_id is not None:
            msg.add_header('Reference', self.reply_message_id)
            msg.add_header('In-Reply-To', self.reply_message_id)

        # TODO: support smtp without ssl
        with smtplib.SMTP_SSL(self.smtp_host, self.smtp_port) as smtp_server:
            smtp_server.login(self.sender_email, self.password)
            smtp_server.sendmail(self.sender_email, self.recipient_email, msg.as_string())

        return dict()
