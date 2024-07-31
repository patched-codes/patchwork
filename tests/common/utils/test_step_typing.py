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
    assert '''\
Invalid inputs for steps:
Step: JoinList
  - delimiter: Missing required input data: delimiter
  - list: Missing required input data: list
''' == exc_info.value.args[0]


def test_validate_step_type_config_or_op():
    key_name = "key1"
    input_keys = {"key2", "key3"}
    step_type_config = StepTypeConfig(or_op=["key1", "key2", "key3"])

    is_ok, msg = validate_step_type_config_with_inputs(key_name, input_keys, step_type_config)
    assert is_ok
    assert msg == ""