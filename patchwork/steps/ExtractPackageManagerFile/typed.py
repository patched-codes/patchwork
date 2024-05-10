from typing_extensions import Iterable, NotRequired, TypedDict


class ExtractPackageManagerInputs(TypedDict):
    sbom_vdr_file_path: NotRequired[str]
    sbom_vdr_values: NotRequired[dict]
    package_manager_file: NotRequired[str]
    upgrade_threshold: NotRequired[str]
    severity: NotRequired[str]


class ExtractPackageManagerOutputs(TypedDict):
    prompt_values: Iterable[dict]
    files_to_patch: Iterable[dict]
