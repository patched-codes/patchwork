from typing_extensions import NotRequired, TypedDict


class CreatePRCommentInputs(TypedDict):
    pr_url: str
    pr_comments: str
    noisy_comments: NotRequired[bool]
    scm_url: NotRequired[str]
    gitlab_api_key: NotRequired[str]
    github_api_key: NotRequired[str]


class CreatePRCommentOutputs(TypedDict):
    pass
