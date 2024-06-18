from __future__ import annotations
from typing_extensions import NotRequired, TypedDict


class CommitChangesInputs(TypedDict):
    modified_code_files: list[str]
    disable_branch: NotRequired[bool]
    force_branch_creation: NotRequired[bool]
    branch_prefix: NotRequired[str]
    branch_suffix: NotRequired[str]


class CommitChangesOutputs(TypedDict):
    base_branch: str
    target_branch: str
