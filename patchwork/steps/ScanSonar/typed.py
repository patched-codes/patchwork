from typing_extensions import Annotated, TypedDict, List
from patchwork.common.utils.step_typing import StepTypeConfig

class __ScanSonarRequiredInputs(TypedDict):
    pass

class ScanSonarInputs(__ScanSonarRequiredInputs, total=False):
    sonarqube_access_token: Annotated[
        str,
        StepTypeConfig(
            is_config=True,
            msg="""SonarQube access token not found.
Please generate an access token in your SonarQube instance and add `--sonarqube_access_token=<token>` to the command line.""",
        ),
    ]
    sonarqube_base_url: Annotated[
        str,
        StepTypeConfig(
            is_config=True,
            msg="""SonarQube base URL not found.
Please provide the URL of your SonarQube instance using `--sonarqube_base_url=<url>`.
For SonarCloud, this would be https://sonarcloud.io""",
        ),
    ]
    sonarqube_project_key: Annotated[
        str,
        StepTypeConfig(
            is_config=True,
            msg="""SonarQube project key not found.
Please provide your project key using `--sonarqube_project_key=<key>`.
You can find this in your SonarQube project settings.""",
        ),
    ]

class SonarVulnerability(TypedDict):
    uri: str
    startLine: int
    endLine: int
    cwe: str
    description: str

class ScanSonarOutputs(TypedDict):
    files_to_patch: List[SonarVulnerability]
