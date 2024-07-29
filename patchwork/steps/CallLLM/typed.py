from typing_extensions import Annotated, Dict, List, Optional, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class CallLLMInputs(TypedDict, total=False):
    prompt_file: Annotated[str, StepTypeConfig(is_config=True)]
    prompts: List[Dict]
    model: Annotated[str, StepTypeConfig(is_config=True)]
    allow_truncated: Annotated[bool, StepTypeConfig(is_config=True)]
    model_args: Annotated[str, StepTypeConfig(is_config=True)]
    client_args: Annotated[str, StepTypeConfig(is_config=True)]
    openai_api_key: Annotated[str, StepTypeConfig(is_config=True)]
    patched_api_key: Annotated[str, StepTypeConfig(is_config=True)]
    google_api_key: Annotated[str, StepTypeConfig(is_config=True)]


class CallLLMOutputs(TypedDict):
    openai_responses: List[str]
