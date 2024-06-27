from __future__ import annotations

from typing_extensions import Iterable, NotRequired, TypedDict


class CallLLMInputs(TypedDict):
    prompt_file: NotRequired[str]
    prompts: NotRequired[Iterable[dict]]
    model: NotRequired[str]
    allow_truncated: NotRequired[bool]
    model_args: NotRequired[str]
    client_args: NotRequired[str]
    openai_api_key: NotRequired[str]
    patched_api_key: NotRequired[str]
    google_api_key: NotRequired[str]


class CallLLMOutputs(TypedDict):
    openai_responses: list[str]
