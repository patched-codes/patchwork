from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __CallCode2PromptRequiredInputs(TypedDict):
    folder_path: Annotated[str, StepTypeConfig(is_config=True, is_path=True)]


class CallCode2PromptInputs(__CallCode2PromptRequiredInputs, total=False):
    filter: Annotated[str, StepTypeConfig(is_config=True)]
    suppress_comments: Annotated[bool, StepTypeConfig(is_config=True)]
    markdown_file_name: Annotated[str, StepTypeConfig(is_config=True)]
    code2prompt_modes: str


class CallCode2PromptOutputs(TypedDict):
    uri: str
    fullContent: str
