import pytest

from patchwork.steps.ExtractModelResponse.ExtractModelResponse import (
    ExtractModelResponse,
)


@pytest.fixture
def sample_inputs():
    return {
        "openai_responses": ["partition1response1partition2", "response2partition3"],
        "response_partitions": {"key1": ["partition1", "partition2"], "key2": ["partition3"]},
    }


def test_init_required_keys(sample_inputs):
    step = ExtractModelResponse(sample_inputs)
    assert step.openai_responses == sample_inputs["openai_responses"]
    assert step.partitions == sample_inputs["response_partitions"]


def test_init_missing_required_keys():
    with pytest.raises(ValueError):
        ExtractModelResponse({})


def test_run_no_partitions(sample_inputs):
    step = ExtractModelResponse({**sample_inputs, "response_partitions": {}})
    output = step.run()
    assert output == {"extracted_responses": []}


def test_run_with_partitions(sample_inputs):
    step = ExtractModelResponse(sample_inputs)
    output = step.run()
    assert len(output["extracted_responses"]) == 2
    assert output["extracted_responses"][0]["key1"] == "response1"
    assert output["extracted_responses"][1]["key2"] == "response2"
