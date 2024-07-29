from typing_extensions import Annotated, List, Optional, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class ExtractCodeContextsInputs(TypedDict):
    base_path: Optional[Annotated[str, StepTypeConfig(is_path=True)]] = None
    context_grouping: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None


class ExtractCodeContextsOutputs(TypedDict):
    files_to_patch: List["ExtractedCode"]


class ExtractedCode(TypedDict):
    uri: str
    startLine: int
    endLine: int
    affectedCode: str
