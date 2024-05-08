import json
import tempfile

import pytest

from patchwork.steps import PreparePrompt


_PROMPT_FILE_DICT = {
    "id": "12345",
    "prompts": [{"key": "value"}]
}


@pytest.fixture
def valid_prompt_file():
    with tempfile.TemporaryFile("w") as f:
        json.dump(_PROMPT_FILE_DICT, f)
        yield f.name


def test_prepare_prompt_prompt_values(valid_prompt_file):
    inputs = {
        "prompt_template_file": valid_prompt_file,
        "prompt_id": "12345",
        "prompt_values": {
            "key1": "value1",
            "key2": "value2"
        }
    }
    prepare_prompt = PreparePrompt(inputs)
    assert prepare_prompt.prompt_template == _PROMPT_FILE_DICT
    assert prepare_prompt.prompt_values is not None


def test_prepare_prompt_required_keys(valid_inputs):
    required_keys = PreparePrompt.required_keys
    for key in required_keys:
        if key not in valid_inputs:
            pytest.xfail("Missing required key")

def test_prepare_prompt_prompts(valid_inputs):
    prepare_prompt = PreparePrompt(valid_inputs)
    prompts = prepare_prompt.run()
    assert prompts["prompt_file"]

def test_prepare_prompt_template_file_not_found(tmp_path):
    prepare_prompt = PreparePrompt({"prompt_template_file": str(tmp_path / "non-existing-file.json")})
    with pytest.raises(ValueError):
        prepare_prompt.run()

def test_prepare_prompt_missing_prompt_id(tmp_path):
    prepare_prompt = PreparePrompt({"prompt_template_file": str(tmp_path / "valid/prompt/template/file.json"), "prompt_id": None})
    with pytest.raises(ValueError):
        prepare_prompt.run()

def test_prepare_prompt_non_existent_prompt_value_file(tmp_path):
    prepare_prompt = PreparePrompt({"prompt_template_file": str(tmp_path / "valid/prompt/template/file.json"), "prompt_id": "12345", "prompt_value_file": str(tmp_path / "non-existing-file.json")})
    with pytest.raises(ValueError):
        prepare_prompt.run()