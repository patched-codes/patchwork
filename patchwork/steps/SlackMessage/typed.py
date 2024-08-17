from typing_extensions import Annotated, Dict, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __SlackMessageRequiredInputs(TypedDict):
    slack_channel: Annotated[str, StepTypeConfig(is_config=True)]
    slack_token: Annotated[str, StepTypeConfig(is_config=True)]


class SlackMessageInputs(__SlackMessageRequiredInputs, total=False):
    slack_message_template_file: Annotated[str, StepTypeConfig(is_config=True)]
    slack_message_template: Annotated[str, StepTypeConfig(is_config=True)]
    slack_message_values: Dict[str, str]


class SlackMessageOutputs(TypedDict):
    is_slack_message_sent: bool
