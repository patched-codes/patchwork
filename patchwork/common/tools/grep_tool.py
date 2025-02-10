from __future__ import annotations

import fnmatch
import itertools
import os
from pathlib import Path

from typing_extensions import Optional

from patchwork.common.tools.tool import Tool


class FindTool(Tool, tool_name="find_files"):
    def __init__(self, path: Path | str, **kwargs):
        self.__working_dir = Path(path).resolve()

    @property
    def json_schema(self) -> dict:
        return {
            "name": "find_files",
            "description": f"""\
Tool to find files in {self.__working_dir} using a pattern based on the Unix shell style.
Unix shell style:
    *       matches everything
    ?       matches any single character
    [seq]   matches any character in seq
    [!seq]  matches any char not in seq

""",
            "input_schema": {
                "type": "object",
                "properties": {
                    "pattern": {
                        "description": """\
The Unix shell style pattern to match files using.

Unix shell style:
    *       matches everything
    ?       matches any single character
    [seq]   matches any character in seq
    [!seq]  matches any char not in seq

Example:
* '*macs' will match the file '.emacs'
* '*.py' will match all files with the '.py' extension
""",
                        "type": "string",
                    },
                    "depth": {
                        "description": "The maximum depth files in directories to look for. Default is 1.",
                        "type": "integer",
                    },
                    "is_case_sensitive": {
                        "description": "Whether the pattern should be case-sensitive.",
                        "type": "boolean",
                    },
                },
                "required": ["pattern"],
            },
        }

    def __is_dot(self, path: Path | str) -> bool:
        return any(part.startswith(".") for part in path.relative_to(self.__working_dir).parts)

    def execute(self, pattern: Optional[str] = None, depth: int = 1, is_case_sensitive: bool = False) -> str:
        if pattern is None:
            raise ValueError("Pattern argument is required!")

        matcher = fnmatch.fnmatch
        if is_case_sensitive:
            matcher = fnmatch.fnmatchcase

        file_matches = []
        dir_matches = []
        for root, dirs, files in os.walk(self.__working_dir):
            root_path = Path(root)
            if len(root_path.resolve().relative_to(self.__working_dir).parts) > depth:
                continue

            for file in itertools.chain(dirs, files):
                file_path = root_path / file
                if self.__is_dot(file_path):
                    continue

                if file_path.is_file():
                    list_to_append = file_matches
                else:
                    list_to_append = dir_matches

                if matcher(str(file_path), pattern):
                    relative_file_path = file_path.relative_to(self.__working_dir)
                    list_to_append.append(str(relative_file_path))

        delim = "\n  * "
        files_part = (delim + delim.join(file_matches)) if len(file_matches) > 0 else "\n  No files found"
        dirs_part = (delim + delim.join(dir_matches)) if len(dir_matches) > 0 else "\n  No directories found"
        return f"""\
Files:{files_part}

Directories:{dirs_part}

"""


class FindTextTool(Tool, tool_name="find_text"):
    __CHAR_LIMIT = 200
    __CHAR_LIMIT_TEXT = "<Too many characters>"

    def __init__(self, path: Path | str, **kwargs):
        self.__working_dir = Path(path).resolve()

    @property
    def json_schema(self) -> dict:
        return {
            "name": "find_text",
            "description": f"""\
Tool to find text in a file using a pattern based on the Unix shell style.
The current working directory is always {self.__working_dir}. 
The path provided should either be absolute or relative to the current working directory.

This tool will match each line of the file with the provided pattern and prints the line number and the line content.
If the line contains more than {self.__CHAR_LIMIT} characters, the line content will be replaced with {self.__CHAR_LIMIT_TEXT}.
""",
            "input_schema": {
                "type": "object",
                "properties": {
                    "path": {
                        "description": "The path to the file to find text in.",
                        "type": "string",
                    },
                    "pattern": {
                        "description": """\
The Unix shell style pattern to match files using.

Unix shell style:
    *       matches everything
    ?       matches any single character
    [seq]   matches any character in seq
    [!seq]  matches any char not in seq

Example:
* '*macs' will match the file '.emacs'
* '*.py' will match all files with the '.py' extension
""",
                        "type": "string",
                    },
                    "is_case_sensitive": {
                        "description": "Whether the pattern should be case-sensitive.",
                        "type": "boolean",
                    },
                },
                "required": ["path", "pattern"],
            },
        }

    def execute(
        self,
        path: Optional[Path] = None,
        pattern: Optional[str] = None,
        is_case_sensitive: bool = False,
    ) -> str:
        if path is None:
            raise ValueError("Path argument is required!")

        if pattern is None:
            raise ValueError("pattern argument is required!")

        matcher = fnmatch.fnmatch
        if is_case_sensitive:
            matcher = fnmatch.fnmatchcase

        path = Path(path).resolve()
        if not path.is_relative_to(self.__working_dir):
            raise ValueError("Path must be relative to working dir")

        matches = []
        with path.open("r") as f:
            for i, line in enumerate(f.readlines()):
                if not matcher(line, pattern):
                    continue

                content = f"Line {i + 1}: {line}"
                if len(line) > self.__CHAR_LIMIT:
                    content = f"Line {i + 1}: {self.__CHAR_LIMIT_TEXT}"

                matches.append(content)
        return f"Pattern matches found in '{path}':\n" + "\n".join(matches)
