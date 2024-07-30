from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.typing import IS_PATH, IS_CONFIG


class ExtractCodeMethodForCommentContextsInputs(TypedDict, total=False):
    base_path: Annotated[str, IS_PATH]
    missing_comment_limit: Annotated[int, IS_CONFIG]


class ExtractCodeMethodForCommentContextsOutputs(TypedDict):
    files_to_patch: list["ExtractedCode"]


class ExtractedCode(TypedDict):
    uri: str
    startLine: int
    endLine: int
    affectedCode: str
