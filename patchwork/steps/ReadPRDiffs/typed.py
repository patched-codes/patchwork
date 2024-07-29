from pydantic import BaseModel
from typing_extensions import Annotated, List, Optional, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class ReadPRDiffsInputs(BaseModel):
    pr_url: str
    scm_url: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    gitlab_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    github_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None


class ReadPRDiffsOutputs(BaseModel):
    prompt_values: List["Diff"]


class Diff(TypedDict):
    path: str
    diff: str
