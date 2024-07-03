from __future__ import annotations

from typing_extensions import Annotated, Any, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class __SimplifiedLLMInputsRequired(TypedDict):
    # PreparePromptInputs
    prompt_user: Annotated[str, IS_CONFIG]
    prompt_values: list[dict[str, Any]]


class SimplifiedLLMInputs(__SimplifiedLLMInputsRequired, total=False):
    prompt_system: Annotated[str, IS_CONFIG]
    # CallLLMInputs
    model: Annotated[str, IS_CONFIG]
    openai_api_key: Annotated[str, IS_CONFIG]
    patched_api_key: Annotated[str, IS_CONFIG]
    google_api_key: Annotated[str, IS_CONFIG]
    json: Annotated[bool, IS_CONFIG]
    # ExtractModelResponseInputs
    response_partitions: Annotated[dict[str, list[str]], IS_CONFIG]


class SimplifiedLLMOutputs(TypedDict):
    # PreparePromptOutputs
    prompts: list[dict]
    # CallLLMOutputs
    openai_responses: list[str]
    # ExtractModelResponseOutputs
    extracted_responses: list[dict[str, str]]
