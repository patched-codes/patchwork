from __future__ import annotations

import os
import subprocess
from pathlib import Path
from typing import Literal

from patchwork.steps.ResolveIssue.tools.tool import Tool


class BashTool(Tool, tool_name="bash"):
    def __init__(self, path: str):
        super().__init__()
        self.path = Path(path)
        self.modified_files = []

    @property
    def json_schema(self) -> dict:
        return {
            "name": "bash",
            "description": """Run commands in a bash shell

* When invoking this tool, the contents of the "command" parameter does NOT need to be XML-escaped.
* You don't have access to the internet via this tool.
* You do have access to a mirror of common linux and python packages via apt and pip.
* State is persistent across command calls and discussions with the user.
* To inspect a particular line range of a file, e.g. lines 10-25, try 'sed -n 10,25p /path/to/the/file'.
* Please avoid commands that may produce a very large amount of output.
* Please run long lived commands in the background, e.g. 'sleep 10 &' or start a server in the background.""",
            "input_schema": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "The bash command to run."
                    }
                },
                "required": ["command"]
            }
        }

    def execute(
        self,
        command: str | None = None,
        *args,
        **kwargs,
    ) -> str:
        """Execute editor commands on files in the repository."""
        if command is None:
            return f"Error: `command` parameter must be set and cannot be empty"

        try:
            result = subprocess.run(
                command,
                shell=True,
                cwd=self.path,
                capture_output=True,
                text=True,
                timeout=60  # Add timeout for safety
            )
            return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
        except subprocess.TimeoutExpired:
            return "Error: Command timed out after 60 seconds"
        except Exception as e:
            return f"Error: {str(e)}"

    @property
    def tool_records(self):
        return dict(modified_files=[{"path": file} for file in self.modified_files])

    def __get_abs_path(self, path: str):
        abs_path = (self.repo_path / path.lstrip("/")).resolve()
        if not abs_path.is_relative_to(self.repo_path):
            raise ValueError(f"Path {path} contains illegal path traversal")

        return abs_path

    def __view(self, path, view_range):
        abs_path = self.__get_abs_path(path)
        if not abs_path.exists():
            return f"Error: Path {path} does not exist"

        if abs_path.is_file():
            with open(abs_path, "r") as f:
                content = f.read()

            if view_range:
                lines = content.splitlines()
                start, end = view_range
                content = "\n".join(lines[start - 1 : end])
            return content
        elif abs_path.is_dir():
            result = []
            for root, dirs, files in os.walk(abs_path):
                level = root[len(abs_path) :].count(os.sep)
                if level <= 2:
                    for d in dirs:
                        result.append(d)
                    for f in files:
                        result.append(f)
            return "\n".join(result)

    def __create(self, file_text, path):
        abs_path = self.__get_abs_path(path)
        if abs_path.exists():
            return f"Error: File {path} already exists"
        abs_path.parent.mkdir(parents=True, exist_ok=True)
        abs_path.write_text(file_text)
        return f"File created successfully at: {path}"

    def __str_replace(self, new_str, old_str, path):
        abs_path = self.__get_abs_path(path)
        if not abs_path.exists():
            return f"Error: File {path} does not exist"
        if not abs_path.is_file():
            return f"Error: File {path} is not a file"
        content = abs_path.read_text()
        occurrences = content.count(old_str)
        if occurrences != 1:
            return f"Error: Found {occurrences} occurrences of old_str, expected exactly 1"
        new_content = content.replace(old_str, new_str)
        with open(abs_path, "w") as f:
            f.write(new_content)
        return "Replacement successful"

    def __insert(self, insert_line, new_str, path):
        abs_path = self.__get_abs_path(path)
        if not abs_path.is_file():
            return f"Error: File {path} does not exist or is not a file"

        lines = abs_path.read_text().splitlines(keepends=True)
        if insert_line is None or insert_line < 1 or insert_line > len(lines):
            return f"Error: Invalid insert line {insert_line}"

        lines.insert(insert_line, new_str + "\n")
        abs_path.write_text("".join(lines))
        return "Insert successful"
