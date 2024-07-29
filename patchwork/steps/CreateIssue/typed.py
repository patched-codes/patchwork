from pydantic import BaseModel
from typing_extensions import Annotated, Optional

from patchwork.common.utils.step_typing import StepTypeConfig


class CreateIssueInputs(BaseModel):
    issue_text: str
    issue_title: Annotated[str, StepTypeConfig(is_config=True)]
    scm_url: Annotated[str, StepTypeConfig(is_config=True)]
    gitlab_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    github_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None


class CreateIssueOutputs(BaseModel):
    issue_url: str
