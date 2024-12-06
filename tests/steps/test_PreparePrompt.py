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
    """A context manager that creates a temporary file containing a valid prompt dictionary.
    
    Args:
        None
    
    Returns:
        str: The path to the temporary file containing the serialized prompt dictionary.
    
    Yields:
        str: The path to the temporary file containing the serialized prompt dictionary.
    
    Notes:
        - This method uses a context manager to ensure proper cleanup of the temporary file.
        - The temporary file is created using tempfile.NamedTemporaryFile with write mode.
        - The _PROMPT_FILE_DICT is assumed to be a predefined dictionary containing prompt data.
        - The temporary file is not automatically deleted when closed, allowing for its use after the context manager exits.
        - The file is manually closed in the 'finally' block to ensure proper resource management.
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
    """Creates a temporary file with valid prompt values and yields the file path.
    
    This method creates a temporary file, writes the contents of _PROMPT_VALUES (assumed to be a
    dictionary or list) as JSON to the file, and yields the file path. The file is automatically
    closed and deleted after use.
    
    Returns:
        str: The path to the temporary file containing the valid prompt values in JSON format.
    
    Yields:
        str: The path to the temporary file.
    
    Raises:
        IOError: If there's an error writing to the temporary file.
        JSONDecodeError: If there's an error encoding _PROMPT_VALUES to JSON.
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
    """Test the PreparePrompt class with missing required keys.
    
    Args:
        valid_prompt_file (str): Path to a valid prompt template file.
        valid_prompt_values_file (str): Path to a valid prompt values file.
        keys (list): List of keys to exclude from the input dictionary.
    
    Returns:
        None
    
    Raises:
        ValueError: When the PreparePrompt class is instantiated with missing required keys.
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
    """Test the PreparePrompt class with different input configurations.
    
    Args:
        valid_prompt_file (str): Path to a valid prompt template file.
        valid_prompt_values_file (str): Path to a valid prompt values file.
        key (str): The key to remove from the inputs dictionary.
    
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
    """Tests the preparation of prompts using the PreparePrompt class.
    
    Args:
        valid_prompt_file (str): Path to a valid prompt template file.
    
    Returns:
        None
    
    Raises:
        AssertionError: If the prompts are not generated correctly or if the number of prompts is unexpected.
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
