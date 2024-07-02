from __future__ import annotations

from typing_extensions import Annotated, Any, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class __LLMInputsRequired(TypedDict):
    # PreparePromptInputs
    prompt_template_file: Annotated[str, IS_CONFIG]
    prompt_id: Annotated[str, IS_CONFIG]


class LLMInputs(__LLMInputsRequired, total=False):
    prompt_value_file: str
    prompt_values: list[dict[str, Any]]
    # CallLLMInputs
    prompt_file: Annotated[str, IS_CONFIG]
    model: Annotated[str, IS_CONFIG]
    allow_truncated: Annotated[bool, IS_CONFIG]
    model_args: Annotated[str, IS_CONFIG]
    client_args: Annotated[str, IS_CONFIG]
    openai_api_key: Annotated[str, IS_CONFIG]
    patched_api_key: Annotated[str, IS_CONFIG]
    google_api_key: Annotated[str, IS_CONFIG]
    # ExtractModelResponseInputs
    response_partitions: Annotated[dict[str, list[str]], IS_CONFIG]


class LLMOutputs(TypedDict):
    # PreparePromptOutputs
    prompts: list[dict]
    # CallLLMOutputs
    openai_responses: list[str]
    # ExtractModelResponseOutputs
    extracted_responses: list[dict[str, str]]
