from typing_extensions import Annotated, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __ReadIssuesRequiredInputs(TypedDict):
    issue_url: str


class ReadIssuesInputs(__ReadIssuesRequiredInputs, total=False):
    scm_url: Annotated[str, StepTypeConfig(is_config=True)]
    gitlab_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["github_api_key"])]
    github_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["gitlab_api_key"])]


class ReadIssuesOutputs(TypedDict):
    issue_title: str
    issue_body: str
    issue_comments: List[str]
    issue_description: str
