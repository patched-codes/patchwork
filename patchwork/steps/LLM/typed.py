from typing_extensions import Annotated, Any, Dict, List, Optional

from patchwork.common.utils.step_typing import StepTypeConfig


class LLMInputs(TypedDict):
    # PreparePromptInputs
    prompt_template_file: Annotated[str, StepTypeConfig(is_config=True)]
    prompt_id: Annotated[str, StepTypeConfig(is_config=True)]
    prompt_value_file: Optional[str] = None
    prompt_values: Optional[List[Dict[str, Any]]] = None
    # CallLLMInputs
    prompt_file: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    model: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    allow_truncated: Optional[Annotated[bool, StepTypeConfig(is_config=True)]] = None
    model_args: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    client_args: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    openai_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    patched_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    google_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    # ExtractModelResponseInputs
    response_partitions: Optional[Annotated[Dict[str, List[str]], StepTypeConfig(is_config=True)]] = None


class LLMOutputs(TypedDict):
    # PreparePromptOutputs
    prompts: List[Dict]
    # CallLLMOutputs
    openai_responses: List[str]
    # ExtractModelResponseOutputs
    extracted_responses: List[Dict[str, str]]
