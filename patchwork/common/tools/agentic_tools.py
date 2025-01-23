from __future__ import annotations

from patchwork.common.tools.tool import Tool


class EndTool(Tool, tool_name="end", abc_register=False):
    MESSAGE = "Ended"

    def __init__(self):
        super().__init__()

    @property
    def json_schema(self) -> dict:
        return {
            "name": "end",
            "description": "End the conversation. Call this when you are done with the conversation.",
            "input_schema": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        }

    def execute(self, *args, **kwargs) -> str:
        return self.MESSAGE
