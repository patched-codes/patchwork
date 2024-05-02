from typing import Any

from typing_extensions import Iterable, NotRequired, TypedDict


class PreparePromptInputs(TypedDict):
    prompt_template_file: str
    prompt_id: str
    prompt_value_file: NotRequired[str]
    prompt_values: NotRequired[Iterable[dict[str, Any]]]


class PreparePromptOutputs(TypedDict):
    prompt_file: str
