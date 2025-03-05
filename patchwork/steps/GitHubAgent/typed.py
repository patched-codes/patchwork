from typing_extensions import Annotated, Any, Dict, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class GitHubAgentInputs(TypedDict, total=False):
    base_path: str
    prompt_value: Dict[str, Any]
    system_prompt: str
    user_prompt: str
    max_llm_calls: Annotated[int, StepTypeConfig(is_config=True)]
    openai_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key", "anthropic_api_key"])
    ]
    anthropic_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key", "openai_api_key"])
    ]
    google_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "openai_api_key", "anthropic_api_key"])
    ]


class GitHubAgentOutputs(TypedDict):
    conversation_history: List[Dict]
    tool_records: List[Dict]
    request_tokens: int
    response_tokens: int
