from __future__ import annotations

from pathlib import Path

from typing_extensions import Literal, Optional, Union

from patchwork.common.tools.tool import Tool
from patchwork.common.utils.utils import detect_newline


class FileViewTool(Tool, tool_name="file_view"):
    __TRUNCATION_TOKEN = "<TRUNCATED>"
    __VIEW_LIMIT = 3000

    def __init__(self, path: Union[Path, str]):
        super().__init__()
        self.repo_path = Path(path).resolve()

    @property
    def json_schema(self) -> dict:
        return {
            "name": "file_view",
            "description": f"""\
Custom tool for viewing files
    
* If `path` is a file, `view` displays the result of applying `cat -n` up to {self.__VIEW_LIMIT} characters. If `path` is a directory, `view` lists non-hidden files and directories.
* The output is too lone, it will be truncated and marked with `{self.__TRUNCATION_TOKEN}`
* The working directory is always {self.repo_path}
""",
            "input_schema": {
                "type": "object",
                "properties": {
                    "path": {
                        "description": "Absolute path to file or directory, e.g. `/repo/file.py` or `/repo`.",
                        "type": "string",
                    },
                    "view_range": {
                        "description": "Optional parameter when `path` points to a file. If none is given, the full file is shown. If provided, the file will be shown in the indicated line number range, e.g. [11, 12] will show lines 11 and 12. Indexing at 1 to start. Setting `[start_line, -1]` shows all lines from `start_line` to the end of the file.",
                        "items": {"type": "integer"},
                        "type": "array",
                    },
                },
                "required": ["path"],
            },
        }

    def __get_abs_path(self, path: str):
        wanted_path = Path(path)
        if not Path(path).is_absolute():
            wanted_path = self.repo_path / path
        if wanted_path.is_relative_to(self.repo_path):
            return wanted_path
        else:
            raise ValueError(f"Path {path} contains illegal path traversal")

    def execute(self, path: str, view_range: Optional[list[int]] = None) -> str:
        abs_path = self.__get_abs_path(path)
        if not abs_path.exists():
            return f"Error: Path {abs_path} does not exist"

        if abs_path.is_file():
            try:
                with open(abs_path, "r") as f:
                    content = f.read()

                if view_range:
                    lines = content.splitlines()
                    start, end = view_range
                    content = "\n".join(lines[start - 1 : end])
            except Exception as e:
                content = "Error: " + str(e)

            if len(content) > self.__VIEW_LIMIT:
                content = content[: self.__VIEW_LIMIT] + self.__TRUNCATION_TOKEN
            return content
        elif abs_path.is_dir():
            directories = []
            files = []
            for file in abs_path.iterdir():
                directories.append(file.name) if file.is_dir() else files.append(file.name)

            rv = ""
            if len(directories) > 0:
                rv += "Directories: \n"
                rv += "\n".join(directories)
                rv += "\n"

            if len(files) > 0:
                rv += "Files: \n"
                rv += "\n".join(files)

            return rv


class CodeEditTool(Tool, tool_name="code_edit_tool"):
    def __init__(self, path: Union[Path, str]):
        super().__init__()
        self.repo_path = Path(path).resolve()
        self.modified_files = set()

    @property
    def json_schema(self) -> dict:
        return {
            "name": "code_edit_tool",
            "description": f"""\
Custom editing tool for viewing, creating and editing files

* State is persistent across command calls and discussions with the user
* The `create` command cannot be used if the specified `path` already exists as a file
* The working directory is always {self.repo_path}

Notes for using the `str_replace` command:
* The `old_str` parameter should match EXACTLY one or more consecutive lines from the original file. Be mindful of whitespaces!
* If the `old_str` parameter is not unique in the file, the replacement will not be performed. Make sure to include enough context in `old_str` to make it unique
* The `new_str` parameter should contain the edited lines that should replace the `old_str`""",
            "input_schema": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "enum": ["create", "str_replace", "insert"],
                        "description": "The commands to run. Allowed options are: `create`, `str_replace`, `insert`.",
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
                },
                "required": ["command", "path"],
            },
        }

    def execute(
        self,
        command: Optional[Literal["create", "str_replace", "insert"]] = None,
        file_text: str = "",
        insert_line: Optional[int] = None,
        new_str: str = "",
        old_str: Optional[str] = None,
        path: Optional[str] = None,
    ) -> str:
        """Execute editor commands on files in the repository."""
        required_dict = dict(command=command, path=path)
        missing_required = {k for k, v in required_dict.items() if v is None}
        if len(missing_required) > 0:
            return f"Error: `{'` and `'.join(missing_required)}` parameters must be set and cannot be empty"

        try:
            abs_path = self.__get_abs_path(path)
            if command == "create":
                result = self.__create(file_text, abs_path)
            elif command == "str_replace":
                result = self.__str_replace(new_str, old_str, abs_path)
            elif command == "insert":
                result = self.__insert(insert_line, new_str, abs_path)
            else:
                return f"Error: Unknown action {command}"
        except Exception as e:
            return f"Error: {str(e)}"

        self.modified_files.update({abs_path})
        return result

    @property
    def tool_records(self):
        return dict(modified_files=[file for file in self.modified_files])

    def __get_abs_path(self, path: str):
        wanted_path = Path(path).resolve()
        if wanted_path.is_relative_to(self.repo_path):
            return wanted_path
        else:
            raise ValueError(f"Path {path} contains illegal path traversal")

    def __create(self, file_text, abs_path):
        if abs_path.exists():
            return f"Error: File {abs_path} already exists"
        abs_path.parent.mkdir(parents=True, exist_ok=True)
        abs_path.write_text(file_text)
        return f"File created successfully at: {abs_path}"

    def __str_replace(self, new_str, old_str, abs_path):
        if not abs_path.exists():
            return f"Error: File {abs_path} does not exist"
        if not abs_path.is_file():
            return f"Error: File {abs_path} is not a file"
        content = abs_path.read_text()
        occurrences = content.count(old_str)
        if occurrences != 1:
            return f"Error: Found {occurrences} occurrences of old_str, expected exactly 1"
        new_content = content.replace(old_str, new_str)
        newline = detect_newline(abs_path)
        with abs_path.open("w", newline=newline) as fp:
            fp.write(new_content)
        return "Replacement successful"

    def __insert(self, insert_line, new_str, abs_path):
        if not abs_path.is_file():
            return f"Error: File {abs_path} does not exist or is not a file"

        lines = abs_path.read_text().splitlines(keepends=True)
        if insert_line is None or insert_line < 1 or insert_line > len(lines):
            return f"Error: Invalid insert line {insert_line}"

        lines.insert(insert_line, new_str + "\n")
        newline = detect_newline(abs_path)
        with abs_path.open("w", newline=newline) as fp:
            fp.write("".join(lines))
        return "Insert successful"
