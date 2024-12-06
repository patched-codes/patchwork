import pytest

from patchwork.steps import ReadIssues


@pytest.mark.parametrize(
    "inputs_extra,method_path,issue_texts",
    [
        (
            {"github_api_key": "key"},
            "patchwork.common.client.scm.GithubClient.find_issue_by_url",
            dict(title="", body="github pr body", comments=["nothing", "there"], description="Title:\n\n\nDescription:\ngithub pr body\n"),
        ),
        (
            {"gitlab_api_key": "key"},
            "patchwork.common.client.scm.GitlabClient.find_issue_by_url",
            dict(title="gitlab pr title", body="", comments=["something", "here"], description="Title:\ngitlab pr title\n\nDescription:\n\n"),
        ),
    ],
)
def test_read_issues(mocker, inputs_extra, method_path, issue_texts):
    # Set up
    """Test the read_issues method of the ReadIssues class.
    
    Args:
        mocker (pytest.MockFixture): A pytest fixture for mocking.
        inputs_extra (dict): Additional input parameters to be merged with base inputs.
        method_path (str): The path to the method to be mocked.
        issue_texts (dict): A dictionary containing issue texts.
    
    Returns:
        None: This test method doesn't return anything, but uses assertions to verify the behavior.
    
    Raises:
        AssertionError: If the results from read_issues.run() do not match the expected output.
    """
    base_inputs = {"issue_url": "https://example.com/issue"}
    inputs = {**base_inputs, **inputs_extra}

    mocked_scm_client = mocker.patch(method_path)
    mocked_scm_client.return_value = issue_texts

    # Actual Run
    read_issues = ReadIssues(inputs)
    results = read_issues.run()

    # Assertions
    assert results == {f"issue_{key}": value for key, value in issue_texts.items()}
