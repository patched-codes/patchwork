from typing_extensions import Annotated, Dict, List, Optional, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class ExtractCodeInputs(TypedDict):
    sarif_values: Dict
    context_size: Optional[Annotated[int, StepTypeConfig(is_config=True)]] = None
    vulnerability_limit: Optional[Annotated[int, StepTypeConfig(is_config=True)]] = None
    severity: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None


class ExtractCodeOutputs(TypedDict):
    files_to_patch: List["ExtractedCode"]


class ExtractedCode(TypedDict):
    uri: str
    startLine: int
    endLine: int
    affectedCode: str
    messageText: str
