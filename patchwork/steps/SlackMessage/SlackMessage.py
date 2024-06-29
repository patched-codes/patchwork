from __future__ import annotations

import logging

from patchwork.common.utils.dependency import slack_sdk
from patchwork.step import Step
from patchwork.steps.SlackMessage.typed import SlackMessageInputs


class SlackMessage(Step):
    def __init__(self, inputs):
        key_diff = SlackMessageInputs.__required_keys__.difference(inputs.keys())
        if key_diff:
            raise ValueError(f'Missing required data: "{key_diff}"')

        self.slack_client = slack_sdk().WebClient(token=inputs["slack_token"])
        if not self.slack_client.auth_test().get("ok", False):
            raise ValueError("Invalid Slack Token")

        slack_team = inputs.get("slack_team")
        response = self.slack_client.auth_teams_list()
        response_ok = response.get("ok", False)
        if slack_team is not None and not response_ok:
            raise ValueError("Unable to fetch Slack Teams")
        elif not response_ok:
            teams = [None]
        elif slack_team is None:
            teams = [team.get("id") for team in response.get("teams", [])]
        else:
            teams = [team.get("id") for team in response.get("teams", []) if team.get("name") == slack_team]

        slack_channel = inputs["slack_channel"]
        channels: list[str] = []
        for team in teams:
            response = self.slack_client.conversations_list(types="public_channel,private_channel", team=team)
            if not response.get("ok", False):
                raise ValueError("Unable to fetch Slack Channels")
            team_channels: list[str] = [
                channel.get("id") for channel in response.get("channels", []) if channel.get("name") == slack_channel
            ]
            channels.extend(team_channels)

        if len(channels) < 1:
            raise ValueError(f'Slack Channel "{slack_channel}" not found')
        if len(channels) > 1:
            logging.info(f'Multiple Slack Channels found for "{slack_channel}", using the first one.')
        self.slack_channel: str = channels[0]

        slack_template_file = inputs.get("slack_message_template_file")
        if slack_template_file is not None:
            with open(slack_template_file, "r") as fp:
                slack_template = fp.read()
        else:
            slack_template = inputs.get("slack_message_template")
        if slack_template is None:
            raise ValueError('Missing required data: "slack_message_template_file" or "slack_message_template"')

        self.slack_message = slack_template
        slack_template_values = inputs.get("slack_message_template_values")
        if slack_template_values is not None:
            for replacement_key, replacement_value in slack_template_values.items():
                self.slack_message = self.slack_message.replace("{{" + replacement_key + "}}", str(replacement_value))

    def run(self):
        response = self.slack_client.chat_postMessage(channel=self.slack_channel, text=self.slack_message)
        return dict(is_slack_message_sent=response.get("ok", False))
