from pydantic import BaseModel
from typing_extensions import Annotated, Optional, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class CreatePRInputs(BaseModel):
    target_branch: str
    base_branch: Optional[str] = None
    pr_title: Optional[str] = None
    pr_body: Optional[str] = None
    force_pr_creation: Optional[Annotated[bool, StepTypeConfig(is_config=True)]] = None
    disable_pr: Optional[Annotated[bool, StepTypeConfig(is_config=True)]] = None
    scm_url: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    gitlab_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    github_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None


class CreatePROutputs(TypedDict):
    pr_url: str
