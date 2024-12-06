import pytest

from patchwork.steps import PreparePR


@pytest.fixture
def prepare_pr_instance():
    """Prepares a PreparePR instance with modified code files information.
    
    Args:
        None
    
    Returns:
        PreparePR: An instance of PreparePR class initialized with a dictionary containing
                   information about modified code files.
    
    """
    inputs = {
        "modified_code_files": [
            {"path": "file1", "start_line": 1, "end_line": 2, "commit_message": "commit msg"},
            {"path": "file2", "patch_message": "patch msg"},
            {"path": "file1", "start_line": 3, "end_line": 4, "commit_message": "commit msg"},
        ]
    }
    return PreparePR(inputs)


def test_init_required_keys(prepare_pr_instance):
    assert prepare_pr_instance.required_keys == {"modified_code_files"}


def test_init_inputs(prepare_pr_instance):
    assert prepare_pr_instance.modified_code_files == [
        {"path": "file1", "start_line": 1, "end_line": 2, "commit_message": "commit msg"},
        {"path": "file2", "patch_message": "patch msg"},
        {"path": "file1", "start_line": 3, "end_line": 4, "commit_message": "commit msg"},
    ]


def test_run(prepare_pr_instance):
    result = prepare_pr_instance.run()
    assert "pr_body" in result
    assert result["pr_body"].startswith(prepare_pr_instance.header)


def test_run_no_modified_files():
    inputs = {"modified_code_files": []}
    prepare_pr_instance = PreparePR(inputs)
    result = prepare_pr_instance.run()
    assert result["pr_body"] == ""
    assert prepare_pr_instance.status.name == "SKIPPED"


def test_init_missing_required_keys():
    with pytest.raises(ValueError):
        PreparePR({})


def test_run_pr_header_override():
    inputs = {
        "modified_code_files": [{"path": "file1"}],
        "pr_header": "Custom PR header",
    }
    prepare_pr_instance = PreparePR(inputs)
    result = prepare_pr_instance.run()
    assert result["pr_body"].startswith("Custom PR header")
