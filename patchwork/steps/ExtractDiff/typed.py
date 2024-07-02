from typing_extensions import Annotated, Iterable, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class __ExtractDiffRequiredInputs(TypedDict):
    update_info: "UpdateInfo"
    libraries_api_key: Annotated[str, IS_CONFIG]
    github_api_key: Annotated[str, IS_CONFIG]


class ExtractDiffInputs(__ExtractDiffRequiredInputs, total=False):
    severity: Annotated[str, IS_CONFIG]


class ExtractDiffOutputs(TypedDict):
    prompt_values: Iterable[dict]
    library_name: str
    platform_type: str


class UpdateInfo(TypedDict):
    vuln_version: str
    fixed_version: str
    purl: str
