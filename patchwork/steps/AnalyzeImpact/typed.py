from typing_extensions import Iterable, TypedDict


class AnalyzeImpactInputs(TypedDict):
    extracted_responses: Iterable["AnalyzeImpactExtractedResponse"]
    library_name: str
    platform_type: str


class AnalyzeImpactExtractedResponse(TypedDict):
    impacted_methods: str


class AnalyzeImpactOutputs(TypedDict):
    files_to_patch: Iterable["AnalyzeImpactImpact"]


class AnalyzeImpactImpact(TypedDict):
    startLine: int
    endLine: int
    uri: str
    previousCode: str
    methodInfoList: str
