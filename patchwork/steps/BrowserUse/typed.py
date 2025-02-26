from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class BrowserUseInputs(TypedDict, total=False):
    task: str
    json_example_schema: str
    openai_api_key: Annotated[
        str,
        StepTypeConfig(is_config=True, or_op=["google_api_key", "anthropic_api_key"]),
    ]
    anthropic_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["google_api_key", "openai_api_key"])
    ]
    google_api_key: Annotated[
        str,
        StepTypeConfig(is_config=True, or_op=["openai_api_key", "anthropic_api_key"]),
    ]
    generate_gif: Annotated[bool, StepTypeConfig(is_config=True)]


class BrowserUseOutputs(TypedDict):
    result: str
    request_tokens: int
    response_tokens: int
