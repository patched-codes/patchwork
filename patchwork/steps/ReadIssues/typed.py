from typing_extensions import Annotated, List, Optional

from patchwork.common.utils.step_typing import StepTypeConfig


class ReadIssuesInputs(TypedDict):
    issue_url: str
    scm_url: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    gitlab_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    github_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None


class ReadIssuesOutputs(TypedDict):
    issue_title: str
    issue_body: str
    issue_comments: List[str]
