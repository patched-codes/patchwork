from typing_extensions import Iterable, NotRequired, TypedDict


class ExtractPackageManagerFileInputs(TypedDict):
    sbom_vdr_file_path: NotRequired[str]
    sbom_vdr_values: NotRequired[dict]
    package_manager_file: NotRequired[str]
    upgrade_threshold: NotRequired[str]
    severity: NotRequired[str]


class ExtractPackageManagerFileOutputs(TypedDict):
    files_to_patch: Iterable[dict]
