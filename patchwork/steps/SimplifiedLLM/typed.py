from typing_extensions import Annotated, Any, Dict, List, Optional

from patchwork.common.utils.step_typing import StepTypeConfig


class SimplifiedLLMInputs(TypedDict):
    # PreparePromptInputs
    prompt_user: Annotated[str, StepTypeConfig(is_config=True)]
    prompt_values: List[Dict[str, Any]]
    prompt_system: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    # CallLLMInputs
    model: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    openai_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    patched_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    google_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    json: Optional[Annotated[bool, StepTypeConfig(is_config=True)]] = None
    # ExtractModelResponseInputs
    response_partitions: Optional[Annotated[Dict[str, List[str]], StepTypeConfig(is_config=True)]] = None


class SimplifiedLLMOutputs(TypedDict):
    # PreparePromptOutputs
    prompts: List[Dict]
    # CallLLMOutputs
    openai_responses: List[str]
    # ExtractModelResponseOutputs
    extracted_responses: List[Dict[str, str]]
