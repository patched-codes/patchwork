from typing_extensions import List

from patchwork.common.client.sonar import SonarClient
from patchwork.step import Step, StepStatus
from patchwork.steps.ExtractCode.ExtractCode import read_and_get_source_code_context
from patchwork.steps.ScanSonar.typed import (
    ScanSonarInputs,
    ScanSonarOutputs,
    SonarVulnerability,
)


class ScanSonar(Step, input_class=ScanSonarInputs, output_class=ScanSonarOutputs):
    def __init__(self, inputs: dict):
        super().__init__(inputs)

        self.context_length = inputs.get("context_length", 1000)
        self.project_key = inputs.get("sonarqube_project_key")
        access_token = inputs.get("sonarqube_api_key")
        sonar_url = inputs.get("sonarqube_base_url")
        sonar_client_kwargs = dict(access_token=access_token)
        if sonar_url is not None:
            sonar_client_kwargs["url"] = sonar_url
        self.client = SonarClient(**sonar_client_kwargs)

    def run(self) -> dict:
        try:
            vulns_by_path = self.client.find_vulns(self.project_key)

            files_to_patch: List[SonarVulnerability] = []

            for file_path, vulns in vulns_by_path.items():
                for vuln in vulns:
                    data = read_and_get_source_code_context(file_path, vuln.start, vuln.end, self.context_length)
                    if data is None:
                        continue
                    source_code_context, start, end = data

                    vulnerability = SonarVulnerability(
                        uri=file_path,
                        startLine=start,
                        endLine=end,
                        affectedCode=source_code_context,
                        messageText=vuln.bug_msg,
                    )
                    files_to_patch.append(vulnerability)

            self.set_status(StepStatus.COMPLETED, "Successfully collected SonarQube results")
            return dict(files_to_patch=files_to_patch)

        except Exception as e:
            self.set_status(StepStatus.FAILED, f"Failed to collect SonarQube results: {str(e)}")
            raise
