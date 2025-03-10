from __future__ import annotations

import sqlite3
import subprocess
from pathlib import Path

import pandas
from sqlalchemy import URL
from typing_extensions import Optional

from patchwork.common.tools.tool import Tool


class In2CSVTool(Tool, tool_name="in2csv_tool", auto_register=False):
    def __init__(self, path: str):
        super().__init__()
        self.path = path

    @property
    def json_schema(self) -> dict:
        return {
            "name": "in2csv_tool",
            "description": """\
Convert common tabular data formats to CSV.

optional arguments:
  --reset-dimensions    Ignore the sheet dimensions provided by the XLSX file.
  --encoding-xls ENCODING_XLS
                        Specify the encoding of the input XLS file.
  -y SNIFF_LIMIT, --snifflimit SNIFF_LIMIT
                        Limit CSV dialect sniffing to the specified number of
                        bytes. Specify "0" to disable sniffing entirely, or
                        "-1" to sniff the entire file.
  -I, --no-inference    Disable type inference (and --locale, --date-format,
                        --datetime-format, --no-leading-zeroes) when parsing
                        CSV input.
""",
            "input_schema": {
                "type": "object",
                "properties": {
                    "files": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "The CSV file(s) to operate on",
                    },
                    "args": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "The args to run with",
                    },
                },
                "required": ["files"],
            },
        }

    def execute(self, files: list[str], args: Optional[list[str]] = None) -> str:
        args = args or []

        original_csvs = set()
        for p in Path(self.path).iterdir():
            if p.suffix == ".csv":
                original_csvs.add(p.name)

        p = subprocess.run(
            ["in2csv", *files, *args, "--write-sheets", "-", "--use-sheet-names"],
            capture_output=True,
            text=True,
            cwd=self.path,
        )
        if p.returncode != 0:
            return "ERROR:\n" + p.stderr

        rv = "Files converted to CSV:"
        for p in Path(self.path).iterdir():
            if p.suffix == ".csv" and p.name not in original_csvs:
                rv += f"\n* {p}"

        return rv


class CSVSQLTool(Tool, tool_name="csvsql_tool", auto_register=False):
    def __init__(self, path: str, tmp_path: str):
        super().__init__()
        self.path = path
        self.tmp_path = tmp_path

    @property
    def json_schema(self) -> dict:
        return {
            "name": "csvsql_tool",
            "description": """\
Execute SQL query directly on csv files. The name of the csv files can be referenced as table in the SQL query

If the output is larger than 5000 characters, the remaining characters are replaced with <TRUNCATED>.
""",
            "input_schema": {
                "type": "object",
                "properties": {
                    "files": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "The CSV file(s) to operate on",
                    },
                    "query": {
                        "type": "string",
                        "description": "SQL query to execute",
                    },
                },
                "required": ["files", "query"],
            },
        }

    def execute(self, files: list[str], query: str) -> str:
        db_path = (Path(self.tmp_path) / "tmp.db").resolve()
        db_url = URL.create(drivername="sqlite", host="/" + str(db_path)).render_as_string()

        files_to_insert = []
        if db_path.is_file():
            with sqlite3.connect(str(db_path)) as conn:
                for file in files:
                    res = conn.execute(
                        f"SELECT 1 from {file.removesuffix('.csv')}",
                    )
                    if res.fetchone() is None:
                        files_to_insert.append(file)
        else:
            files_to_insert = files

        if len(files_to_insert) > 0:
            p = subprocess.run(
                ["csvsql", *files_to_insert, "--db", db_url, "--insert"], capture_output=True, text=True, cwd=self.path
            )
            if p.returncode != 0:
                return "ERROR:\n" + p.stderr

        with sqlite3.connect(str(db_path)) as conn:
            pandas_df = pandas.read_sql_query(query, conn)
            rv = pandas_df.to_csv()

        if len(rv) > 5000:
            return rv[:5000] + "<TRUNCATED>"
        return rv
