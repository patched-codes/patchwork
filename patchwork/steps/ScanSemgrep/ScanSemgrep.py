import subprocess
import tempfile
from pathlib import Path

from patchwork.logger import logger
from patchwork.step import Step


class ScanSemgrep(Step):
    def __init__(self, inputs: dict):
        logger.info(f"Run started {self.__class__.__name__}")
        self.extra_args = inputs.get("semgrep_extra_args", "")
        self.enabled = "sarif_file_path" not in inputs.keys()

    def run(self) -> dict:
        if not self.enabled:
            logger.info(f"Run skipped {self.__class__.__name__} because sarif_file_path is already present in inputs")
            return dict()

        cwd = Path.cwd()
        sarif_file_path = Path(tempfile.mktemp(".sarif"))

        cmd = [
            "semgrep",
            self.extra_args.split(),
            str(cwd),
            "--sarif",
        ]

        p = subprocess.run(cmd, capture_output=True, text=True)

        with open(sarif_file_path, "w") as file:
            file.write(p.stdout)

        logger.info(f"Run completed {self.__class__.__name__}")
        return {"sarif_file_path": sarif_file_path}
