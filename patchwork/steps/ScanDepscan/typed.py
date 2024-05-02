from typing_extensions import NotRequired, TypedDict


class ScanDepscanInputs(TypedDict):
    language: NotRequired[str]


class ScanDepscanOutputs(TypedDict):
    sbom_vdr_file_path: str
