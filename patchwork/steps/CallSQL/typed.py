from __future__ import annotations

from typing_extensions import Any, TypedDict


class __RequiredCallSQLInputs(TypedDict):
    db_dialect: str
    db_query: str


class CallSQLInputs(__RequiredCallSQLInputs, total=False):
    db_driver: str
    db_username: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str
    db_params: dict[str, Any]
    db_driver_args: dict[str, Any]
    db_query_template_values: dict[str, Any]


class CallSQLOutputs(TypedDict):
    results: list[dict[str, Any]]
