import pytest
from patchwork.steps import CreatePR


@pytest.fixture
def create_pr_instance():
    inputs = {
        "github_api_key": "fake_key",
        "scm_url": "https://github.com/user/repo",
        "pr_body": "This is a test PR",
        "pr_title": "Test PR",
        "base_branch": "main",
        "target_branch": "feature-branch"
    }
    return CreatePR(inputs)


def test_pr_creation_enabled(create_pr_instance):
    result = create_pr_instance.run()
    assert "pr_url" in result


def test_pr_creation_disabled():
    inputs = {
        "disable_pr": True,
        "target_branch": "feature-branch"
    }
    create_pr_instance = CreatePR(inputs)
    result = create_pr_instance.run()
    assert result == {}


def test_pr_creation_missing_api_keys():
    inputs = {
        "target_branch": "feature-branch"
    }
    with pytest.raises(ValueError):
        CreatePR(inputs)


def test_pr_creation_enabled_with_missing_base_branch():
    inputs = {
        "github_api_key": "fake_key",
        "scm_url": "https://github.com/user/repo",
        "pr_body": "This is a test PR",
        "pr_title": "Test PR",
        "target_branch": "feature-branch"
    }
    create_pr_instance = CreatePR(inputs)
    result = create_pr_instance.run()
    assert result == {}


def test_pr_creation_same_base_and_target_branch():
    inputs = {
        "github_api_key": "fake_key",
        "scm_url": "https://github.com/user/repo",
        "pr_body": "This is a test PR",
        "pr_title": "Test PR",
        "base_branch": "feature-branch",
        "target_branch": "feature-branch"
    }
    create_pr_instance = CreatePR(inputs)
    result = create_pr_instance.run()
    assert result == {}

def test_pr_creation_with_force_flag(create_pr_instance):
    create_pr_instance.force = True
    result = create_pr_instance.run()
    assert "pr_url" in result
