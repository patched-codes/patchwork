import string
from random import choices

import pytest
from slack_sdk import WebClient

from patchwork.steps.SlackMessage.SlackMessage import (
    SlackMessage,  # replace with the actual module name
)


@pytest.fixture
def mocked_slack_key():
    return "".join(choices(string.ascii_letters + string.digits, k=12))


@pytest.fixture
def mocked_slack_client(mocker, mocked_slack_key):
    mocked_slack_client = mocker.MagicMock()
    mocker.patch.object(WebClient, "__new__", return_value=mocked_slack_client)

    mocked_slack_client.auth_test.return_value = {"ok": True}
    mocked_slack_client.auth_teams_list.return_value = {"ok": True, "teams": [{"id": "team-id", "name": "team-name"}]}
    mocked_slack_client.conversations_list.return_value = {
        "ok": True,
        "channels": [{"id": "channel-id", "name": "channel-name"}],
    }
    return mocked_slack_client


def test_slack_message_init_valid_inputs(mocked_slack_client, mocked_slack_key):
    inputs = {
        "slack_token": mocked_slack_key,
        "slack_channel": "channel-name",
        "slack_message_template": "Hello {{name}}!",
        "slack_message_template_values": {"name": "John"},
    }
    slack_message = SlackMessage(inputs)
    assert slack_message.slack_channel == "channel-id"
    assert slack_message.slack_message == "Hello John!"


@pytest.mark.parametrize(
    "inputs",
    [
        {
            "slack_channel": "channel-name",
            "slack_message_template": "Hello {{name}}!",
            "slack_message_template_values": {"name": "John"},
        },
        {
            "slack_token": "valid-token",
            "slack_message_template": "Hello {{name}}!",
            "slack_message_template_values": {"name": "John"},
        },
        {
            "slack_token": "valid-token",
            "slack_channel": "channel-name",
            "slack_message_template_values": {"name": "John"},
        },
        {"slack_token": "valid-token", "slack_channel": "channel-name"},
        {
            "slack_token": "valid-token",
            "slack_team": "wrong-name",
            "slack_channel": "channel-name",
            "slack_message_template": "Hello {{name}}!",
        },
        {
            "slack_token": "valid-token",
            "slack_team": "team-name",
            "slack_channel": "wrong-name",
            "slack_message_template": "Hello {{name}}!",
        },
    ],
)
def test_slack_message_init_missing_required_key(mocked_slack_client, mocked_slack_key, inputs):
    if "slack_token" in inputs:
        inputs["slack_token"] = mocked_slack_key
    with pytest.raises(ValueError):
        SlackMessage(inputs)


def test_slack_message_run(mocked_slack_client, mocked_slack_key):
    mocked_slack_client.chat_postMessage.return_value = {"ok": True}
    inputs = {
        "slack_token": mocked_slack_key,
        "slack_channel": "channel-name",
        "slack_message_template": "Hello {{name}}!",
        "slack_message_template_values": {"name": "John"},
    }
    slack_message = SlackMessage(inputs)
    result = slack_message.run()
    assert result["is_slack_message_sent"] is True
