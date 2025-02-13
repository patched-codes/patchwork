from __future__ import annotations

import base64
import os
import quopri
from datetime import datetime
from pathlib import Path

from eml_parser import EmlParser
from pydantic import BaseModel, Field

from patchwork.step import Step
from patchwork.steps.ReadEmail.typed import ReadEmailInputs, ReadEmailOutputs


class ParsedHeader(BaseModel):
    subject: str
    from_: str = Field(alias="from")
    to: list[str]
    date: datetime


class ParsedBody(BaseModel):
    content: str
    content_type: str


class AttachmentHeader(BaseModel):
    content_disposition: list[str] = Field(alias="content-disposition")
    content_transfer_encoding: list[str] = Field(alias="content-transfer-encoding")
    content_type: list[str] = Field(alias="content-type")


class ParsedAttachment(BaseModel):
    filename: str
    raw: bytes
    content_header: AttachmentHeader


class ParsedEmail(BaseModel):
    header: ParsedHeader
    body: list[ParsedBody]
    attachment: list[ParsedAttachment]


class ReadEmail(Step, input_class=ReadEmailInputs, output_class=ReadEmailOutputs):
    def __init__(self, inputs: dict):
        super().__init__(inputs)
        self.file = inputs["eml_file_path"]
        self.base_path = inputs.get("base_path", os.getcwd())

    def __decode(self, content_transfer_encoding: str, content: bytes) -> bytes:
        if content_transfer_encoding.lower() == "base64":
            return base64.b64decode(content)
        elif content_transfer_encoding.lower() == "quoted‑printable":
            return quopri.decodestring(content)

        return content

    def run(self) -> dict:
        ep = EmlParser(
            include_raw_body=True,
            include_attachment_data=True,
        )

        email_data_dict = ep.decode_email(self.file)
        email_data = ParsedEmail.model_validate(email_data_dict)

        rv = {
            "subject": email_data.header.subject,
            "datetime": email_data.header.date,
            "from": email_data.header.from_,
            "attachments": [],
            "body": "",
        }

        base_path = Path(self.base_path)
        base_path.mkdir(parents=True, exist_ok=True)
        for attachment in email_data.attachment:
            file_path = base_path / attachment.filename
            with file_path.open("wb") as f:
                content = attachment.raw
                for content_transfer_encoding in attachment.content_header.content_transfer_encoding:
                    content = self.__decode(content_transfer_encoding, content)
                f.write(content)
            rv["attachments"].append(dict(path=file_path, content=content.decode()))

        for body in email_data.body:
            rv["body"] += body.content

        return rv
