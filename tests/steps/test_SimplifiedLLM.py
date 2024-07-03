from pathlib import Path

import pytest

from patchwork.steps.CallLLM.CallLLM import CallLLM
from patchwork.steps.ExtractModelResponse.ExtractModelResponse import ExtractModelResponse
from patchwork.steps.PreparePrompt.PreparePrompt import PreparePrompt
from patchwork.steps.SimplifiedLLM.SimplifiedLLM import SimplifiedLLM


@pytest.mark.parametrize("inputs", [
    {
         "prompt_user": "user",
         "model": "model",
         "openai_api_key": "openai_api_key",
         "json": True,
     },
])
def test_invalid(inputs):
    with pytest.raises(ValueError):
        SimplifiedLLM(inputs)


def test_non_json_run(mocker):
    inputs = dict(
        prompt_user="user",
        prompt_system="system",
        prompt_values=[{"value": "here"}],
        model="model",
        openai_api_key="openai_api_key",
    )

    mocked_prepare_prompt = mocker.MagicMock()
    mocked_prepare_prompt_class = mocker.patch.object(PreparePrompt, "__new__", return_value=mocked_prepare_prompt)
    mocked_call_llm = mocker.MagicMock()
    mocked_call_llm_class = mocker.patch.object(CallLLM, "__new__", return_value=mocked_call_llm)
    mocked_extract_model_response = mocker.MagicMock()
    mocked_extract_model_response_class = mocker.patch.object(ExtractModelResponse, "__new__", return_value=mocked_extract_model_response)

    simplified_llm = SimplifiedLLM(inputs)
    output = simplified_llm.run()

    assert mocked_prepare_prompt.run.called
    assert mocked_call_llm.run.called
    assert mocked_extract_model_response.run.called

    prepare_prompt_inputs = mocked_prepare_prompt_class.call_args[0][1]
    assert prepare_prompt_inputs["prompt_template_file"]
    assert not Path(prepare_prompt_inputs["prompt_template_file"]).exists()
    assert prepare_prompt_inputs["prompt_id"] == "prompt_id"
    assert prepare_prompt_inputs["prompt_values"] == inputs["prompt_values"]

    call_llm_inputs = mocked_call_llm_class.call_args[0][1]
    assert call_llm_inputs["model_response_format"] == {"type": "text"}
    assert call_llm_inputs["prompts"] == mocked_prepare_prompt.run().get()
    assert call_llm_inputs["model"] == inputs["model"]
    assert call_llm_inputs["openai_api_key"] == inputs["openai_api_key"]

    extract_model_response_inputs = mocked_extract_model_response_class.call_args[0][1]
    assert extract_model_response_inputs["openai_responses"] == mocked_call_llm.run().get()


def test_json_run(mocker):
    inputs = dict(
        prompt_user="user",
        prompt_system="system",
        prompt_values=[{"value": "here"}],
        model="model",
        openai_api_key="openai_api_key",
        json=True,
    )

    mocked_prepare_prompt = mocker.MagicMock()
    mocked_prepare_prompt_class = mocker.patch.object(PreparePrompt, "__new__", return_value=mocked_prepare_prompt)
    mocked_call_llm = mocker.MagicMock()
    mocked_call_llm_class = mocker.patch.object(CallLLM, "__new__", return_value=mocked_call_llm)
    mocked_extract_model_response = mocker.MagicMock()
    mocked_extract_model_response_class = mocker.patch.object(ExtractModelResponse, "__new__", return_value=mocked_extract_model_response)

    simplified_llm = SimplifiedLLM(inputs)
    output = simplified_llm.run()

    assert mocked_prepare_prompt.run.called
    assert mocked_call_llm.run.called
    assert mocked_extract_model_response.run.not_called

    prepare_prompt_inputs = mocked_prepare_prompt_class.call_args[0][1]
    assert prepare_prompt_inputs["prompt_template_file"]
    assert not Path(prepare_prompt_inputs["prompt_template_file"]).exists()
    assert prepare_prompt_inputs["prompt_id"] == "prompt_id"
    assert prepare_prompt_inputs["prompt_values"] == inputs["prompt_values"]

    call_llm_inputs = mocked_call_llm_class.call_args[0][1]
    assert call_llm_inputs["model_response_format"] == {"type": "json_object"}
    assert call_llm_inputs["prompts"] == mocked_prepare_prompt.run().get()
    assert call_llm_inputs["model"] == inputs["model"]
    assert call_llm_inputs["openai_api_key"] == inputs["openai_api_key"]
