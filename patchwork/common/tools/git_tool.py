from __future__ import annotations

import os
import subprocess

from patchwork.common.tools.tool import Tool


class GitTool(Tool, tool_name="git_tool",  abc_register=False):
    def __init__(self, path: str):
        super().__init__()
        self.path = path

    @property
    def json_schema(self) -> dict:
        return {
            "name": "git_tool",
            "description": """\
Access to the Git CLI, the command is also `git` all args provided are used as is.
""",
            "input_schema": {
                "type": "object",
                "properties": {
                    "args": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": """
The args to run `git` command with. 
E.g. 
[\"commit\", \"-m\", \"A commit message\"] to commit changes with a commit message.
[\"add\", \".\"] to stage all changed files.
""",
                    }
                },
                "required": ["args"],
            },
        }

    def execute(self, args: list[str]) -> str:
        env = os.environ.copy()
        p = subprocess.run(
            ["git", *args],
            env=env,
            cwd=self.path,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        return p.stdout
