import os
import subprocess
from pathlib import Path

from patchwork.logger import logger
from patchwork.step import Step, StepStatus

FOLDER_PATH = "folder_path"


class CallCode2Prompt(Step):
    required_keys = {FOLDER_PATH}

    def __init__(self, inputs: dict):
        super().__init__(inputs)
        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.folder_path = Path(inputs[FOLDER_PATH])
        if not self.folder_path.is_dir():
            raise ValueError(f"Folder path does not exist: {self.folder_path}")
        self.filter = inputs.get("filter", None)
        self.suppress_comments = inputs.get("suppress_comments", False)
        self.markdown_file_name = inputs.get("markdown_file_name", "README.md")
        self.code_file_path = str(Path(self.folder_path) / self.markdown_file_name)
        # Check if the file exists
        if not os.path.exists(self.code_file_path):
            # The file does not exist, create it by opening it in append mode and then closing it
            with open(self.code_file_path, "a") as file:
                pass  # No need to write anything, just create the file if it doesn't exist

    def run(self) -> dict:
        cmd = [
            "code2prompt",
            "--path",
            self.folder_path,
        ]

        if self.filter is not None:
            cmd.extend(["--filter", self.filter])

        if self.suppress_comments:
            cmd.append("--suppress-comments")

        try:
            p = subprocess.run(cmd, capture_output=True, text=True, check=True)
            prompt_content_md = p.stdout
        except subprocess.CalledProcessError as e:
            self.set_status(StepStatus.FAILED, f"Subprocess failed: {e}")
            return dict(files_to_patch=[])

        # Attempt to read the documentation's current content
        try:
            with open(self.code_file_path, "r") as file:
                file_content = file.read()
        except FileNotFoundError:
            logger.info(f"Unable to find file: {self.code_file_path}")
            return dict(files_to_patch=[
                dict(uri=self.code_file_path, fullContent=prompt_content_md)
            ])

        lines = file_content.splitlines(keepends=True)

        return dict(
            files_to_patch=[
                dict(uri=self.code_file_path, startLine=0, endLine=len(lines), fullContent=prompt_content_md)
            ]
        )
