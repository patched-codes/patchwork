from typing_extensions import Annotated, Dict, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class ExtractPackageManagerFileInputs(TypedDict, total=False):
    sbom_vdr_file_path: Annotated[str, StepTypeConfig(is_config=True, is_path=True, or_op=["sbom_vdr_values"])]
    sbom_vdr_values: Annotated[Dict, StepTypeConfig(or_op=["sbom_vdr_file_path"])]
    package_manager_file: Annotated[str, StepTypeConfig(is_config=True)]
    upgrade_threshold: Annotated[str, StepTypeConfig(is_config=True)]
    severity: Annotated[str, StepTypeConfig(is_config=True)]


class ExtractPackageManagerFileOutputs(TypedDict):
    files_to_patch: List[Dict]
