from typing_extensions import Annotated, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class ExtractCodeMethodForCommentContextsInputs(TypedDict):
    base_path: Annotated[str, StepTypeConfig(is_path=True)]


class ExtractCodeMethodForCommentContextsOutputs(TypedDict):
    files_to_patch: List["ExtractedCode"]


class ExtractedCode(TypedDict):
    uri: str
    startLine: int
    endLine: int
    affectedCode: str
