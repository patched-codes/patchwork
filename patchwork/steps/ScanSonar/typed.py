from typing_extensions import Annotated, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __ScanSonarRequiredInputs(TypedDict):
    sonarqube_api_key: Annotated[
        str,
        StepTypeConfig(
            is_config=True,
            msg="""SonarQube access token not found.
Please generate an access token in your SonarQube instance and add `--sonarqube_api_key=<token>` to the command line.""",
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


class ScanSonarInputs(__ScanSonarRequiredInputs, total=False):
    sonarqube_base_url: Annotated[
        str,
        StepTypeConfig(
            is_config=True,
            msg="""SonarQube base URL not found.
Please provide the URL of your SonarQube instance using `--sonarqube_base_url=<url>`.
For SonarCloud, this would be https://sonarcloud.io""",
        ),
    ]


class SonarVulnerability(TypedDict):
    uri: str
    startLine: int
    endLine: int
    affectedCode: str
    messageText: str


class ScanSonarOutputs(TypedDict):
    files_to_patch: List[SonarVulnerability]
