from __future__ import annotations

from typing_extensions import Annotated, Any, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class __CommitChangesRequiredInputs(TypedDict):
    modified_code_files: list[dict[str, Any]]


class CommitChangesInputs(__CommitChangesRequiredInputs, total=False):
    disable_branch: Annotated[bool, IS_CONFIG]
    force_branch_creation: Annotated[bool, IS_CONFIG]
    branch_prefix: Annotated[str, IS_CONFIG]
    branch_suffix: Annotated[str, IS_CONFIG]


class CommitChangesOutputs(TypedDict):
    base_branch: str
    target_branch: str
