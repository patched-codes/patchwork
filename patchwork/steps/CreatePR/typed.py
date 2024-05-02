from typing_extensions import NotRequired, TypedDict


class CreatePRInputs(TypedDict):
    target_branch: str
    base_branch: NotRequired[str]
    pr_title: NotRequired[str]
    pr_body: NotRequired[str]
    force_pr_creation: NotRequired[bool]
    disable_pr: NotRequired[bool]
    scm_url: NotRequired[str]
    gitlab_api_key: NotRequired[str]
    github_api_key: NotRequired[str]


class CreatePROutputs(TypedDict):
    pr_url: str
