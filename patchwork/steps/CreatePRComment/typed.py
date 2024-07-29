from typing_extensions import Annotated, Optional, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig

class __CreatePRCommentRequiredInputs(TypedDict):
    pr_url: str
    pr_comment: str

class CreatePRCommentInputs(__CreatePRCommentRequiredInputs, total=False):
    noisy_comments: Annotated[bool, StepTypeConfig(is_config=True)]
    scm_url: Annotated[str, StepTypeConfig(is_config=True)]
    gitlab_api_key: Annotated[str, StepTypeConfig(is_config=True)]
    github_api_key: Annotated[str, StepTypeConfig(is_config=True)]


class CreatePRCommentOutputs(TypedDict):
    pr_url: str
