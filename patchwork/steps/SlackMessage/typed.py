from typing_extensions import NotRequired, TypedDict


class SlackMessageInputs(TypedDict):
    slack_channel: str
    slack_token: str
    slack_message_template_file: NotRequired[str]
    slack_message_template: NotRequired[str]
    slack_message_values: NotRequired[dict[str, str]]


class SlackMessageOutputs(TypedDict):
    is_slack_message_sent: bool
