from __future__ import annotations

from typing_extensions import NotRequired, TypedDict


class __SlackMessageRequiredInputs(TypedDict):
    slack_channel: str
    slack_token: str


class SlackMessageInputs(__SlackMessageRequiredInputs, total=False):
    slack_message_template_file: NotRequired[str]
    slack_message_template: NotRequired[str]
    slack_message_values: NotRequired[dict[str, str]]


class SlackMessageOutputs(TypedDict):
    is_slack_message_sent: bool
