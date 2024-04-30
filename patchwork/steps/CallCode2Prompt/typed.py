from pathlib import Path

from typing_extensions import NotRequired, TypedDict


class CallCode2PromptInputs(TypedDict):
    folder_path: str
    filter: NotRequired[str]
    suppress_comments: NotRequired[bool]


class CallCode2PromptOutputs(TypedDict):
    prompt_value_file: Path
    code_file: Path
