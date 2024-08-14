from typing_extensions import List, TypedDict, Union, Dict


class CombineInputs(TypedDict):
    json_1: Union[List[Dict], Dict]
    json_2: Union[List[Dict], Dict]


class CombineOutputs(TypedDict):
    result_json: Union[List[Dict], Dict]
