from __future__ import annotations

import subprocess

from patchwork.logger import logger
from patchwork.step import Step, DataPoint
from patchwork.steps import CallCommand
from patchwork.steps.ScanPSFuzz.typed import ScanPSFuzzInputs, ScanPSFuzzOutputs


class ScanPSFuzz(Step, input_class=ScanPSFuzzInputs, output_class=ScanPSFuzzOutputs):
    def __init__(self, inputs: dict):
        if not self.__is_ps_fuzz_installed():
            raise ValueError("""\
`prompt-security-fuzzer` is not installed. Please install with the following instructions:
1. Install pipx: https://github.com/pypa/pipx
2. pipx install prompt-security-fuzzer
3. pipx inject prompt-security-fuzzer setuptools
""")
        super().__init__(inputs)
        wrapped_input = dict(
            command="prompt-security-fuzzer",
            command_args=f'-b {inputs["prompt_file_path"]}',
            env=f'OPENAI_API_KEY={inputs["openai_api_key"]}'
        )
import os

wrapped_input = dict(
    command="prompt-security-fuzzer",
    command_args=f'-b {inputs["prompt_file_path"]}',
    env=f'OPENAI_API_KEY={os.getenv("OPENAI_API_KEY")}'
)
        working_dir = inputs.get("working_dir")
        if working_dir is not None:
            wrapped_input["working_dir"] = working_dir

        self.inner_step = CallCommand(wrapped_input)

    @staticmethod
    def __is_ps_fuzz_installed():
        try:
            subprocess.run(["prompt-security-fuzzer", "-h"], capture_output=True, check=True)
            return True
        except subprocess.CalledProcessError as e:
            err = e
        except FileNotFoundError as e:
            err = e
        # If the command fails, prompt-security-fuzzer is not installed
        logger.info(f"prompt-security-fuzzer is not installed: {err}")
        return False

    def run(self) -> DataPoint:
        rv = self.inner_step.run()
        self.set_status(self.inner_step.status, self.inner_step.status_message)
        return rv
