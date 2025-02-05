from __future__ import annotations

import os
import shlex
import subprocess
from pathlib import Path

from patchwork.common.utils.utils import mustache_render
from patchwork.logger import logger
from patchwork.step import Step, StepStatus
from patchwork.steps.CallShell.typed import CallShellInputs, CallShellOutputs


class CallShell(Step, input_class=CallShellInputs, output_class=CallShellOutputs):
    def __init__(self, inputs: dict):
        super().__init__(inputs)
        script_template_values = inputs.get("script_template_values", {})
        self.script = mustache_render(inputs["script"], script_template_values)
        self.working_dir = inputs.get("working_dir", Path.cwd())
        self.env = self.__parse_env_text(inputs.get("env", ""))

    @staticmethod
    def __parse_env_text(env_text: str) -> dict[str, str]:
        env_spliter = shlex.shlex(env_text, posix=True)
        env_spliter.whitespace_split = True
        env_spliter.whitespace += ";"

        env: dict[str, str] = os.environ.copy()
        for env_assign in env_spliter:
            env_assign_spliter = shlex.shlex(env_assign, posix=True)
            env_assign_spliter.whitespace_split = True
            env_assign_spliter.whitespace += "="
            env_parts = list(env_assign_spliter)
            if len(env_parts) < 1:
                continue

            env_assign_target = env_parts[0]
            if len(env_parts) < 2:
                logger.error(f"{env_assign_target} is not assigned anything, skipping...")
                continue
            if len(env_parts) > 2:
                logger.error(f"{env_assign_target} has more than 1 assignment, skipping...")
                continue
            env[env_assign_target] = env_parts[1]

        return env

    def run(self) -> dict:
        p = subprocess.run(self.script, shell=True, capture_output=True, text=True, cwd=self.working_dir, env=self.env)
        try:
            p.check_returncode()
        except subprocess.CalledProcessError as e:
            self.set_status(
                StepStatus.FAILED,
                f"Script failed.",
            )
        logger.info(f"stdout: \n{p.stdout}")
        logger.info(f"stderr:\n{p.stderr}")
        return dict(stdout_output=p.stdout, stderr_output=p.stderr)
