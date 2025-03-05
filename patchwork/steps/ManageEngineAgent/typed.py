from typing_extensions import Annotated, Dict, List, Optional, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class ManageEngineAgentInputs(TypedDict, total=False):
    me_access_token: str
    max_agent_calls: int
    openai_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key", "anthropic_api_key"])
    ]
    anthropic_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key", "openai_api_key"])
    ]
    google_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "openai_api_key", "anthropic_api_key"])
    ]

    # Prompt and strategy configuration
    system_prompt: Optional[str]
    user_prompt: str
    example_json: Optional[Dict]


class ManageEngineAgentOutputs(TypedDict):
    conversation_history: List[Dict]
    tool_records: List[Dict]
    request_tokens: int
    response_tokens: int
