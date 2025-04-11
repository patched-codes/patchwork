from typing_extensions import Annotated, Any, Dict, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class AgenticLLMV2Inputs(TypedDict, total=False):
    base_path: str
    prompt_value: Dict[str, Any]
    system_prompt: str
    user_prompt: str
    max_agent_calls: Annotated[int, StepTypeConfig(is_config=True)]
    strategy_model: str
    agent_model: str
    agent_system_prompt: str
    example_json: str
    openai_api_key: Annotated[
        str,
        StepTypeConfig(
            is_config=True, or_op=["patched_api_key", "google_api_key", "client_is_gcp", "anthropic_api_key"]
        ),
    ]
    anthropic_api_key: Annotated[
        str,
        StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key", "client_is_gcp", "openai_api_key"]),
    ]
    google_api_key: Annotated[
        str,
        StepTypeConfig(
            is_config=True, or_op=["patched_api_key", "openai_api_key", "client_is_gcp", "anthropic_api_key"]
        ),
    ]
    client_is_gcp: Annotated[
        str,
        StepTypeConfig(
            is_config=True, or_op=["patched_api_key", "openai_api_key", "anthropic_api_key", "google_api_key"]
        ),
    ]


class AgenticLLMV2Outputs(TypedDict):
    request_tokens: int
    response_tokens: int
