from typing import List

from patchwork.step import Step, StepStatus
from patchwork.common.client.sonar import SonarClient
from patchwork.steps.ScanSonar.typed import (
    ScanSonarInputs, 
    ScanSonarOutputs,
    SonarVulnerability
)

class ScanSonar(Step, input_class=ScanSonarInputs, output_class=ScanSonarOutputs):
    def __init__(self, inputs: dict):
        super().__init__(inputs)
        
        self.project_key = inputs.get("sonarqube_project_key")
        self.access_token = inputs.get("sonarqube_access_token")
        self.sonar_url = inputs.get("sonarqube_base_url")
        
        self.client = SonarClient(
            access_token=self.access_token,
            url=self.sonar_url
        )

    def run(self) -> dict:
        try:
            vulns_by_path = self.client.find_vulns(self.project_key)
            
            files_to_patch: List[SonarVulnerability] = []
            
            for file_path, vulns in vulns_by_path.items():
                for vuln in vulns:
                    vulnerability = SonarVulnerability(
                        uri=file_path,
                        startLine=vuln.start,
                        endLine=vuln.end,
                        cwe=vuln.cwe,
                        description=vuln.bug_msg,
                    )
                    files_to_patch.append(vulnerability)
            
            self.set_status(StepStatus.COMPLETED, "Successfully collected SonarQube results")
            return dict(files_to_patch=files_to_patch)
            
        except Exception as e:
            self.set_status(StepStatus.FAILED, f"Failed to collect SonarQube results: {str(e)}")
            raise
