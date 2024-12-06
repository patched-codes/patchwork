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
    """A context manager that creates a temporary file with valid prompt data.
    
    This method creates a temporary file, writes a predefined dictionary
    (_PROMPT_FILE_DICT) as JSON to the file, and yields the file path. The file
    is automatically closed and deleted after the context is exited.
    
    Args:
        None
    
    Returns:
        str: The path to the temporary file containing the valid prompt data.
    
    Yields:
        str: The path to the temporary file containing the valid prompt data.
    
    Raises:
        JSONDecodeError: If there's an error in JSON serialization.
        IOError: If there's an error in file operations.
    """
    fp = tempfile.NamedTemporaryFile("w", delete=False)
    try:
        json.dump(_PROMPT_FILE_DICT, fp)
        fp.flush()
        yield str(fp.name)
    finally:
        fp.close()


@pytest.fixture
def valid_prompt_values_file():
    """Creates a temporary file containing valid prompt values and yields the file path.
    
    This method generates a temporary file, writes the contents of _PROMPT_VALUES
    (assumed to be a dictionary or list) as JSON to the file, and yields the file path.
    The file is automatically closed and deleted after use.
    
    Args:
        None
    
    Returns:
        str: The path to the temporary file containing the valid prompt values.
    
    Yields:
        str: The path to the temporary file containing the valid prompt values.
    
    Raises:
        IOError: If there's an error writing to the temporary file.
        JSONDecodeError: If _PROMPT_VALUES cannot be serialized to JSON.
    """
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
    """Tests the PreparePrompt class with required keys missing.
    
    This method tests the behavior of the PreparePrompt class when required keys are missing from the input dictionary. It expects a ValueError to be raised when the PreparePrompt class is instantiated with incomplete inputs.
    
    Args:
        valid_prompt_file (str): Path to a valid prompt template file.
        valid_prompt_values_file (str): Path to a valid prompt values file.
        keys (list): List of keys to be removed from the input dictionary.
    
    Returns:
        None
    
    Raises:
        ValueError: When PreparePrompt is instantiated with missing required keys.
    """
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
    """Tests the PreparePrompt class initialization with different input combinations.
    
    Args:
        valid_prompt_file (str): Path to a valid prompt template file.
        valid_prompt_values_file (str): Path to a valid prompt values file.
        key (str): The key to be removed from the inputs dictionary.
    
    Returns:
        None: This method doesn't return anything explicitly.
    
    Raises:
        AssertionError: If the assertions for prompt_template or prompt_values fail.
    """
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
    """Test the preparation of prompts using a valid prompt file.
    
    Args:
        valid_prompt_file (str): Path to a valid prompt template file.
    
    Returns:
        None
    
    Raises:
        AssertionError: If the prepared prompts are None or if the number of prompts is not equal to 2.
    """
    inputs = {
        "prompt_template_file": valid_prompt_file,
        "prompt_id": _PROMPT_ID,
        "prompt_values": _PROMPT_VALUES,
    }
    prepare_prompt = PreparePrompt(inputs)
    prompts = prepare_prompt.run()
    assert prompts["prompts"] is not None
    assert len(prompts["prompts"]) == 2
