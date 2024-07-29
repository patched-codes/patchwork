from typing_extensions import Annotated, Optional

from patchwork.common.utils.step_typing import StepTypeConfig


class CreatePRCommentInputs(TypedDict):
    pr_url: str
    pr_comment: str
    noisy_comments: Optional[Annotated[bool, StepTypeConfig(is_config=True)]] = None
    scm_url: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    gitlab_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    github_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None


class CreatePRCommentOutputs(TypedDict):
    pr_url: str
