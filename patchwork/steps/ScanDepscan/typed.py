from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class ScanDepscanInputs(TypedDict, total=False):
    language: Annotated[str, IS_CONFIG]


class ScanDepscanOutputs(TypedDict):
    sbom_vdr_values: dict
