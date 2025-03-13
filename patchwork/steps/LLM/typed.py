from typing_extensions import Annotated, Any, Dict, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig
from patchwork.steps.CallLLM.CallLLM import TOKEN_URL


class __LLMInputsRequired(TypedDict):
    # PreparePromptInputs
    prompt_template_file: Annotated[str, StepTypeConfig(is_config=True)]
    prompt_id: Annotated[str, StepTypeConfig(is_config=True)]


class LLMInputs(__LLMInputsRequired, total=False):
    prompt_value_file: Annotated[str, StepTypeConfig(or_op=["prompt_values"])]
    prompt_values: Annotated[List[Dict[str, Any]], StepTypeConfig(or_op=["prompt_value_file"])]
    # CallLLMInputs
    max_llm_calls: Annotated[int, StepTypeConfig(is_config=True)]
    prompt_file: Annotated[str, StepTypeConfig(is_config=True)]
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
    # ExtractModelResponseInputs
    response_partitions: Annotated[Dict[str, List[str]], StepTypeConfig(is_config=True)]


class LLMOutputs(TypedDict):
    # PreparePromptOutputs
    prompts: List[Dict]
    # CallLLMOutputs
    openai_responses: List[str]
    request_tokens: List[int]
    response_tokens: List[int]
    # ExtractModelResponseOutputs
    extracted_responses: List[Dict[str, str]]
