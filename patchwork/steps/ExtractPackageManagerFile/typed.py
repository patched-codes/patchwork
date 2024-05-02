from typing_extensions import NotRequired, TypedDict


class ExtractPackageManagerInputs(TypedDict):
    sbom_vdr_file_path: str
    package_manager_file: NotRequired[str]
    upgrade_threshold: NotRequired[str]
    severity: NotRequired[str]


class ExtractPackageManagerOutputs(TypedDict):
    prompt_value_file: str
    code_file: str
