from __future__ import annotations

from typing_extensions import TypedDict

from patchwork.steps.PreparePR.typed import ModifiedCodeFile


class __PRInputsRequired(TypedDict):
    # CommitChangesInputs & PreparePRInputs
    modified_code_files: list["ModifiedCodeFile"]


class PRInputs(__PRInputsRequired, total=False):
    # CommitChangesInputs
    disable_branch: bool
    force_branch_creation: bool
    branch_prefix: str
    branch_suffix: str
    # PreparePRInputs
    pr_header: str
    # CreatePRInputs
    pr_title: str
    force_pr_creation: bool
    disable_pr: bool
    scm_url: str
    gitlab_api_key: str
    github_api_key: str


class PROutputs(TypedDict):
    # CommitChangesOutputs
    base_branch: str
    target_branch: str
    # PreparePROutputs
    pr_body: str
    # CreatePROutputs
    pr_url: str
