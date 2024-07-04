from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from patchwork.common.utils.typing import IS_PATH


class ExtractCodeMethodForCommentContextsInputs(TypedDict):
    base_path: Annotated[str, IS_PATH]


class ExtractCodeMethodForCommentContextsOutputs(TypedDict):
    files_to_patch: list["ExtractedCode"]


class ExtractedCode(TypedDict):
    uri: str
    startLine: int
    endLine: int
    affectedCode: str
