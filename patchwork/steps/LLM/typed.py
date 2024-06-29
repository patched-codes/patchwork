from __future__ import annotations

from typing_extensions import Any, Iterable, TypedDict


class __LLMInputsRequired(TypedDict):
    # PreparePromptInputs
    prompt_template_file: str
    prompt_id: str


class LLMInputs(__LLMInputsRequired, total=False):
    prompt_value_file: str
    prompt_values: Iterable[dict[str, Any]]
    # CallLLMInputs
    prompt_file: str
    model: str
    allow_truncated: bool
    model_args: str
    client_args: str
    openai_api_key: str
    patched_api_key: str
    google_api_key: str
    # ExtractModelResponseInputs
    response_partitions: dict[str, list[str]]


class LLMOutputs(TypedDict):
    # PreparePromptOutputs
    prompts: Iterable[dict]
    # CallLLMOutputs
    openai_responses: list[str]
    # ExtractModelResponseOutputs
    extracted_responses: list[dict[str, str]]
