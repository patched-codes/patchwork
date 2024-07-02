from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class __SlackMessageRequiredInputs(TypedDict):
    slack_channel: Annotated[str, IS_CONFIG]
    slack_token: Annotated[str, IS_CONFIG]


class SlackMessageInputs(__SlackMessageRequiredInputs, total=False):
    slack_message_template_file: Annotated[str, IS_CONFIG]
    slack_message_template: Annotated[str, IS_CONFIG]
    slack_message_values: dict[str, str]


class SlackMessageOutputs(TypedDict):
    is_slack_message_sent: bool
