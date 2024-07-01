from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class CallLLMInputs(TypedDict, total=False):
    prompt_file: Annotated[str, IS_CONFIG]
    prompts: list[dict]
    model: Annotated[str, IS_CONFIG]
    allow_truncated: Annotated[bool, IS_CONFIG]
    model_args: Annotated[str, IS_CONFIG]
    client_args: Annotated[str, IS_CONFIG]
    openai_api_key: Annotated[str, IS_CONFIG]
    patched_api_key: Annotated[str, IS_CONFIG]
    google_api_key: Annotated[str, IS_CONFIG]


class CallLLMOutputs(TypedDict):
    openai_responses: list[str]
