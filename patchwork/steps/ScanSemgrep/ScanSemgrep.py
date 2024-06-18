import json
import subprocess
from pathlib import Path

from patchwork.common.utils.dependency import import_with_dependency_group
from patchwork.logger import logger
from patchwork.step import Step


class ScanSemgrep(Step):
    def __init__(self, inputs: dict):
        logger.info(f"Run started {self.__class__.__name__}")

        self.extra_args = inputs.get("semgrep_extra_args", "")
        sarif_file_path = inputs.get("sarif_file_path")
        if sarif_file_path is not None:
            sarif_file_path = Path(sarif_file_path)
            if not sarif_file_path.is_file():
                raise ValueError(f'Unable to find input file: "{sarif_file_path}"')
            with open(sarif_file_path, "r") as fp:
                self.sarif_values = json.load(fp)
        elif inputs.get("sarif_values") is not None:
            self.sarif_values = inputs.get("sarif_values")
        else:
            self.sarif_values = None

    def run(self) -> dict:
        if self.sarif_values is not None:
            return dict(sarif_values=self.sarif_values)

        import_with_dependency_group("semgrep")
        cwd = Path.cwd()

        cmd = [
            "semgrep",
            *self.extra_args.split(),
            str(cwd),
            "--sarif",
        ]

        p = subprocess.run(cmd, capture_output=True, text=True)
        try:
            sarif_values = json.loads(p.stdout)
        except json.JSONDecodeError as e:
            logger.debug(f"Error parsing semgrep output: {p.stdout}", e)
            raise ValueError("Error parsing semgrep output")

        logger.info(f"Run completed {self.__class__.__name__}")
        return dict(sarif_values=sarif_values)
