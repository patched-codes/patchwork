from __future__ import annotations
from typing_extensions import Any, Iterable, NotRequired, TypedDict


class PreparePromptInputs(TypedDict):
    prompt_template_file: str
    prompt_id: str
    prompt_value_file: NotRequired[str]
    prompt_values: NotRequired[Iterable[dict[str, Any]]]


class PreparePromptOutputs(TypedDict):
    prompts: Iterable[dict]
