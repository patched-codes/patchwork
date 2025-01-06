from typing_extensions import Annotated, Any, Dict, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig
from patchwork.steps.CallLLM.CallLLM import TOKEN_URL


class __AgenticLLMInputsRequired(TypedDict):
    # PreparePromptInputs
    prompt_template_file: Annotated[str, StepTypeConfig(is_config=True)]
    prompt_id: Annotated[str, StepTypeConfig(is_config=True)]


class AgenticLLMInputs(__AgenticLLMInputsRequired, total=False):
    prompt_values: Annotated[List[Dict[str, Any]], StepTypeConfig(or_op=["prompt_value_file"])]
    system_prompt: str
    user_prompt: str
    max_llm_calls: Annotated[int, StepTypeConfig(is_config=True)]
    model_args: Annotated[str, StepTypeConfig(is_config=True)]
    client_args: Annotated[str, StepTypeConfig(is_config=True)]
    openai_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key", "anthropic_api_key"])
    ]
    anthropic_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key", "openai_api_key"])
    ]
    patched_api_key: Annotated[
        str,
        StepTypeConfig(
            is_config=True,
            or_op=["openai_api_key", "google_api_key", "anthropic_api_key"],
            msg=f"""\
Model API key not found.
Please login at: "{TOKEN_URL}"
Please go to the Integration's tab and generate an API key.
Please copy the access token that is generated, and add `--patched_api_key=<token>` to the command line.

If you are using a OpenAI API Key, please set `--openai_api_key=<token>`.""",
        ),
    ]
    google_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "openai_api_key", "anthropic_api_key"])
    ]


class AgenticLLMOutputs(TypedDict):
    conversation_history: List[Dict]
    tool_records: List[Dict]
    # request_tokens: int
    # response_tokens: int