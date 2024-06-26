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
    result = extract_code_instance.run()

    # Check that the extracted code contexts are correct
    assert len(extract_code_instance.extracted_code_contexts) == 1
    assert extract_code_instance.extracted_code_contexts[0]["uri"] == "test.py"
    assert extract_code_instance.extracted_code_contexts[0]["startLine"] == 0
    assert extract_code_instance.extracted_code_contexts[0]["endLine"] == 1
    assert extract_code_instance.extracted_code_contexts[0]["affectedCode"] == "print('Hello, world!')"
    assert extract_code_instance.extracted_code_contexts[0]["messageText"] == "Error message"

    assert result.keys() == {"files_to_patch"}
    for output_data in result.values():
        assert len(output_data) == 1
        assert output_data[0]["uri"] == "test.py"
        assert output_data[0]["startLine"] == 0
        assert output_data[0]["endLine"] == 1
        assert output_data[0]["affectedCode"] == "print('Hello, world!')"
        assert output_data[0]["messageText"] == "Error message"
