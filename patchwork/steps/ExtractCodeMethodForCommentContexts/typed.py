from typing_extensions import Iterable, NotRequired, TypedDict


class ExtractCodeInputs(TypedDict):
    base_path: NotRequired[str]
    context_grouping: NotRequired[str]


class ExtractCodeOutputs(TypedDict):
    files_to_patch: Iterable["ExtractedCode"]
    prompt_values: Iterable["ExtractedCode"]


class ExtractedCode(TypedDict):
    uri: str
    startLine: int
    endLine: int
    affectedCode: str
