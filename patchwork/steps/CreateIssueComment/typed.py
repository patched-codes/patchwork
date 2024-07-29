from typing_extensions import Annotated, Optional, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig

class __CreateIssueCommentRequiredInputs(TypedDict):
    issue_text: str
    issue_url: str
class CreateIssueCommentInputs(__CreateIssueCommentRequiredInputs, total=False):
    scm_url: Annotated[str, StepTypeConfig(is_config=True)]
    gitlab_api_key: Annotated[str, StepTypeConfig(is_config=True)]
    github_api_key: Annotated[str, StepTypeConfig(is_config=True)]


class CreateIssueCommentOutputs(TypedDict):
    issue_comment_url: str
