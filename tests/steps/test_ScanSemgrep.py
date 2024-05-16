import random
import string
from collections import namedtuple
from pathlib import Path

import pytest

from patchwork.steps import ScanSemgrep

MockedCompletedProcessClass = namedtuple("CompletedProcess", ["stdout"])


def test_scan_semgrep_enabled(mocker):
    """
    Test when sarif_file_path is not present in inputs
    """

    # Test setup
    inputs = {"_sarif_file_path": "not_present"}
    expected_text = "{}"

    mocked_subprocess_run = mocker.patch("subprocess.run")
    mocked_subprocess_run.return_value = MockedCompletedProcessClass(stdout=expected_text)

    # Actual test
    scan_semgrep = ScanSemgrep(inputs)
    result = scan_semgrep.run()

    # Assertions
    assert result.get("sarif_values") is not None
    assert result["sarif_values"] == {}


def test_scan_semgrep_file(mocker, tmp_path):
    """
    Test when sarif_file_path is not present in inputs
    """

    sarif_path = tmp_path / "sarif.json"
    with open(sarif_path, "w") as f:
        f.write("{}")

    # Test setup
    inputs = {"sarif_file_path": sarif_path}

    mocked_subprocess_run = mocker.patch("subprocess.run")

    # Actual test
    scan_semgrep = ScanSemgrep(inputs)
    result = scan_semgrep.run()

    # Assertions
    assert mocked_subprocess_run.call_count == 0
    assert result.get("sarif_values") is not None
    assert result["sarif_values"] == {}


def test_scan_semgrep_raises():
    """
    Test when sarif_file_path is present but does not exist in inputs
    """
    # Test setup
    inputs = {"sarif_file_path": "already_present"}

    # Actual test
    # Assertions
    with pytest.raises(ValueError):
        ScanSemgrep(inputs)
