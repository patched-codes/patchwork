import sys

import pytest

from patchwork.common.utils.step_typing import validate_steps_with_inputs, validate_step_type_config_with_inputs, \
    StepTypeConfig
from patchwork.steps import ScanSemgrep, JoinList


def test_valid_input_keys():
    keys = {"key1", "key2", "key3"}
    # should not raise any error
    validate_steps_with_inputs(keys, ScanSemgrep)


def test_invalid_input_keys():
    keys = {"key1", "key2"}
    steps = [JoinList]

    with pytest.raises(ValueError) as exc_info:
        validate_steps_with_inputs(keys, *steps)

    # Ensure the error message is correct
    lines = '''\
Invalid inputs for steps:
Step: JoinList
  - delimiter: 
      Missing required input data
  - list: 
      Missing required input data
'''.splitlines()

    for line in lines:
        assert line in exc_info.value.args[0]


@pytest.mark.parametrize(
    "key_name, input_keys, step_type_config, expected",
    [
        ["key1", set(), StepTypeConfig(or_op=["key1", "key2", "key3"]), (False, "Missing required input: At least one of key1, key1, key2, key3 has to be set")],
        ["key1", {"key1"}, StepTypeConfig(or_op=["key1", "key2", "key3"]), (True, "")],
        ["key1", {"key2", "key3"}, StepTypeConfig(or_op=["key1", "key2", "key3"]), (True, "")],
        ["key1", {"key1", "key2", "key3"}, StepTypeConfig(and_op=["key1", "key2", "key3"]), (True, "")],
        ["key1", {"key2", "key3"}, StepTypeConfig(and_op=["key1", "key2", "key3"]), (True, "")],
        ["key1", {"key1", "key3"}, StepTypeConfig(and_op=["key1", "key2", "key3"]), (False, "Missing required input data because key1 is set: key2")],
        ["key1", {"key1"}, StepTypeConfig(xor_op=["key1", "key2", "key3"]), (True, "")],
        ["key1", {"key2", "key3"}, StepTypeConfig(xor_op=["key1", "key2", "key3"]), (True, "")],
        ["key1", {"key1", "key3"}, StepTypeConfig(xor_op=["key1", "key2", "key3"]), (False, "Excess input data: key1, key3 cannot be set at the same time")],
    ]
 )
def test_validate_step_type_config(key_name, input_keys, step_type_config, expected):
    is_ok, msg = validate_step_type_config_with_inputs(key_name, input_keys, step_type_config)
    assert is_ok == expected[0]
    assert msg == expected[1]