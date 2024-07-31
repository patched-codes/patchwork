from typing_extensions import Annotated, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class ExtractCodeContextsInputs(TypedDict, total=False):
    base_path: Annotated[str, StepTypeConfig(is_path=True)]
    context_grouping: Annotated[str, StepTypeConfig(is_config=True)]


class ExtractCodeContextsOutputs(TypedDict):
    files_to_patch: List["ExtractedCode"]


class ExtractedCode(TypedDict):
    uri: str
    startLine: int
    endLine: int
    affectedCode: str
