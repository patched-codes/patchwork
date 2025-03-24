from typing_extensions import Any, Union

from patchwork.common.tools import Tool
from patchwork.steps import CallSQL


class DatabaseQueryTool(Tool, tool_name="db_query_tool"):
    def __init__(self, inputs: dict[str, Any]):
        super().__init__()
        self.db_settings = inputs.copy()

    @property
    def json_schema(self) -> dict:
        return {
            "name": "db_query_tool",
            "description": """\
Run SQL Query on current database.
""",
            "input_schema": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Database query to run.",
                    }
                },
                "required": ["query"],
            },
        }

    def execute(self, query: str) -> Union[list[dict[str, Any]], str]:
        db_settings = self.db_settings.copy()
        db_settings["db_query"] = query
        try:
            return CallSQL(db_settings).run().get("results", [])
        except Exception as e:
            return str(e)
