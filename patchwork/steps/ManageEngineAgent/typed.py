from typing_extensions import Annotated, Any, Dict, List, Optional, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __ManageEngineAgentInputsRequired(TypedDict):
    zoho_access_token: str
    user_prompt: str
    prompt_value: Dict[str, Any]


class ManageEngineAgentInputs(__ManageEngineAgentInputsRequired, total=False):
    max_agent_calls: int
    openai_api_key: Annotated[str, StepTypeConfig(or_op=["google_api_key", "anthropic_api_key"])]
    anthropic_api_key: Annotated[str, StepTypeConfig(or_op=["google_api_key", "openai_api_key"])]
    google_api_key: Annotated[str, StepTypeConfig(or_op=["openai_api_key", "anthropic_api_key"])]

    # Prompt and strategy configuration
    system_prompt: Optional[str]
    example_json: Optional[Dict]


class ManageEngineAgentOutputs(TypedDict):
    conversation_history: List[Dict]
    tool_records: List[Dict]
    request_tokens: int
    response_tokens: int
