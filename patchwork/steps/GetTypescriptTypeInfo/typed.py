from typing_extensions import TypedDict


class GetTypescriptTypeInfoInputs(TypedDict):
    file_path: str
    variable_name: str


class GetTypescriptTypeInfoOutputs(TypedDict):
    type_information: str
