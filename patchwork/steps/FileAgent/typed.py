from typing_extensions import Annotated, Any, Dict, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __ReconcilationAgentRequiredInputs(TypedDict):
    task: str


class FileAgentInputs(__ReconcilationAgentRequiredInputs, total=False):
    base_path: str
    prompt_value: Dict[str, Any]
    max_llm_calls: Annotated[int, StepTypeConfig(is_config=True)]
    anthropic_api_key: Annotated[str, StepTypeConfig(is_config=True)]


class FileAgentOutputs(TypedDict):
    request_tokens: int
    response_tokens: int
