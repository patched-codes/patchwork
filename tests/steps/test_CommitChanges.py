import git
import pytest

from patchwork.steps.CommitChanges.CommitChanges import CommitChanges


@pytest.fixture
def repo(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    repo = git.Repo.init(tmp_path, initial_branch="main")
    with repo.config_writer() as writer:
        writer.set_value("user", "name", "test")
        writer.set_value("user", "email", "test@test.com")
    repo.create_remote("origin", str(tmp_path))
    (tmp_path / "file.txt").write_text("base\n")
    repo.git.add("file.txt")
    repo.git.commit("-m", "base commit")
    return repo


def _run_commit_changes(tmp_path, filename="file.txt", content="patched\n"):
    (tmp_path / filename).write_text(content)
    inputs = {
        "modified_code_files": [{"path": str(tmp_path / filename)}],
        "branch_prefix": "patchwork-",
    }
    return CommitChanges(inputs).run()


def test_run_creates_branch_with_commit(repo, tmp_path):
    result = _run_commit_changes(tmp_path)

    assert result["target_branch"] == "patchwork-main"
    assert "patchwork-main" in repo.heads
    assert repo.active_branch.name == "main"
    assert (tmp_path / "file.txt").read_text() == "base\n"


def test_rerun_preserves_previous_unmerged_commit_in_backup_branch(repo, tmp_path):
    first_result = _run_commit_changes(tmp_path, content="first patch\n")
    first_commit = repo.heads[first_result["target_branch"]].commit

    second_result = _run_commit_changes(tmp_path, content="second patch\n")

    backup_branches = [head.name for head in repo.heads if head.name.startswith("patchwork-main-backup-")]
    assert len(backup_branches) == 1, "expected the discarded commit to be preserved as a backup branch"
    assert repo.heads[backup_branches[0]].commit == first_commit

    assert repo.heads[second_result["target_branch"]].commit != first_commit
