from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __CreatePRRequiredInputs(TypedDict):
    target_branch: str


class CreatePRInputs(__CreatePRRequiredInputs, total=False):
    base_branch: str
    pr_title: str
    pr_body: str
    force_pr_creation: Annotated[bool, StepTypeConfig(is_config=True)]
    disable_pr: Annotated[bool, StepTypeConfig(is_config=True)]
    scm_url: Annotated[str, StepTypeConfig(is_config=True)]
    gitlab_api_key: Annotated[str, StepTypeConfig(is_config=True)]
    github_api_key: Annotated[str, StepTypeConfig(is_config=True)]
    azuredevops_api_key: Annotated[str, StepTypeConfig(is_config=True)]


class CreatePROutputs(TypedDict):
    pr_url: str
