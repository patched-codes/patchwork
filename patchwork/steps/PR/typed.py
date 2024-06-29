from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from patchwork.steps.PreparePR.typed import ModifiedCodeFile


class PRInputs(TypedDict):
    # CommitChangesInputs
    modified_code_files: list[str]
    disable_branch: NotRequired[bool]
    force_branch_creation: NotRequired[bool]
    branch_prefix: NotRequired[str]
    branch_suffix: NotRequired[str]
    # PreparePRInputs
    modified_code_files: list["ModifiedCodeFile"]
    pr_header: NotRequired[str]
    # CreatePRInputs
    pr_title: NotRequired[str]
    force_pr_creation: NotRequired[bool]
    disable_pr: NotRequired[bool]
    scm_url: NotRequired[str]
    gitlab_api_key: NotRequired[str]
    github_api_key: NotRequired[str]


class PROutputs(TypedDict):
    # CommitChangesOutputs
    base_branch: str
    target_branch: str
    # PreparePROutputs
    pr_body: str
    # CreatePROutputs
    pr_url: str
