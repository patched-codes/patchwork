from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __RequiredScanPSFuzzInputs(TypedDict):
    prompt_file_path:  Annotated[str, StepTypeConfig(is_path=True)]
    openai_api_key: Annotated[str, StepTypeConfig(is_config=True)]

class ScanPSFuzzInputs(__RequiredScanPSFuzzInputs, total=False):
    working_dir: Annotated[str, StepTypeConfig(is_path=True)]


class ScanPSFuzzOutputs(TypedDict):
    stdout_output: str
