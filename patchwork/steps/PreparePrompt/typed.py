from __future__ import annotations

from typing_extensions import Annotated, Any, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class __PreparePromptRequiredInputs(TypedDict):
    prompt_template_file: Annotated[str, IS_CONFIG]
    prompt_id: Annotated[str, IS_CONFIG]


class PreparePromptInputs(__PreparePromptRequiredInputs, total=False):
    prompt_value_file: Annotated[str, IS_CONFIG]
    prompt_values: list[dict[str, Any]]


class PreparePromptOutputs(TypedDict):
    prompts: list[dict]
