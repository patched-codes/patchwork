from typing_extensions import Annotated, Dict, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __ExtractCodeRequiredInputs(TypedDict):
    sarif_values: Dict


class ExtractCodeInputs(__ExtractCodeRequiredInputs, total=False):
    context_size: Annotated[int, StepTypeConfig(is_config=True)]
    vulnerability_limit: Annotated[int, StepTypeConfig(is_config=True)]
    severity: Annotated[str, StepTypeConfig(is_config=True)]


class ExtractCodeOutputs(TypedDict):
    files_to_patch: List["ExtractedCode"]


class ExtractedCode(TypedDict):
    uri: str
    startLine: int
    endLine: int
    affectedCode: str
    messageText: str
