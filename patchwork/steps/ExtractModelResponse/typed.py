from typing_extensions import Iterable, TypedDict


class ExtractModelResponseInputs(TypedDict):
    openai_responses: Iterable[str]
    response_partitions: dict[str, list[str]]


class ExtractModelResponseOutputs(TypedDict):
    extracted_responses: list[dict[str, str]]
