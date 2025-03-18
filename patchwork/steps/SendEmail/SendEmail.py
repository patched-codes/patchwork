from __future__ import annotations

import smtplib
import textwrap
from datetime import datetime
from email.message import EmailMessage

from patchwork.common.utils.utils import mustache_render
from patchwork.step import Step
from patchwork.steps.ReadEmail.ReadEmail import ReadEmail
from patchwork.steps.SendEmail.typed import SendEmailInputs, SendEmailOutputs


class SendEmail(Step, input_class=SendEmailInputs, output_class=SendEmailOutputs):
    def __init__(self, inputs):
        super().__init__(inputs)
        self.smtp_host = inputs.get("smtp_host", "smtp.gmail.com")
        self.smtp_username = inputs["smtp_username"]
        self.smtp_password = inputs["smtp_password"]
        self.smtp_port = int(inputs.get("smtp_port", 25))
        self.is_ssl = bool(inputs.get("is_smtp_ssl", False))

        self.sender_email = inputs["sender_email"]
        self.recipient_email = inputs["recipient_email"]
        email_template_value = inputs.get("email_template_value", dict())
        self.subject = mustache_render(inputs.get("subject", "Patchwork Execution Email"), email_template_value)
        self.body = mustache_render(inputs.get("body", "Patchwork Execution Email"), email_template_value)
        self.reply_message_id = inputs.get("reply_message_id")
        self.__handle_eml_file(inputs.get("reply_eml_file_path"))

    def __handle_eml_file(self, eml_file: str):
        if eml_file is None:
            return

        original_email_data = ReadEmail(dict(eml_file_path=eml_file)).run()
        timestamp: datetime = original_email_data.get("datetime")
        date_str = timestamp.date().strftime('%-d %b %Y')
        time_str = timestamp.time().strftime('%H:%M')
        from_ = original_email_data.get("from")
        self.subject = original_email_data.get("subject")
        self.body += f"\n\nOn {date_str} at {time_str}, {from_} wrote:\n\n" + textwrap.indent(original_email_data.get("body"), "> ")
        self.reply_message_id = original_email_data.get("message_id")

    def run(self) -> dict:
        msg = self.__create_email_message()

        smtp_clazz = smtplib.SMTP
        if self.is_ssl:
            smtp_clazz = smtplib.SMTP_SSL

        with smtp_clazz(host=self.smtp_host, port=self.smtp_port) as mailserver:
            mailserver.login(self.smtp_username, self.smtp_password)
            mailserver.send_message(msg)
        return dict()

    def __create_email_message(self):
        msg = EmailMessage()
        msg.set_content(self.body)
        msg["Subject"] = self.subject
        msg["From"] = self.sender_email
        msg["To"] = self.recipient_email
        if self.reply_message_id is not None:
            msg.add_header("References", self.reply_message_id)
            msg.add_header("In-Reply-To", self.reply_message_id)
        return msg
