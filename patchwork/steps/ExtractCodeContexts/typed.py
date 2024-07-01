from __future__ import annotations
from typing_extensions import Iterable, NotRequired, TypedDict, Annotated

from patchwork.common.utils.types import IS_CONFIG


class ExtractCodeContextsInputs(TypedDict, total=False):
    base_path: Annotated[str, IS_CONFIG]
    context_grouping: Annotated[str, IS_CONFIG]


class ExtractCodeContextsOutputs(TypedDict):
    files_to_patch: list["ExtractedCode"]


class ExtractedCode(TypedDict):
    uri: str
    startLine: int
    endLine: int
    affectedCode: str
