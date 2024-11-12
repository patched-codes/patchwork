import json
import shlex
import subprocess
from pathlib import Path

from patchwork.logger import logger
from patchwork.step import Step, StepStatus
from patchwork.steps.CallCommand.typed import CallCommandInputs, CallCommandOutputs


class CallCommand(Step, input_class=CallCommandInputs, output_class=CallCommandOutputs):
    def __init__(self, inputs: dict):
        super().__init__(inputs)
        self.command = inputs["command"]
        self.command_args = inputs.get("command_args", "")
        self.working_dir = inputs.get("working_dir", Path.cwd())
        self.env = self.__parse_env_text(inputs.get("env", ""))

    @staticmethod
    def __parse_env_text(env_text):
        env_spliter = shlex.shlex(env_text, posix=True)
        env_spliter.whitespace_split = True
        env_spliter.whitespace += ";"

        env = dict()
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
        cmd = [self.command, *shlex.split(self.command_args)]
        p = subprocess.run(cmd, capture_output=True, text=True, cwd=self.working_dir, env=self.env)
        try:
            p.check_returncode()
            return dict(stdout_output=p.stdout)
        except subprocess.CalledProcessError as e:
            self.set_status(StepStatus.FAILED, f"`{self.command} {self.command_args}` failed with stdout:\n{p.stdout}\nstderr:\n{e.stderr}")
            return dict()
