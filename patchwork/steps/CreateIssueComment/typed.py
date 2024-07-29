from typing_extensions import Annotated, Optional

from patchwork.common.utils.step_typing import StepTypeConfig


class CreateIssueCommentInputs(TypedDict):
    issue_text: str
    issue_url: str
    scm_url: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    gitlab_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    github_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None


class CreateIssueCommentOutputs(TypedDict):
    issue_comment_url: str
