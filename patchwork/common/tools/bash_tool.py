from __future__ import annotations

import subprocess
from pathlib import Path

from typing_extensions import Optional

from patchwork.common.tools.tool import Tool


class BashTool(Tool, tool_name="bash"):
    def __init__(self, path: Path):
        super().__init__()
        self.path = Path(path)
        self.modified_files = []

    @property
    def json_schema(self) -> dict:
        return {
            "name": "bash",
            "description": f"""Run commands in a bash shell

* When invoking this tool, the contents of the "command" parameter does NOT need to be XML-escaped.
* You don't have access to the internet via this tool.
* You do have access to a mirror of common linux and python packages via apt and pip.
* State is persistent across command calls and discussions with the user.
* To inspect a particular line range of a file, e.g. lines 10-25, try 'sed -n 10,25p /path/to/the/file'.
* Please avoid commands that may produce a very large amount of output.
* Please run long lived commands in the background, e.g. 'sleep 10 &' or start a server in the background.
* The working directory is always {self.path}""",
            "input_schema": {
                "type": "object",
                "properties": {"command": {"type": "string", "description": "The bash command to run."}},
                "required": ["command"],
            },
        }

    def execute(
        self,
        command: Optional[str] = None,
    ) -> str:
        """Execute editor commands on files in the repository."""
        if command is None:
            return f"Error: `command` parameter must be set and cannot be empty"

        try:
            result = subprocess.run(
                command, shell=True, cwd=self.path, capture_output=True, text=True, timeout=60  # Add timeout for safety
            )
            return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
        except subprocess.TimeoutExpired:
            return "Error: Command timed out after 60 seconds"
        except Exception as e:
            return f"Error: {str(e)}"
