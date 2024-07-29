from pydantic import BaseModel
from typing_extensions import Annotated, Dict, List, Optional

from patchwork.common.utils.step_typing import StepTypeConfig


class ExtractPackageManagerFileInputs(BaseModel):
    sbom_vdr_file_path: Optional[Annotated[str, StepTypeConfig(is_config=True, is_path=True)]] = None
    sbom_vdr_values: Optional[dict] = None
    package_manager_file: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    upgrade_threshold: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    severity: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None


class ExtractPackageManagerFileOutputs(BaseModel):
    files_to_patch: List[Dict]
