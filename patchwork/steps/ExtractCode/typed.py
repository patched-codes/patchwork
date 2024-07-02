from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class __ExtractCodeRequiredInputs(TypedDict):
    sarif_values: dict


class ExtractCodeInputs(__ExtractCodeRequiredInputs, total=False):
    context_size: Annotated[int, IS_CONFIG]
    vulnerability_limit: Annotated[int, IS_CONFIG]
    severity: Annotated[str, IS_CONFIG]


class ExtractCodeOutputs(TypedDict):
    files_to_patch: list["ExtractedCode"]


class ExtractedCode(TypedDict):
    uri: str
    startLine: int
    endLine: int
    affectedCode: str
    messageText: str
