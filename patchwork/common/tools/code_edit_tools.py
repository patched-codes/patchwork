from __future__ import annotations

import os
from pathlib import Path
from typing import Literal

from patchwork.common.tools.tool import Tool


class CodeEditTool(Tool, tool_name="code_edit_tool"):
    def __init__(self, path: str):
        super().__init__()
        self.repo_path = Path(path)
        self.modified_files = set()

    @property
    def json_schema(self) -> dict:
        return {
            "name": "code_edit_tool",
            "description": """Custom editing tool for viewing, creating and editing files

* State is persistent across command calls and discussions with the user
* If `path` is a file, `view` displays the result of applying `cat -n`. If `path` is a directory, `view` lists non-hidden files and directories up to 2 levels deep
* The `create` command cannot be used if the specified `path` already exists as a file
* If a `command` generates a long output, it will be truncated and marked with `<response clipped>`
* The `undo_edit` command will revert the last edit made to the file at `path`

Notes for using the `str_replace` command:
* The `old_str` parameter should match EXACTLY one or more consecutive lines from the original file. Be mindful of whitespaces!
* If the `old_str` parameter is not unique in the file, the replacement will not be performed. Make sure to include enough context in `old_str` to make it unique
* The `new_str` parameter should contain the edited lines that should replace the `old_str`""",
            "input_schema": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "enum": ["view", "create", "str_replace", "insert", "undo_edit"],
                        "description": "The commands to run. Allowed options are: `view`, `create`, `str_replace`, `insert`, `undo_edit`.",
                    },
                    "file_text": {
                        "description": "Required parameter of `create` command, with the content of the file to be created.",
                        "type": "string",
                    },
                    "insert_line": {
                        "description": "Required parameter of `insert` command. The `new_str` will be inserted AFTER the line `insert_line` of `path`.",
                        "type": "integer",
                    },
                    "new_str": {
                        "description": "Required parameter of `str_replace` command containing the new string. Required parameter of `insert` command containing the string to insert.",
                        "type": "string",
                    },
                    "old_str": {
                        "description": "Required parameter of `str_replace` command containing the string in `path` to replace.",
                        "type": "string",
                    },
                    "path": {
                        "description": "Absolute path to file or directory, e.g. `/repo/file.py` or `/repo`.",
                        "type": "string",
                    },
                    "view_range": {
                        "description": "Optional parameter of `view` command when `path` points to a file. If none is given, the full file is shown. If provided, the file will be shown in the indicated line number range, e.g. [11, 12] will show lines 11 and 12. Indexing at 1 to start. Setting `[start_line, -1]` shows all lines from `start_line` to the end of the file.",
                        "items": {"type": "integer"},
                        "type": "array",
                    },
                },
                "required": ["command", "path"],
            },
        }

    def execute(
        self,
        command: Literal["view", "create", "str_replace", "insert"] | None = None,
        file_text: str = "",
        insert_line: int | None = None,
        new_str: str = "",
        old_str: str | None = None,
        path: str | None = None,
        view_range: list[int] | None = None,
        *args,
        **kwargs,
    ) -> str:
        """Execute editor commands on files in the repository."""
        required_dict = dict(command=command, path=path)
        missing_required = {k for k, v in required_dict.items() if v is None}
        if len(missing_required) > 0:
            return f"Error: `{'` and `'.join(missing_required)}` parameters must be set and cannot be empty"

        try:
            if command == "view":
                result = self.__view(path, view_range)
            elif command == "create":
                result = self.__create(file_text, path)
            elif command == "str_replace":
                result = self.__str_replace(new_str, old_str, path)
            elif command == "insert":
                result = self.__insert(insert_line, new_str, path)
            else:
                return f"Error: Unknown action {command}"

            if command in {"create", "str_replace", "insert"}:
                self.modified_files.update({path.lstrip("/")})

            return result

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
                level = root[len(str(abs_path)) :].count(os.sep)
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
