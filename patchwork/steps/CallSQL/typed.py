from __future__ import annotations

from typing_extensions import Any, TypedDict


class __RequiredCallSQLInputs(TypedDict):
    dialect: str
    username: str
    query: str


class CallSQLInputs(__RequiredCallSQLInputs, total=False):
    driver: str
    password: str
    host: str
    port: int
    database: str
    query_template_values: dict[str, Any]


class CallSQLOutputs(TypedDict):
    result: list[dict[str, Any]]
