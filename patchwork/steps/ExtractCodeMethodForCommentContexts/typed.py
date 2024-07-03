from __future__ import annotations

from typing_extensions import TypedDict


class ExtractCodeMethodForCommentContextsInputs(TypedDict):
    base_path: str


class ExtractCodeMethodForCommentContextsOutputs(TypedDict):
    files_to_patch: list["ExtractedCode"]


class ExtractedCode(TypedDict):
    uri: str
    startLine: int
    endLine: int
    affectedCode: str
