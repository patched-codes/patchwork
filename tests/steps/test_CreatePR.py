import logging

import git
import pytest

from patchwork.steps.CreatePR import CreatePR as create_pr_module
from patchwork.steps.CreatePR.CreatePR import CreatePR


@pytest.fixture
def repo(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    repo = git.Repo.init(tmp_path, initial_branch="main")
    with repo.config_writer() as writer:
        writer.set_value("user", "name", "test")
        writer.set_value("user", "email", "test@test.com")
    (tmp_path / "file.txt").write_text("base\n")
    repo.git.add("file.txt")
    repo.git.commit("-m", "base commit")
    return repo


def test_push_failure_message_names_branch_and_recovery_command(repo, monkeypatch, caplog):
    monkeypatch.setattr("patchwork.common.client.scm.GithubClient.test", lambda self: True)
    monkeypatch.setattr(create_pr_module, "push", lambda repo, args: False)

    inputs = {
        "target_branch": "patchwork-main",
        "base_branch": "main",
        "github_api_key": "fake-token",
        "force_pr_creation": True,
    }
    step = CreatePR(inputs)

    with caplog.at_level(logging.ERROR, logger="patched"):
        with pytest.raises(ValueError):
            step.run()

    assert '"patchwork-main"' in caplog.text
    assert "were not lost" in caplog.text
    assert "git push origin patchwork-main" in caplog.text
