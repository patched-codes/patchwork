from typing_extensions import Annotated, Dict, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class ModifiedCodeFile(TypedDict):
    path: str
    commit_message: str
    patch_message: str


class PRInputs(TypedDict, total=False):
    # CommitChangesInputs & PreparePRInputs
    modified_code_files: List["ModifiedCodeFile"]
    # modified_code_files alternative
    modified_files: List[Dict]
    path_key: str
    comment_title_key: str
    comment_message_key: str
    # CommitChangesInputs
    disable_branch: Annotated[bool, StepTypeConfig(is_config=True)]
    force_branch_creation: Annotated[bool, StepTypeConfig(is_config=True)]
    branch_prefix: Annotated[str, StepTypeConfig(is_config=True)]
    branch_suffix: Annotated[str, StepTypeConfig(is_config=True)]
    # PreparePRInputs
    pr_header: Annotated[str, StepTypeConfig(is_config=True)]
    # CreatePRInputs
    pr_title: Annotated[str, StepTypeConfig(is_config=True)]
    force_pr_creation: Annotated[bool, StepTypeConfig(is_config=True)]
    disable_pr: Annotated[bool, StepTypeConfig(is_config=True)]
    scm_url: Annotated[str, StepTypeConfig(is_config=True)]
    gitlab_api_key: Annotated[str, StepTypeConfig(is_config=True)]
    github_api_key: Annotated[str, StepTypeConfig(is_config=True)]
    issue_url: Annotated[str, StepTypeConfig(is_config=True)]


class PROutputs(TypedDict):
    # CommitChangesOutputs
    base_branch: str
    target_branch: str
    # PreparePROutputs
    pr_body: str
    # CreatePROutputs
    pr_url: str
