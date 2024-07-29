from typing_extensions import Annotated, List, Optional

from patchwork.common.utils.step_typing import StepTypeConfig
from patchwork.steps.PreparePR.typed import ModifiedCodeFile


class PRInputs(TypedDict):
    # CommitChangesInputs & PreparePRInputs
    modified_code_files: List["ModifiedCodeFile"]
    # CommitChangesInputs
    disable_branch: Optional[Annotated[bool, StepTypeConfig(is_config=True)]] = None
    force_branch_creation: Optional[Annotated[bool, StepTypeConfig(is_config=True)]] = None
    branch_prefix: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    branch_suffix: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    # PreparePRInputs
    pr_header: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    # CreatePRInputs
    pr_title: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    force_pr_creation: Optional[Annotated[bool, StepTypeConfig(is_config=True)]] = None
    disable_pr: Optional[Annotated[bool, StepTypeConfig(is_config=True)]] = None
    scm_url: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    gitlab_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    github_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None


class PROutputs(TypedDict):
    # CommitChangesOutputs
    base_branch: str
    target_branch: str
    # PreparePROutputs
    pr_body: str
    # CreatePROutputs
    pr_url: str
