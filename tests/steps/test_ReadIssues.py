import pytest

from patchwork.steps import ReadIssues


@pytest.mark.parametrize(
    "inputs_extra,method_path,issue_texts",
    [
        (
            {"github_api_key": "key"},
            "patchwork.common.client.scm.GithubClient.find_issue_by_url",
            dict(title="", body="github pr body", comments=["nothing", "there"]),
        ),
        (
            {"gitlab_api_key": "key"},
            "patchwork.common.client.scm.GitlabClient.find_issue_by_url",
            dict(title="gitlab pr title", body="", comments=["something", "here"]),
        ),
    ],
)
def test_read_issues(mocker, inputs_extra, method_path, issue_texts):
    # Set up
    base_inputs = {"issue_url": "https://example.com/issue"}
    inputs = {**base_inputs, **inputs_extra}

    mocked_scm_client = mocker.patch(method_path)
    mocked_scm_client.return_value = issue_texts

    # Actual Run
    read_issues = ReadIssues(inputs)
    results = read_issues.run()

    # Assertions
    assert results == {f"issue_{key}": value for key, value in issue_texts.items()}
