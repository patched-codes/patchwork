from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.typing import IS_CONFIG


class JoinListInputs(TypedDict):
    list: list[str]
    delimiter: Annotated[str, IS_CONFIG]


class JoinListOutputs(TypedDict):
    text: str
