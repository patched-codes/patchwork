from __future__ import annotations

from typing import TypedDict


class JoinListInputs(TypedDict):
    list: list[str]
    delimiter: str


class JoinListOutputs(TypedDict):
    text: str
