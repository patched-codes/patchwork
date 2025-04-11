from typing_extensions import Annotated, Any, Dict, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __DatabaseAgentOutputsRequiredInputs(TypedDict):
    task: str
    db_dialect: str


class DatabaseAgentInputs(__DatabaseAgentOutputsRequiredInputs, total=False):
    db_driver: str
    db_username: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str
    db_params: dict[str, Any]
    db_driver_args: dict[str, Any]
    prompt_value: Dict[str, Any]
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
    example_json: str


class DatabaseAgentOutputs(TypedDict):
    request_tokens: int
    response_tokens: int
