from typing_extensions import Annotated, Dict, List, TypedDict

from patchwork.common.constants import TOKEN_URL
from patchwork.common.utils.step_typing import StepTypeConfig


class CallLLMInputs(TypedDict, total=False):
    max_llm_calls: Annotated[int, StepTypeConfig(is_config=True)]
    prompt_file: Annotated[str, StepTypeConfig(is_config=True, or_op=["prompts"])]
    prompts: Annotated[List[Dict], StepTypeConfig(or_op=["prompt_file"])]
    model: Annotated[str, StepTypeConfig(is_config=True)]
    allow_truncated: Annotated[bool, StepTypeConfig(is_config=True)]
    model_args: Annotated[str, StepTypeConfig(is_config=True)]
    client_args: Annotated[str, StepTypeConfig(is_config=True)]
    openai_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key", "client_is_gcp", "anthropic_api_key"])
    ]
    anthropic_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key", "client_is_gcp", "openai_api_key"])
    ]
    patched_api_key: Annotated[
        str,
        StepTypeConfig(
            is_config=True,
            or_op=["openai_api_key", "google_api_key", "client_is_gcp", "anthropic_api_key"],
            msg=f"""\
Model API key not found.
Please login at: "{TOKEN_URL}"
Please go to the Integration's tab and generate an API key.
Please copy the access token that is generated, and add `--patched_api_key=<token>` to the command line.

If you are using a OpenAI API Key, please set `--openai_api_key=<token>`.""",
        ),
    ]
    google_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "openai_api_key", "anthropic_api_key", "client_is_gcp"])
    ]
    client_is_gcp: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "openai_api_key", "anthropic_api_key", "google_api_key"])
    ]
    file: Annotated[str, StepTypeConfig(is_path=True)]


class CallLLMOutputs(TypedDict):
    openai_responses: List[str]
    request_tokens: List[int]
    response_tokens: List[int]
