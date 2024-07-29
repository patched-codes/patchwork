from typing_extensions import Annotated, Optional, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __CreateIssueRequiredInputs(TypedDict):
    issue_text: str
issue_title: Annotated[str, StepTypeConfig(is_config=True)]
scm_url: Annotated[str, StepTypeConfig(is_config=True)]

class CreateIssueInputs(__CreateIssueRequiredInputs, total=False):
    gitlab_api_key: Annotated[str, StepTypeConfig(is_config=True)]
    github_api_key: Annotated[str, StepTypeConfig(is_config=True)]


class CreateIssueOutputs(TypedDict):
    issue_url: str
