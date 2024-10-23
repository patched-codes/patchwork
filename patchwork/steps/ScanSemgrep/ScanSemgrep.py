import json
import subprocess
from pathlib import Path

from patchwork.common.utils.dependency import import_with_dependency_group
from patchwork.common.utils.input_parsing import parse_to_list
from patchwork.logger import logger
from patchwork.step import Step, StepStatus
from patchwork.steps.ScanSemgrep.typed import ScanSemgrepInputs, ScanSemgrepOutputs


class ScanSemgrep(Step, input_class=ScanSemgrepInputs, output_class=ScanSemgrepOutputs):
    def __init__(self, inputs: dict):
        super().__init__(inputs)

        self.extra_args = inputs.get("semgrep_extra_args", "")
        sarif_file_path = inputs.get("sarif_file_path")
        if sarif_file_path is not None:
            sarif_file_path = Path(sarif_file_path)
            if not sarif_file_path.is_file():
                raise ValueError(f'Unable to find input file: "{sarif_file_path}"')
            with open(sarif_file_path, "r") as fp:
                self.sarif_values = json.load(fp, strict=False)
        elif inputs.get("sarif_values") is not None:
            sarif_values = inputs.get("sarif_values")
            if isinstance(sarif_values, str):
                sarif_values = json.loads(sarif_values, strict=False)
            self.sarif_values = sarif_values
        else:
            self.sarif_values = None

        path_key = inputs.get("path_key", "path")
        self.paths = parse_to_list(inputs.get("paths", ""), possible_delimiters=[",", None], possible_keys=[path_key])

    def run(self) -> dict:
        if self.sarif_values is not None:
            self.set_status(StepStatus.SKIPPED, "Using provided SARIF")
            return dict(sarif_values=self.sarif_values)

        import_with_dependency_group("semgrep")
        cwd = Path.cwd()

        cmd = [
            "semgrep",
            "scan",
            *self.paths,
            *self.extra_args.split(),
            "--sarif",
        ]

        p = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
        try:
            sarif_values = json.loads(p.stdout)
            return dict(sarif_values=sarif_values)
        except json.JSONDecodeError as e:
            logger.debug(f"Error parsing semgrep output: {p.stdout}", e)
            self.set_status(StepStatus.FAILED, f"Error parsing semgrep output")
