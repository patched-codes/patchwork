from typing_extensions import Annotated, Any, Dict, List, Optional, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig

class __LLMInputsRequired(TypedDict):
    # PreparePromptInputs
    prompt_template_file: Annotated[str, StepTypeConfig(is_config=True)]
    prompt_id: Annotated[str, StepTypeConfig(is_config=True)]

class LLMInputs(__LLMInputsRequired, total=False):
    prompt_value_file: str
    prompt_values: List[Dict[str, Any]]
    # CallLLMInputs
    max_llm_calls: Annotated[int, IS_CONFIG]
    prompt_file: Annotated[str, StepTypeConfig(is_config=True)]
    model: Annotated[str, StepTypeConfig(is_config=True)]
    allow_truncated: Annotated[bool, StepTypeConfig(is_config=True)]
    model_args: Annotated[str, StepTypeConfig(is_config=True)]
    client_args: Annotated[str, StepTypeConfig(is_config=True)]
    openai_api_key: Annotated[str, StepTypeConfig(is_config=True)]
    patched_api_key: Annotated[str, StepTypeConfig(is_config=True)]
    google_api_key: Annotated[str, StepTypeConfig(is_config=True)]
    # ExtractModelResponseInputs
    response_partitions: Annotated[Dict[str, List[str]], StepTypeConfig(is_config=True)]


class LLMOutputs(TypedDict):
    # PreparePromptOutputs
    prompts: List[Dict]
    # CallLLMOutputs
    openai_responses: List[str]
    # ExtractModelResponseOutputs
    extracted_responses: List[Dict[str, str]]
