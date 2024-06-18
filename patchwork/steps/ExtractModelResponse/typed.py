from __future__ import annotations

from typing_extensions import Iterable, NotRequired, TypedDict


class ExtractModelResponseInputs(TypedDict):
    openai_responses: Iterable[str]
    response_partitions: NotRequired[dict[str, list[str]]]


class ExtractModelResponseOutputs(TypedDict):
    extracted_responses: list[dict[str, str]]
