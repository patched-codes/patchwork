from pathlib import Path
from unittest.mock import patch

import pytest

from patchwork.common.client.sonar import SonarClient, SonarVuln
from patchwork.steps.ScanSonar.ScanSonar import ScanSonar


def test_scan_sonar():
    inputs = {
        "sonarqube_project_key": "test-project",
        "sonarqube_api_key": "test-token",
        "sonarqube_base_url": "https://sonarcloud.io",
    }

    path_to_resource_file = Path(__file__).parent.parent / "cicd" / "generate_docstring" / "python_test_file.py"
    mock_vulns = {str(path_to_resource_file): [SonarVuln(start=13, end=14, cwe="CWE-79", bug_msg="Test vulnerability")]}

    with patch.object(SonarClient, "find_vulns", return_value=mock_vulns):
        step = ScanSonar(inputs)
        result = step.run()

        assert "files_to_patch" in result
        vulns = result["files_to_patch"]
        assert len(vulns) == 1

        vuln = vulns[0]
        assert vuln["uri"] == str(path_to_resource_file)
        assert vuln["startLine"] == 0
        assert vuln["endLine"] == 24
        assert vuln["messageText"] == "Test vulnerability"


def test_scan_sonar_error():
    inputs = {
        "sonarqube_project_key": "test-project",
        "sonarqube_api_key": "test-token",
        "sonarqube_base_url": "https://sonarcloud.io",
    }

    with patch.object(SonarClient, "find_vulns", side_effect=Exception("Test error")):
        step = ScanSonar(inputs)
        with pytest.raises(Exception) as exc_info:
            step.run()
        assert str(exc_info.value) == "Test error"
