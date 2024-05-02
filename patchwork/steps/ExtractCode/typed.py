from typing_extensions import Iterable, NotRequired, TypedDict


class ExtractCodeInputs(TypedDict):
    sarif_file_path: str
    context_size: NotRequired[int]
    vulnerability_limit: NotRequired[int]
    severity: NotRequired[str]


class ExtractCodeOutputs(TypedDict):
    code_file: str
    prompt_values: Iterable["ExtractedCode"]


class ExtractedCode(TypedDict):
    uri: str
    startLine: int
    endLine: int
    affectedCode: str
    messageText: str
