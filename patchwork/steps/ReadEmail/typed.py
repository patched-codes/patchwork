from typing_extensions import Annotated, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __ReadEmailRequiredInputs(TypedDict):
    eml_file_path: Annotated[str, StepTypeConfig(is_path=True)]


class ReadEmailInputs(__ReadEmailRequiredInputs, total=False):
    base_path: Annotated[str, StepTypeConfig(is_path=True)]


class Attachment(TypedDict):
    path: str


class ReadEmailOutputs(TypedDict):
    subject: str
    datetime: str
    from_: str  # this is actually from instead of from_
    body: str
    message_id: str
    attachments: List[Attachment]
