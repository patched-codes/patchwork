import itertools
import json
import tempfile

import pytest

from patchwork.steps import PreparePrompt

_PROMPT_ID = "test"
_PROMPT_FILE_DICT = [
    {
        "id": _PROMPT_ID,
        "prompts": [{"role": "system", "content": "{{test1}}"}, {"role": "user", "content": "{{test2}}"}],
    }
]
_PROMPT_VALUES = [
    {"test1": "value1", "test2": "value2", "test3": "value3"},
    {"test1": "value1", "test2": "value2", "test3": "value3"},
]


@pytest.fixture
def valid_prompt_file():
    fp = tempfile.NamedTemporaryFile("w", delete=False)
    try:
        json.dump(_PROMPT_FILE_DICT, fp)
        fp.flush()
        yield str(fp.name)
    finally:
        fp.close()


@pytest.fixture
def valid_prompt_values_file():
    fp = tempfile.NamedTemporaryFile("w", delete=False)
    try:
        json.dump(_PROMPT_VALUES, fp)
        fp.flush()
        yield str(fp.name)
    finally:
        fp.close()


@pytest.mark.parametrize(
    "keys",
    [
        set(),
        {"prompt_template_file"},
        {"prompt_id"},
        {"prompt_values"},
        {"prompt_value_file"},
        {"prompt_template_file", "prompt_id"},
        {"prompt_template_file", "prompt_values"},
        {"prompt_template_file", "prompt_value_file"},
        {"prompt_id", "prompt_values"},
        {"prompt_id", "prompt_value_file"},
        {"prompt_values", "prompt_value_file"},
        {"prompt_template_file", "prompt_values", "prompt_value_file"},
        # this will pass
        # {"prompt_template_file", "prompt_id", "prompt_values"},
    ],
)
def test_prepare_prompt_required_keys(valid_prompt_file, valid_prompt_values_file, keys):
    inputs = {
        "prompt_template_file": valid_prompt_file,
        "prompt_id": _PROMPT_ID,
        "prompt_values": _PROMPT_VALUES,
        "prompt_value_file": valid_prompt_values_file,
    }
    bad_inputs = {key: value for key, value in inputs.items() if key in keys}
    with pytest.raises(ValueError):
        PreparePrompt(bad_inputs)


@pytest.mark.parametrize("keys", itertools.combinations(["prompt_template_file", "prompt_value_file", ""], 2))
def test_prepare_prompt_non_existent_files(valid_prompt_file, valid_prompt_values_file, keys):
    inputs = {
        "prompt_template_file": valid_prompt_file,
        "prompt_id": _PROMPT_ID,
        "prompt_value_file": valid_prompt_values_file,
    }
    for key in keys:
        inputs[key] = "non-existing-file.json"

    with pytest.raises(ValueError):
        PreparePrompt(inputs)


@pytest.mark.parametrize("key", ["prompt_values", "prompt_value_file"])
def test_prepare_prompt_prompt_values(valid_prompt_file, valid_prompt_values_file, key):
    inputs = {
        "prompt_template_file": valid_prompt_file,
        "prompt_id": _PROMPT_ID,
        "prompt_values": _PROMPT_VALUES,
        "prompt_value_file": valid_prompt_values_file,
    }
    del inputs[key]
    prepare_prompt = PreparePrompt(inputs)
    assert prepare_prompt.prompt_template == _PROMPT_FILE_DICT[0]["prompts"]
    assert prepare_prompt.prompt_values == _PROMPT_VALUES


def test_prepare_prompt_prompts(valid_prompt_file):
    inputs = {
        "prompt_template_file": valid_prompt_file,
        "prompt_id": _PROMPT_ID,
        "prompt_values": _PROMPT_VALUES,
    }
    prepare_prompt = PreparePrompt(inputs)
    prompts = prepare_prompt.run()
    assert prompts["prompts"] is not None
    assert len(prompts["prompts"]) == 2
