from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __CreatePRCommentRequiredInputs(TypedDict):
    pr_url: str
    pr_comment: str


class CreatePRCommentInputs(__CreatePRCommentRequiredInputs, total=False):
    noisy_comments: Annotated[bool, StepTypeConfig(is_config=True)]
    scm_url: Annotated[str, StepTypeConfig(is_config=True)]
    gitlab_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["github_api_key", "azuredevops_api_key"])]
    github_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["gitlab_api_key", "azuredevops_api_key"])]
    azuredevops_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["gitlab_api_key", "github_api_key"])]


class CreatePRCommentOutputs(TypedDict):
    pr_url: str
