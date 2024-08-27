from typing_extensions import TypedDict


class TsMorphInputs(TypedDict):
    file_path: str
    variable_name: str


class TsMorphOutputs(TypedDict):
    type_information: str
