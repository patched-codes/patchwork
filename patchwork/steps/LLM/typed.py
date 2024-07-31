from typing_extensions import Annotated, Any, Dict, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __LLMInputsRequired(TypedDict):
    # PreparePromptInputs
    prompt_template_file: Annotated[str, StepTypeConfig(is_config=True)]
    prompt_id: Annotated[str, StepTypeConfig(is_config=True)]


class LLMInputs(__LLMInputsRequired, total=False):
    prompt_value_file: Annotated[str, StepTypeConfig(or_op=["prompt_values"])]
    prompt_values: Annotated[List[Dict[str, Any]], StepTypeConfig(or_op=["prompt_value_file"])]
    # CallLLMInputs
    max_llm_calls: Annotated[int, StepTypeConfig(is_config=True)]
    prompt_file: Annotated[str, StepTypeConfig(is_config=True)]
    model: Annotated[str, StepTypeConfig(is_config=True)]
    allow_truncated: Annotated[bool, StepTypeConfig(is_config=True)]
    model_args: Annotated[str, StepTypeConfig(is_config=True)]
    client_args: Annotated[str, StepTypeConfig(is_config=True)]
    openai_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key"])]
    patched_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["openai_api_key", "google_api_key"])]
    google_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "openai_api_key"])]
    # ExtractModelResponseInputs
    response_partitions: Annotated[Dict[str, List[str]], StepTypeConfig(is_config=True)]


class LLMOutputs(TypedDict):
    # PreparePromptOutputs
    prompts: List[Dict]
    # CallLLMOutputs
    openai_responses: List[str]
    # ExtractModelResponseOutputs
    extracted_responses: List[Dict[str, str]]
