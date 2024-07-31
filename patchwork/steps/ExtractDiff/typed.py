from typing_extensions import Annotated, Dict, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __ExtractDiffRequiredInputs(TypedDict):
    update_info: "UpdateInfo"
    libraries_api_key: Annotated[str, StepTypeConfig(is_config=True)]
    github_api_key: Annotated[str, StepTypeConfig(is_config=True)]


class ExtractDiffInputs(__ExtractDiffRequiredInputs, total=False):
    severity: Annotated[str, StepTypeConfig(is_config=True)]


class ExtractDiffOutputs(TypedDict):
    prompt_values: List[Dict]
    library_name: str
    platform_type: str


class UpdateInfo(TypedDict):
    vuln_version: str
    fixed_version: str
    purl: str
