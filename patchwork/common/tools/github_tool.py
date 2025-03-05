from __future__ import annotations

import os
import subprocess

from patchwork.common.tools.tool import Tool


class GitHubTool(Tool, tool_name="github_tool"):
    def __init__(self, path: str, gh_token: str):
        super().__init__()
        self.path = path
        self.gh_token = gh_token

    @property
    def json_schema(self) -> dict:
        return {
            "name": "github_tool",
            "description": """\
Access to the GitHub CLI, the command is also `gh` all args provided are used as is
""",
            "input_schema": {
                "type": "object",
                "properties": {
                    "args": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "The args to run `gh` command with.",
                    }
                },
                "required": ["args"],
            },
        }

    def execute(self, args: list[str]) -> str:
        env = os.environ.copy()
        env["GH_TOKEN"] = self.gh_token
        p = subprocess.run(
            ["gh", *args],
            env=env,
            cwd=self.path,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        return p.stdout
