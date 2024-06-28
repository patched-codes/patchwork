from __future__ import annotations

from typing_extensions import NotRequired, TypedDict


class ReadPRDiffsInputs(TypedDict):
    pr_url: str
    scm_url: NotRequired[str]
    gitlab_api_key: NotRequired[str]
    github_api_key: NotRequired[str]


class ReadPRDiffsOutputs(TypedDict):
    prompt_values: list["Diff"]


class Diff(TypedDict):
    path: str
    diff: str
