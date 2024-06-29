from __future__ import annotations

from typing_extensions import Any, Iterable, NotRequired, TypedDict


class LLMInputs(TypedDict):
    # PreparePromptInputs
    prompt_template_file: str
    prompt_id: str
    prompt_value_file: NotRequired[str]
    prompt_values: NotRequired[Iterable[dict[str, Any]]]
    # CallLLMInputs
    prompt_file: NotRequired[str]
    prompts: NotRequired[Iterable[dict]]
    model: NotRequired[str]
    allow_truncated: NotRequired[bool]
    model_args: NotRequired[str]
    client_args: NotRequired[str]
    openai_api_key: NotRequired[str]
    patched_api_key: NotRequired[str]
    google_api_key: NotRequired[str]
    # ExtractModelResponseInputs
    openai_responses: Iterable[str]
    response_partitions: NotRequired[dict[str, list[str]]]


class LLMOutputs(TypedDict):
    # PreparePromptOutputs
    prompts: Iterable[dict]
    # CallLLMOutputs
    openai_responses: list[str]
    # ExtractModelResponseOutputs
    extracted_responses: list[dict[str, str]]
