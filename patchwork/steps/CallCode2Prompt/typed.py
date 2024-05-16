from typing_extensions import Iterable, NotRequired, TypedDict


class CallCode2PromptInputs(TypedDict):
    folder_path: str
    filter: NotRequired[str]
    suppress_comments: NotRequired[bool]


class CallCode2PromptOutputs(TypedDict):
    prompt_values: Iterable[dict]
    files_to_patch: Iterable[dict]
