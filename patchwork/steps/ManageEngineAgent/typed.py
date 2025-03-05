from typing import Dict, Optional, TypedDict

from typing_extensions import Annotated

from patchwork.common.utils.step_typing import StepTypeConfig


class ManageEngineAgentInputs(TypedDict, total=False):
    """
    Inputs for the ManageEngine agentic step
    """

    # Required inputs
    me_access_token: str

    # Optional configuration
    max_agent_calls: int
    openai_api_key: Annotated[
        str,
        StepTypeConfig(
            is_config=True,
            or_op=["patched_api_key", "google_api_key", "anthropic_api_key"],
        ),
    ]
    anthropic_api_key: Annotated[
        str,
        StepTypeConfig(
            is_config=True,
            or_op=["patched_api_key", "google_api_key", "openai_api_key"],
        ),
    ]
    google_api_key: Annotated[
        str,
        StepTypeConfig(
            is_config=True,
            or_op=["patched_api_key", "openai_api_key", "anthropic_api_key"],
        ),
    ]

    # Prompt and strategy configuration
    system_prompt: Optional[str]
    user_prompt: str
    example_json: Optional[Dict]


class ManageEngineAgentOutputs(TypedDict, total=False):
    """
    Outputs from the ManageEngine agentic step
    """

    result: Dict
    usage: Dict
    error: Optional[str]
