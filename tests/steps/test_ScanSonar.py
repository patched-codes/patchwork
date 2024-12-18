import pytest
from unittest.mock import Mock, patch

from patchwork.steps.ScanSonar.ScanSonar import ScanSonar
from patchwork.common.client.sonar import SonarClient, SonarVuln

def test_scan_sonar():
    inputs = {
        "sonarqube_project_key": "test-project",
        "sonarqube_access_token": "test-token",
        "sonarqube_base_url": "https://sonarcloud.io"
    }
    
    mock_vulns = {
        "src/file1.py": [
            SonarVuln(
                start=10,
                end=15,
                cwe="CWE-79",
                bug_msg="Test vulnerability"
            )
        ]
    }
    
    with patch.object(SonarClient, 'find_vulns', return_value=mock_vulns):
        step = ScanSonar(inputs)
        result = step.run()
        
        assert "files_to_patch" in result
        vulns = result["files_to_patch"]
        assert len(vulns) == 1
        
        vuln = vulns[0]
        assert vuln["uri"] == "src/file1.py"
        assert vuln["startLine"] == 10
        assert vuln["endLine"] == 15
        assert vuln["cwe"] == "CWE-79"
        assert vuln["description"] == "Test vulnerability"

def test_scan_sonar_error():
    inputs = {
        "sonarqube_project_key": "test-project",
        "sonarqube_api_key": "test-token",
        "sonarqube_base_url": "https://sonarcloud.io"
    }
    
    with patch.object(SonarClient, 'find_vulns', side_effect=Exception("Test error")):
        step = ScanSonar(inputs)
        with pytest.raises(Exception) as exc_info:
            step.run()
        assert str(exc_info.value) == "Test error"
