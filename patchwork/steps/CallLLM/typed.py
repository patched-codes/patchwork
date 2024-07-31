from typing_extensions import Annotated, Dict, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class CallLLMInputs(TypedDict, total=False):
    max_llm_calls: Annotated[int, StepTypeConfig(is_config=True)]
    prompt_file: Annotated[str, StepTypeConfig(is_config=True, or_op=["prompts"])]
    prompts: Annotated[List[Dict], StepTypeConfig(or_op=["prompt_file"])]
    model: Annotated[str, StepTypeConfig(is_config=True)]
    allow_truncated: Annotated[bool, StepTypeConfig(is_config=True)]
    model_args: Annotated[str, StepTypeConfig(is_config=True)]
    client_args: Annotated[str, StepTypeConfig(is_config=True)]
    openai_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key"])]
    patched_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["openai_api_key", "google_api_key"])]
    google_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "openai_api_key"])]


class CallLLMOutputs(TypedDict):
    openai_responses: List[str]
