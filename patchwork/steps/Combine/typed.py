from typing_extensions import Dict, List, TypedDict, Union


class CombineInputs(TypedDict):
    base_json: Union[List[Dict], Dict]
    update_json: Union[List[Dict], Dict]


class CombineOutputs(TypedDict):
    result_json: Union[List[Dict], Dict]
