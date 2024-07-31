from typing_extensions import Annotated, Any, Dict, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __PreparePromptRequiredInputs(TypedDict):
    prompt_template_file: Annotated[str, StepTypeConfig(is_config=True)]
    prompt_id: Annotated[str, StepTypeConfig(is_config=True)]


class PreparePromptInputs(__PreparePromptRequiredInputs, total=False):
    prompt_value_file: Annotated[str, StepTypeConfig(or_op=["prompt_values"])]
    prompt_values: Annotated[List[Dict[str, Any]], StepTypeConfig(or_op=["prompt_value_file"])]


class PreparePromptOutputs(TypedDict):
    prompts: List[Dict]
