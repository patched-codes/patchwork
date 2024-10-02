from __future__ import annotations

import os
import subprocess
import tempfile
from pathlib import Path

from patchwork.step import Step, StepStatus

FOLDER_PATH = "folder_path"


class CallCode2Prompt(Step):
    __CUSTOM_GIT_IGNORE = [
        # Compiled source
        "*.com",
        "*.class",
        "*.dll",
        "*.exe",
        "*.o",
        "*.so",
        # Archives
        "*.7z",
        "*.dmg",
        "*.gz",
        "*.iso",
        "*.jar",
        "*.rar",
        "*.tar",
        "*.zip",
        # data stores
        "*.log",
        "*.sql",
        "*.sqlite",
        "*.yml",
        "*.json",
        # OS generated files
        ".DS_Store",
        ".DS_Store?",
        "._*",
        ".Spotlight-V100",
        ".Trashes",
        "ehthumbs.db",
        "Thumbs.db",
        # Test files
        "test",
        "tests",
        "Test",
        "Tests",
        "testing",
        "Testing",
        "*.test.js",
        "*.test.ts",
        "*.test.jsx",
        "*.test.tsx",
        "*.spec.js",
        "*.spec.ts",
        "*.spec.jsx",
        "*.spec.tsx",
        # IDE files
        ".idea",
        ".vscode",
        "*.suo",
        "*.ntvs*",
        "*.njsproj",
        "*.sln",
    ]
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
        self.modes = self.__parse_modes(inputs.get("code2prompt_modes", ""))
        # Check if the file exists
        if not os.path.exists(self.code_file_path):
            # The file does not exist, create it by opening it in append mode and then closing it
            with open(self.code_file_path, "a") as file:
                pass  # No need to write anything, just create the file if it doesn't exist

    @staticmethod
    def __parse_modes(modes: str) -> list[str]:
        return [mode.strip() for mode in modes.split(",") if mode.strip() != ""]

    def __get_cmd_args(self, git_ignore_temp_fp) -> list[str]:
        cmd = [
            "code2prompt",
            "--path",
            self.folder_path,
        ]

        repo_gitignore = self.folder_path / ".gitignore"
        custom_gitignore_text = "\n".join(self.__CUSTOM_GIT_IGNORE)
        if repo_gitignore.is_file():
            custom_gitignore_text = custom_gitignore_text + "\n" + repo_gitignore.read_text()
        git_ignore_temp_fp.write(custom_gitignore_text)
        cmd.extend(["--gitignore", git_ignore_temp_fp.name])

        for mode in self.modes:
            cmd.append(f"--{mode}")

        if self.filter is not None:
            cmd.extend(["--filter", self.filter])

        if self.suppress_comments:
            cmd.append("--suppress-comments")

        return cmd

    def run(self) -> dict:
        try:
            with tempfile.NamedTemporaryFile(mode="w+") as temp_file:
                cmd = self.__get_cmd_args(temp_file)
                p = subprocess.run(cmd, capture_output=True, text=True, check=True)
            prompt_content_md = p.stdout
        except subprocess.CalledProcessError as e:
            self.set_status(StepStatus.FAILED, f"Subprocess failed: {e}")
            return dict()

        return dict(uri=self.code_file_path, fullContent=prompt_content_md)
