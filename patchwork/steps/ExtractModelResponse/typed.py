from typing_extensions import Iterable, NotRequired, TypedDict


class ExtractModelResponsesInputs(TypedDict):
    openai_responses: Iterable[str]
    response_partitions: NotRequired[dict[str, list[str]]]


class ExtractModelResponsesOutputs(TypedDict):
    extracted_responses: list[dict[str, str]]
