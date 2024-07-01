from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class __PreparePRRequiredInputs(TypedDict):
    modified_code_files: list["ModifiedCodeFile"]


class PreparePRInputs(__PreparePRRequiredInputs, total=False):
    pr_header: Annotated[str, IS_CONFIG]


class PreparePROutputs(TypedDict):
    pr_body: str


class ModifiedCodeFile(TypedDict, total=False):
    path: str
    start_line: int
    end_line: int
