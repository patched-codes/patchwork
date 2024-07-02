from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class ExtractCodeMethodForCommentContextsInputs(TypedDict):
    base_path: Annotated[str, IS_CONFIG]
    context_grouping: Annotated[str, IS_CONFIG]


class ExtractCodeMethodForCommentContextsOutputs(TypedDict):
    files_to_patch: list["ExtractedCode"]


class ExtractedCode(TypedDict):
    uri: str
    startLine: int
    endLine: int
    affectedCode: str
