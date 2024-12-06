import os
from pathlib import Path

import pytest

from patchwork.steps.ExtractCode.ExtractCode import ExtractCode, Severity

_DEFAULT_SARIF_FILE_NAME = "sarif_file.sarif"


@pytest.fixture
def extract_code_instance(tmp_path):
    original_dir = Path.cwd()

    os.chdir(tmp_path)

    test_file = tmp_path / "test.py"
    test_file.write_text("print('Hello, world!')")

    inputs = {
        "sarif_values": {
            "runs": [
                {
                    "results": [
                        {
                            "message": {"text": "Error message"},
                            "ruleId": "1",
                            "locations": [
                                {
                                    "physicalLocation": {
                                        "artifactLocation": {"uri": str(test_file)},
                                        "region": {"startLine": 1, "endLine": 1},
                                    }
                                }
                            ],
                        }
                    ],
                    "tool": {"driver": {"rules": [{"id": "1", "defaultConfiguration": {"level": "high"}}]}},
                }
            ],
        },
        "context_size": 1000,
        "vulnerability_limit": 10,
        "severity": "HIGH",
    }
    yield ExtractCode(inputs)
    os.chdir(original_dir)


def test_extract_code_init(extract_code_instance):
    assert extract_code_instance.context_length == 1000
    assert extract_code_instance.vulnerability_limit == 10
    assert extract_code_instance.severity_threshold == Severity.HIGH


def test_extract_code_run(extract_code_instance, tmp_path):
    # Run the extract code step
    """Test the extract_code method of an ExtractCode instance.
    
    This method runs the extract_code step and verifies the expected output structure and content.
    
    Args:
        extract_code_instance (ExtractCode): An instance of the ExtractCode class to be tested.
        tmp_path (pathlib.Path): A temporary directory path provided by the pytest fixture.
    
    Returns:
        None
    
    Raises:
        AssertionError: If any of the assertions fail, indicating that the extract_code output
                        does not match the expected structure or content.
    """
    result = extract_code_instance.run()

    assert result.keys() == {"files_to_patch"}
    for output_data in result.values():
        assert len(output_data) == 1
        assert output_data[0]["uri"] == "test.py"
        assert output_data[0]["startLine"] == 0
        assert output_data[0]["endLine"] == 1
        assert output_data[0]["affectedCode"] == "print('Hello, world!')"
        assert output_data[0]["messageText"] == "Issue Description: Error message"


@pytest.fixture
def extract_code_instance_with_fix(tmp_path):
    """Extract code instance with fix from a given test file.
    
    Args:
        tmp_path (Path): A temporary directory path for creating and manipulating files.
    
    Returns:
        Generator[ExtractCode]: A generator that yields an ExtractCode object containing
        the extracted code instance with fix information.
    
    Raises:
        OSError: If there are issues with file operations or directory changes.
    """
    original_dir = Path.cwd()

    os.chdir(tmp_path)

    test_file = tmp_path / "test.py"
    test_file.write_text("print('Hello, world!')")

    inputs = {
        "sarif_values": {
            "runs": [
                {
                    "results": [
                        {
                            "fixes": [{"description": {"text": "Fix here"}}, {"description": {"text": "Fix there"}}],
                            "message": {"text": "Error message"},
                            "ruleId": "1",
                            "locations": [
                                {
                                    "physicalLocation": {
                                        "artifactLocation": {"uri": str(test_file)},
                                        "region": {"startLine": 1, "endLine": 1},
                                    }
                                }
                            ],
                        }
                    ],
                    "tool": {"driver": {"rules": [{"id": "1", "defaultConfiguration": {"level": "high"}}]}},
                }
            ],
        },
        "context_size": 1000,
        "vulnerability_limit": 10,
        "severity": "HIGH",
    }
    yield ExtractCode(inputs)
    os.chdir(original_dir)


def test_extract_code_run_with_fix(extract_code_instance_with_fix, tmp_path):
    # Run the extract code step
    """Test the extraction of code with fix functionality.
    
    Args:
        extract_code_instance_with_fix (ExtractCode): An instance of ExtractCode class with fix functionality.
        tmp_path (pathlib.Path): A temporary directory path for the test.
    
    Returns:
        None: This method doesn't return anything explicitly.
    
    Raises:
        AssertionError: If any of the assertions fail during the test.
    """
    result = extract_code_instance_with_fix.run()

    assert result.keys() == {"files_to_patch"}
    for output_data in result.values():
        assert len(output_data) == 1
        assert output_data[0]["uri"] == "test.py"
        assert output_data[0]["startLine"] == 0
        assert output_data[0]["endLine"] == 1
        assert output_data[0]["affectedCode"] == "print('Hello, world!')"
        assert (
            output_data[0]["messageText"]
            == """\
Issue Description: Error message
Suggested fixes:
- Fix here
- Fix there"""
        )
