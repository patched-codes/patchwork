from typing_extensions import Annotated, Any, Dict, List, Optional, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig

class __SimplifiedLLMInputsRequired(TypedDict):
    # PreparePromptInputs
    prompt_user: Annotated[str, StepTypeConfig(is_config=True)]
    prompt_values: List[Dict[str, Any]]

class SimplifiedLLMInputs(__SimplifiedLLMInputsRequired, total=False):
    prompt_system: Annotated[str, StepTypeConfig(is_config=True)]
    # CallLLMInputs
    max_llm_calls: Annotated[int, StepTypeConfig(is_config=True)]
    model: Annotated[str, StepTypeConfig(is_config=True)]
    openai_api_key: Annotated[str, StepTypeConfig(is_config=True)]
    patched_api_key: Annotated[str, StepTypeConfig(is_config=True)]
    google_api_key: Annotated[str, StepTypeConfig(is_config=True)]
    json: Annotated[bool, StepTypeConfig(is_config=True)]
    # ExtractModelResponseInputs
    response_partitions: Annotated[Dict[str, List[str]], StepTypeConfig(is_config=True)]


class SimplifiedLLMOutputs(TypedDict):
    # PreparePromptOutputs
    prompts: List[Dict]
    # CallLLMOutputs
    openai_responses: List[str]
    # ExtractModelResponseOutputs
    extracted_responses: List[Dict[str, str]]
