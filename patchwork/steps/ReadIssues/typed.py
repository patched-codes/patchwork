from __future__ import annotations
from typing_extensions import NotRequired, TypedDict


class ReadIssuesInputs(TypedDict):
    issue_url: str
    scm_url: NotRequired[str]
    gitlab_api_key: NotRequired[str]
    github_api_key: NotRequired[str]


class ReadIssuesOutputs(TypedDict):
    issue_text: list[str]
