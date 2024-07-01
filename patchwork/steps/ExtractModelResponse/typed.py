from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class __ExtractModelResponseRequiredInputs(TypedDict):
    openai_responses: list[str]


class ExtractModelResponseInputs(__ExtractModelResponseRequiredInputs, total=False):
    response_partitions: Annotated[dict[str, list[str]], IS_CONFIG]


class ExtractModelResponseOutputs(TypedDict):
    extracted_responses: list[dict[str, str]]
