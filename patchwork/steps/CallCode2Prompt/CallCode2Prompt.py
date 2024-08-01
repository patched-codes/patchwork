import os
import subprocess
from pathlib import Path

from patchwork.logger import logger
from patchwork.step import Step

FOLDER_PATH = "folder_path"


class CallCode2Prompt(Step):
    required_keys = {FOLDER_PATH}

    def __init__(self, inputs: dict):
        logger.info(f"Run started {self.__class__.__name__}")

        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.folder_path = inputs[FOLDER_PATH]
        self.filter = inputs.get("filter", None)
        self.suppress_comments = inputs.get("suppress_comments", False)
        self.markdown_file_name = inputs.get("markdown_file_name", "README.md")
        self.code_file_path = str(Path(self.folder_path) / self.markdown_file_name)
        # Check if the file exists
        if not os.path.exists(self.code_file_path):
            # The file does not exist, create it by opening it in append mode and then closing it
            with open(self.code_file_path, "a") as file:
                pass  # No need to write anything, just create the file if it doesn't exist

        # Prepare for data extraction
        self.extracted_data = []

    def run(self) -> dict:
        cmd = [
            "code2prompt",
            "--path",
            self.folder_path,
        ]

        if self.filter is not None:
            cmd.append("--filter")
            cmd.append(self.filter)

        if self.suppress_comments:
            cmd.append("--suppress-comments")

        p = subprocess.run(cmd, capture_output=True, text=True)

        prompt_content_md = p.stdout

        # Attempt to read the documentation's current content
        try:
            with open(self.code_file_path, "r") as file:
                file_content = file.read()
        except FileNotFoundError:
            logger.info(f"Unable to find file: {self.code_file_path}")

        lines = file_content.splitlines(keepends=True)

        self.extracted_data.append(
            dict(uri=self.code_file_path, startLine=0, endLine=len(lines), fullContent=prompt_content_md)
        )

        logger.info(f"Run completed {self.__class__.__name__}")
        return dict(files_to_patch=self.extracted_data)
