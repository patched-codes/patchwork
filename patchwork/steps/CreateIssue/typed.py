from __future__ import annotations

from typing_extensions import NotRequired, TypedDict


class CreateIssueInputs(TypedDict):
    issue_text: list[str]
    issue_title: str
    scm_url: str
    gitlab_api_key: NotRequired[str]
    github_api_key: NotRequired[str]


class CreateIssueOutputs(TypedDict):
    issue_url: str
