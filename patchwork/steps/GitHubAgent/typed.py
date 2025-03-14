from typing_extensions import Annotated, Any, Dict, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __GitHubAgentRequiredInputs(TypedDict):
    task: str


class GitHubAgentInputs(__GitHubAgentRequiredInputs, total=False):
    base_path: str
    prompt_value: Dict[str, Any]
    max_llm_calls: Annotated[int, StepTypeConfig(is_config=True)]
    openai_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key", "client_is_gcp", "anthropic_api_key"])
    ]
    anthropic_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key", "client_is_gcp", "openai_api_key"])
    ]
    google_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "openai_api_key", "client_is_gcp", "anthropic_api_key"])
    ]
    client_is_gcp: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "openai_api_key", "anthropic_api_key", "google_api_key"])
    ]


class GitHubAgentOutputs(TypedDict):
    request_tokens: int
    response_tokens: int
