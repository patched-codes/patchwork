from typing_extensions import Annotated, Iterable, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class __CallCode2PromptRequiredInputs(TypedDict):
    folder_path: Annotated[str, IS_CONFIG]


class CallCode2PromptInputs(__CallCode2PromptRequiredInputs, total=False):
    filter: Annotated[str, IS_CONFIG]
    suppress_comments: Annotated[bool, IS_CONFIG]


class CallCode2PromptOutputs(TypedDict):
    files_to_patch: Iterable[dict]
