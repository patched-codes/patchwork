from pydantic import BaseModel
from typing_extensions import Annotated, Dict, Optional

from patchwork.common.utils.step_typing import StepTypeConfig


class SlackMessageInputs(BaseModel):
    slack_channel: Annotated[str, StepTypeConfig(is_config=True)]
    slack_token: Annotated[str, StepTypeConfig(is_config=True)]
    slack_message_template_file: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    slack_message_template: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    slack_message_values: Optional[Dict[str, str]] = None


class SlackMessageOutputs(BaseModel):
    is_slack_message_sent: bool
