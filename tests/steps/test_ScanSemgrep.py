import random
import string
from collections import namedtuple
from pathlib import Path

from patchwork.steps import ScanSemgrep

MockedCompletedProcessClass = namedtuple("CompletedProcess", ["stdout"])


def test_scan_semgrep_enabled(mocker):
    """
    Test when sarif_file_path is not present in inputs
    """

    # Test setup
    inputs = {"_sarif_file_path": "not_present"}
    expected_text = "".join(random.choices(string.ascii_letters, k=12))

    mocked_subprocess_run = mocker.patch("subprocess.run")
    mocked_subprocess_run.return_value = MockedCompletedProcessClass(stdout=expected_text)

    # Actual test
    scan_semgrep = ScanSemgrep(inputs)
    result = scan_semgrep.run()

    # Assertions
    assert result.get("sarif_file_path") is not None
    assert Path(result["sarif_file_path"]).is_file()
    assert Path(result["sarif_file_path"]).read_text() == expected_text
    assert scan_semgrep.enabled


def test_scan_semgrep_disabled(mocker):
    """
    Test when sarif_file_path is present in inputs
    """
    # Test setup
    inputs = {"sarif_file_path": "already_present"}

    mocked_subprocess_run = mocker.patch("subprocess.run")

    # Actual test
    scan_semgrep = ScanSemgrep(inputs)
    result = scan_semgrep.run()

    # Assertions
    assert mocked_subprocess_run.called is False
    assert result == dict()  # Check if result is empty dict
    assert not scan_semgrep.enabled
