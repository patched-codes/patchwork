from __future__ import annotations

from typing_extensions import TypedDict


class ModifyCodeInputs(TypedDict):
    files_to_patch: list[dict]
    extracted_responses: list[dict[str, str]]


class ModifyCodeOutputs(TypedDict):
    modified_code_files: list["ModifiedCodeFile"]


class ModifiedCodeFile(TypedDict, total=False):
    path: str
    start_line: int
    end_line: int
