from typing_extensions import List, TypedDict


class AnalyzeImpactInputs(TypedDict):
    extracted_responses: List["AnalyzeImpactExtractedResponse"]
    library_name: str
    platform_type: str


class AnalyzeImpactExtractedResponse(TypedDict):
    impacted_methods: str


class AnalyzeImpactOutputs(TypedDict):
    files_to_patch: List["AnalyzeImpactImpact"]


class AnalyzeImpactImpact(TypedDict):
    startLine: int
    endLine: int
    uri: str
    previousCode: str
    methodInfoList: str
