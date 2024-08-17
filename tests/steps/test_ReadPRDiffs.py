import pytest

from patchwork.common.client.scm import PullRequestProtocol
from patchwork.steps.ReadPRDiffs.ReadPRDiffs import _IGNORED_EXTENSIONS, ReadPRDiffs


@pytest.mark.parametrize(
    "inputs_extra,method_path,texts,expected",
    [
        (
            {"github_api_key": "key"},
            "patchwork.common.client.scm.GithubClient.get_pr_by_url",
            dict(title="this", body="", comments=[], diffs=dict(path="diff")),
            [dict(path="path", diff="diff", title="this", body="")],
        ),
        (
            {"gitlab_api_key": "key"},
            "patchwork.common.client.scm.GitlabClient.get_pr_by_url",
            dict(title="", body="that", comments=[], diffs=dict(path="diff")),
            [dict(path="path", diff="diff", body="that", title="")],
        ),
        (
            {"github_api_key": "key"},
            "patchwork.common.client.scm.GithubClient.get_pr_by_url",
            dict(title="", body="", comments=[], diffs={f"path{ext}": "diff" for ext in _IGNORED_EXTENSIONS}),
            [],
        ),
    ],
)
def test_read_prdiffs(mocker, inputs_extra, method_path, texts, expected):
    # Set up
    base_inputs = {"pr_url": "https://example.com/pr"}
    inputs = {**base_inputs, **inputs_extra}

    mocked_pr = mocker.Mock(spec=PullRequestProtocol)
    mocked_pr.texts.return_value = texts
    mocked_scm_client = mocker.patch(method_path)
    mocked_scm_client.return_value = mocked_pr

    # Actual Run
    read_pr_diffs = ReadPRDiffs(inputs)
    results = read_pr_diffs.run()

    # Assertions
    assert results.get("prompt_values") == expected
