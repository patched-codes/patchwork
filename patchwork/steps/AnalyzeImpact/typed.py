from pydantic import BaseModel
from typing_extensions import List, TypedDict


class AnalyzeImpactInputs(BaseModel):
    extracted_responses: List["AnalyzeImpactExtractedResponse"]
    library_name: str
    platform_type: str


class AnalyzeImpactExtractedResponse(TypedDict):
    impacted_methods: str


class AnalyzeImpactOutputs(BaseModel):
    files_to_patch: List["AnalyzeImpactImpact"]


class AnalyzeImpactImpact(TypedDict):
    startLine: int
    endLine: int
    uri: str
    previousCode: str
    methodInfoList: str
