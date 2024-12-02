from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __RequiredCallCommandInputs(TypedDict):
    command: str

class CallCommandInputs(__RequiredCallCommandInputs, total=False):
    command_args: str
    working_dir: Annotated[str, StepTypeConfig(is_path=True)]
    env: str


class CallCommandOutputs(TypedDict):
    stdout_output: str
