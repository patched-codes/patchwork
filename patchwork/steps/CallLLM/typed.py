from pathlib import Path

from typing_extensions import NotRequired, TypedDict


class CallLLMInputs(TypedDict):
    prompt_file: Path
    model: str
    allow_truncated: NotRequired[bool]
    model_args: NotRequired[str]
    client_args: NotRequired[str]
    openai_api_key: NotRequired[str]
    patched_api_key: NotRequired[str]
    google_api_key: NotRequired[str]


class CallLLMOutputs(TypedDict):
    new_code: Path
    openai_response: list[str]
