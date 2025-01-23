from typing_extensions import Annotated, List, TypedDict

from patchwork.common.client.scm import PullRequestComment
from patchwork.common.utils.step_typing import StepTypeConfig


class __ReadPRDiffsRequiredInputs(TypedDict):
    pr_url: str


class ReadPRDiffsInputs(__ReadPRDiffsRequiredInputs, total=False):
    scm_url: Annotated[str, StepTypeConfig(is_config=True)]
    gitlab_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["github_api_key", "azuredevops_api_key"])]
    github_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["gitlab_api_key", "azuredevops_api_key"])]
    azuredevops_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["gitlab_api_key", "github_api_key"])]


class ReadPRDiffsOutputs(TypedDict):
    title: str
    body: str
    comments: List[PullRequestComment]
    diffs: List["Diff"]


class Diff(TypedDict):
    path: str
    diff: str
