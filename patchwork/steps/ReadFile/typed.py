from typing_extensions import TypedDict, Annotated

from patchwork.common.utils.step_typing import StepTypeConfig


class ReadFileInputs(TypedDict):
    file_path: Annotated[str, StepTypeConfig(is_path=True)]


class ReadFileOutputs(TypedDict):
    file_content: str
