from typing_extensions import Annotated, Any, Dict, Optional, TypedDict, List

from patchwork.common.utils.step_typing import StepTypeConfig


class __BrowserUseInputsRequired(TypedDict):
    task: str
    task_value: Dict[str, Any]


class BrowserUseInputs(__BrowserUseInputsRequired, total=False):
    example_json: Optional[str]
    openai_api_key: Annotated[str, StepTypeConfig(or_op=["google_api_key", "anthropic_api_key"])]
    anthropic_api_key: Annotated[str, StepTypeConfig(or_op=["google_api_key", "openai_api_key"])]
    google_api_key: Annotated[str, StepTypeConfig(or_op=["openai_api_key", "anthropic_api_key"])]
    gif_path: Optional[str]
    headless: Optional[bool]
    initial_actions: Optional[List[Dict[str, Dict[str, Any]]]]
    downloads_path: Optional[str]
    use_vision: Optional[bool]
    timeout: Optional[int]  # optional timeout in seconds, defaults to 600 if not provided


class BrowserUseOutputs(TypedDict):
    result: str
    request_tokens: int
    response_tokens: int
