import json

import pytest

from patchwork.steps.ModifyCode.ModifyCode import (
    ModifyCode,
    handle_indent,
    replace_code_in_file,
    save_file_contents,
)


def test_save_file_contents(tmp_path):
    file_path = tmp_path / "test.txt"
    content = "Hello, World!"
    save_file_contents(str(file_path), content)
    assert file_path.read_text() == content


@pytest.mark.parametrize(
    "src,target,expected",
    [
        ([], [], []),
        (["line 1"], ["line 1"], ["line 1"]),
        (["line 1", "line 2"], ["line 1", "line 2"], ["line 1", "line 2"]),
        (["  def foo():", "    pass"], ["  def bar():", "    pass"], ["  def bar():", "    pass"]),
        (["  def foo():", "    pass"], ["def bar():", "  pass"], ["  def bar():", "    pass"]),
        (["\tdef foo():", "\t\tpass"], ["def bar():", "\tpass"], ["\tdef bar():", "\t\tpass"]),
    ],
)
def test_handle_indent(src, target, expected):
    indented_target = handle_indent(src, target, 0, 999)
    assert indented_target == expected


def test_replace_code_in_file(tmp_path):
    """Test the replace_code_in_file function.
    
    Args:
        tmp_path (pathlib.Path): A temporary directory path fixture provided by pytest.
    
    Returns:
        None: This function doesn't return anything explicitly.
    
    Raises:
        AssertionError: If the file content after replacement doesn't match the expected output.
    """
    file_path = tmp_path / "test.txt"
    file_path.write_text("line 1\nline 2\nline 3")
    start_line = 1
    end_line = 3
    new_code = "new line 1\nnew line 2"
    replace_code_in_file(str(file_path), start_line, end_line, new_code)
    assert file_path.read_text() == "line 1\nnew line 1\nnew line 2\n"


def test_modify_code_init():
    inputs = {
        "files_to_patch": [{"uri": "path/to/uri", "startLine": 1, "endLine": 2}],
        "extracted_responses": [{"uri": "path/to/uri", "startLine": 1, "endLine": 2, "patch": "new_code"}],
    }
    modify_code = ModifyCode(inputs)
    assert modify_code.files_to_patch == [{"uri": "path/to/uri", "startLine": 1, "endLine": 2}]
    assert modify_code.extracted_responses == [
        {"uri": "path/to/uri", "startLine": 1, "endLine": 2, "patch": "new_code"}
    ]


def test_modify_code_run(tmp_path):
    """Test the modify_code_run functionality
    
    This function tests the ModifyCode class's run method by creating a temporary file,
    modifying its content, and verifying the result.
    
    Args:
        tmp_path (pathlib.Path): A pytest fixture that provides a temporary directory unique to the test invocation.
    
    Returns:
        None
    
    Raises:
        AssertionError: If the result doesn't contain the expected 'modified_code_files' key or if the number of modified files is not 1.
    """
    file_path = tmp_path / "test.txt"
    file_path.write_text("line 1\nline 2\nline 3")

    code_snippets_path = tmp_path / "code.json"
    with open(code_snippets_path, "w") as f:
        json.dump([{"uri": str(file_path), "startLine": 1, "endLine": 2}], f)

    inputs = {
        "files_to_patch": [{"uri": str(file_path), "startLine": 1, "endLine": 2}],
        "extracted_responses": [{"patch": "new_code"}],
    }
    modify_code = ModifyCode(inputs)
    result = modify_code.run()
    assert result.get("modified_code_files") is not None
    assert len(result["modified_code_files"]) == 1


def test_modify_code_none_edit(tmp_path):
    """Test the modify_code method with no edits
    
    This function tests the behavior of the ModifyCode class when no edits are provided.
    It creates a test file, sets up input data with no patch, and verifies that the
    ModifyCode.run() method returns an empty list of modified code files.
    
    Args:
        tmp_path (pathlib.Path): A temporary directory path provided by pytest for testing
    
    Returns:
        None: This test function doesn't return anything, it uses assertions to verify behavior
    
    Raises:
        AssertionError: If the assertions in the test fail
    """
    file_path = tmp_path / "test.txt"
    file_path.write_text("line 1\nline 2\nline 3")

    code_snippets_path = tmp_path / "code.json"
    with open(code_snippets_path, "w") as f:
        json.dump([{"uri": str(file_path), "startLine": 1, "endLine": 2}], f)

    inputs = {
        "files_to_patch": [{"uri": str(file_path), "startLine": 1, "endLine": 2}],
        "extracted_responses": [{"patch": None}],
    }
    modify_code = ModifyCode(inputs)
    result = modify_code.run()
    assert result.get("modified_code_files") is not None
    assert len(result["modified_code_files"]) == 0
