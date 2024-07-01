from __future__ import annotations

from typing_extensions import TypedDict


class AnalyzeImpactInputs(TypedDict):
    extracted_responses: list["AnalyzeImpactExtractedResponse"]
    library_name: str
    platform_type: str


class AnalyzeImpactExtractedResponse(TypedDict):
    impacted_methods: str


class AnalyzeImpactOutputs(TypedDict):
    files_to_patch: list["AnalyzeImpactImpact"]


class AnalyzeImpactImpact(TypedDict):
    startLine: int
    endLine: int
    uri: str
    previousCode: str
    methodInfoList: str
