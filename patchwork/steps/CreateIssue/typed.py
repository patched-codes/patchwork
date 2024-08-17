from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __CreateIssueRequiredInputs(TypedDict):
    issue_text: str
    issue_title: Annotated[str, StepTypeConfig(is_config=True)]


class CreateIssueInputs(__CreateIssueRequiredInputs, total=False):
    scm_url: Annotated[str, StepTypeConfig(is_config=True)]
    gitlab_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["github_api_key"])]
    github_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["gitlab_api_key"])]


class CreateIssueOutputs(TypedDict):
    issue_url: str
