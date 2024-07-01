from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class __ReadPRDiffsRequiredInputs(TypedDict):
    pr_url: Annotated[str, IS_CONFIG]


class ReadPRDiffsInputs(__ReadPRDiffsRequiredInputs, total=False):
    scm_url: Annotated[str, IS_CONFIG]
    gitlab_api_key: Annotated[str, IS_CONFIG]
    github_api_key: Annotated[str, IS_CONFIG]


class ReadPRDiffsOutputs(TypedDict):
    prompt_values: list["Diff"]


class Diff(TypedDict):
    path: str
    diff: str
