from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.types import IS_CONFIG
from patchwork.steps.PreparePR.typed import ModifiedCodeFile


class __PRInputsRequired(TypedDict):
    # CommitChangesInputs & PreparePRInputs
    modified_code_files: list["ModifiedCodeFile"]


class PRInputs(__PRInputsRequired, total=False):
    # CommitChangesInputs
    disable_branch: Annotated[bool, IS_CONFIG]
    force_branch_creation: Annotated[bool, IS_CONFIG]
    branch_prefix: Annotated[str, IS_CONFIG]
    branch_suffix: Annotated[str, IS_CONFIG]
    # PreparePRInputs
    pr_header: Annotated[str, IS_CONFIG]
    # CreatePRInputs
    pr_title: Annotated[str, IS_CONFIG]
    force_pr_creation: Annotated[bool, IS_CONFIG]
    disable_pr: Annotated[bool, IS_CONFIG]
    scm_url: Annotated[str, IS_CONFIG]
    gitlab_api_key: Annotated[str, IS_CONFIG]
    github_api_key: Annotated[str, IS_CONFIG]


class PROutputs(TypedDict):
    # CommitChangesOutputs
    base_branch: str
    target_branch: str
    # PreparePROutputs
    pr_body: str
    # CreatePROutputs
    pr_url: str
