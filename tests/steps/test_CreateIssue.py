import pytest

from patchwork.steps.CreateIssue.CreateIssue import CreateIssue


@pytest.mark.parametrize(
    "inputs",
    [
        {"issue_title": "my issue", "issue_text": "my issue text", "scm_url": "https://github.com/my/repo"},
        {"issue_title": "my issue", "scm_url": "https://github.com/my/repo", "github_api_key": "my api key"},
        {"issue_text": "my issue text", "scm_url": "https://github.com/my/repo", "github_api_key": "my api key"},
    ],
)
def test_init_missing_required_keys(inputs):
    with pytest.raises(ValueError) as e:
        CreateIssue(inputs)


def test_init_required_keys():
    inputs = {
        "issue_title": "my issue",
        "issue_text": "my issue text",
        "scm_url": "https://github.com/my/repo",
        "github_api_key": "my api key",
    }
    create_issue = CreateIssue(inputs)
    assert create_issue.issue_title == "my issue"
    assert create_issue.issue_text == "my issue text"


def test_run(mocker):
    inputs = {
        "issue_title": "my issue",
        "issue_text": "my issue text",
        "scm_url": "https://github.com/my/repo",
        "github_api_key": "my api key",
    }
    mocked_create_issue_comment = mocker.patch("patchwork.common.client.scm.GithubClient.create_issue_comment")
    mocked_create_issue_comment.return_value = "https://github.com/my/repo/issues/1"

    create_issue = CreateIssue(inputs)
    output = create_issue.run()
    assert output["issue_url"] == "https://github.com/my/repo/issues/1"
    assert create_issue.scm_client is not None
