from __future__ import annotations

import json
from collections.abc import Iterable, Mapping

from typing_extensions import AnyStr, Union

__ITEM_TYPE = Union[AnyStr, Mapping]


def __parse_to_list_handle_str(input_value: AnyStr, possible_delimiters: Iterable[AnyStr | None]) -> list[str]:
    for possible_delimiter in possible_delimiters:
        if possible_delimiter is None:
            return input_value.split()

        if possible_delimiter in input_value:
            return input_value.split(possible_delimiter)

    return []


def __parse_to_list_handle_dict(input_value: Mapping, possible_keys: Iterable[AnyStr | None]) -> list[str]:
    for possible_key in possible_keys:
        if input_value.get(possible_key) is not None:
            return input_value.get(possible_key)

    return []


def __parse_to_list_handle_iterable(
    input_value: Iterable[__ITEM_TYPE], possible_keys: Iterable[AnyStr | None]
) -> list[str]:
    rv = []
    for item in input_value:
        if isinstance(item, dict):
            for possible_key in possible_keys:
                if item.get(possible_key) is not None:
                    rv.append(item.get(possible_key))
        else:
            rv.append(item)

    return rv


def parse_to_list(
    input_value: __ITEM_TYPE | Iterable[__ITEM_TYPE],
    possible_delimiters: Iterable[AnyStr | None] | None = None,
    possible_keys: Iterable[AnyStr | None] | None = None,
) -> list[str]:
    if len(input_value) < 1:
        return []

    if possible_delimiters is None:
        possible_delimiters = []
    if possible_keys is None:
        possible_keys = []

    value_to_parse = []
    if isinstance(input_value, dict):
        value_to_parse = __parse_to_list_handle_dict(input_value, possible_keys)
    elif isinstance(input_value, str):
        value_to_parse = __parse_to_list_handle_str(input_value, possible_delimiters)
    elif isinstance(input_value, Iterable):
        value_to_parse = __parse_to_list_handle_iterable(input_value, possible_keys)

    rv = []
    for value in value_to_parse:
        stripped_value = value.strip()
        if stripped_value == "":
            continue
        rv.append(stripped_value)
    return rv


def parse_to_dict(possible_dict, limit=-1):
    if possible_dict is None and limit == 0:
        return None

    if isinstance(possible_dict, dict):
        new_dict = dict()
        for k, v in possible_dict.items():
            new_dict[k] = parse_to_dict(v, limit - 1)
        return new_dict
    elif isinstance(possible_dict, str):
        try:
            new_dict = json.loads(possible_dict, strict=False)
        except json.JSONDecodeError:
            return possible_dict

        return parse_to_dict(new_dict, limit - 1)
    else:
        return possible_dict
