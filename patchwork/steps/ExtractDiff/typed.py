from typing_extensions import NotRequired, TypedDict


class ExtractDiffInputs(TypedDict):
    update_info: "UpdateInfo"
    libraries_api_key: str
    github_api_key: str
    severity: NotRequired[str]


class ExtractDiffOutputs(TypedDict):
    prompt_value_file: str
    library_name: str
    platform_type: str


class UpdateInfo(TypedDict):
    vuln_version: str
    fixed_version: str
    purl: str
