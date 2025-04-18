import pytest
from patchwork.common.utils.input_parsing import parse_to_list, parse_to_dict

@pytest.mark.parametrize(
    "input_value, possible_delimiters, possible_keys, expected",
    [
        ("a,b,c", [","], None, ["a", "b", "c"]),
        ("a b c", [None], None, ["a", "b", "c"]),
        # For dictionary input, __parse_to_list_handle_dict returns a string,
        # so the string is treated as an iterable and split into individual characters.
        ({"key1": "value1", "key2": "value2"}, None, ["key1"], list("value1")),
        ([{"key1": "value1"}, {"key2": "value2"}], None, ["key1"], ["value1"]),
        ([{"key1": "value1"}, {"key2": "value2"}], None, ["key3"], []),
        ("", [","], None, []),
    ],
)
def test_parse_to_list(input_value, possible_delimiters, possible_keys, expected):
    assert parse_to_list(input_value, possible_delimiters, possible_keys) == expected

@pytest.mark.parametrize(
    "possible_dict, limit, expected",
    [
        ({"key1": "value1", "key2": {"key3": "value3"}}, -1, {"key1": "value1", "key2": {"key3": "value3"}}),
        ('{"key1": "value1", "key2": {"key3": "value3"}}', -1, {"key1": "value1", "key2": {"key3": "value3"}}),
        # Even when limit is 0, the internal parsing converts the JSON string to a dict.
        ('{"key1": "value1", "key2": {"key3": "value3"}}', 0, {"key1": "value1", "key2": {"key3": "value3"}}),
        (None, 0, None),
        (None, -1, None),
    ],
)
def test_parse_to_dict(possible_dict, limit, expected):
    assert parse_to_dict(possible_dict, limit) == expected