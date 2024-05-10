import json
import subprocess
from pathlib import Path

from patchwork.logger import logger
from patchwork.step import Step


class ScanSemgrep(Step):
    def __init__(self, inputs: dict):
        logger.info(f"Run started {self.__class__.__name__}")
        self.extra_args = inputs.get("semgrep_extra_args", "")
        self.sarif_file_path = inputs.get("sarif_file_path")
        self.sarif_values = inputs.get("sarif_values")
        self.enabled = (self.sarif_file_path or self.sarif_values) is not None

    def run(self) -> dict:
        if not self.enabled:
            logger.info(
                f"Run skipped {self.__class__.__name__} "
                f"because sarif_file_path or sarif_values is already present in inputs"
            )
            sarif_values = self.sarif_values
            if self.sarif_file_path:
                with open(self.sarif_file_path) as f:
                    sarif_values = json.load(f)
            return dict(sarif_values=sarif_values)

        cwd = Path.cwd()

        cmd = [
            "semgrep",
            *self.extra_args.split(),
            str(cwd),
            "--sarif",
        ]

        p = subprocess.run(cmd, capture_output=True, text=True)
        sarif_values = json.loads(p.stdout)

        logger.info(f"Run completed {self.__class__.__name__}")
        return dict(sarif_values=sarif_values)
