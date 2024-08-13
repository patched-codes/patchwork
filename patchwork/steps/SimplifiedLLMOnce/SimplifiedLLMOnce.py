import json

from patchwork.common.utils.utils import exclude_none_dict
from patchwork.step import Step
from patchwork.steps.CallLLM.CallLLM import CallLLM
from patchwork.steps.ExtractModelResponse.ExtractModelResponse import (
    ExtractModelResponse,
)
from patchwork.steps.PreparePrompt.PreparePrompt import PreparePrompt
from patchwork.steps.SimplifiedLLM.typed import SimplifiedLLMInputs


def json_loads(s: str) -> dict:
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        return dict()


class SimplifiedLLMOnce(Step):
    def __init__(self, inputs):
        super().__init__(inputs)
        missing_keys = SimplifiedLLMInputs.__required_keys__.difference(set(inputs.keys()))
        if len(missing_keys) > 0:
            raise ValueError(f'Missing required data: "{missing_keys}"')

        self.user = inputs["prompt_user"]
        self.system = inputs.get("prompt_system")
        self.prompt_value = inputs["prompt_value"]
        self.is_json_mode = inputs.get("json", False)
        self.inputs = inputs

    def run(self) -> dict:
        prompts = [dict(role="user", content=self.user)]
        if self.system:
            prompts.insert(0, dict(role="system", content=self.system))
        prepare_prompt_inputs = dict(
            prompt_template=prompts,
            prompt_values=[self.prompt_value],
        )
        prepare_prompt_outputs = PreparePrompt(prepare_prompt_inputs).run()

        call_llm_inputs = dict(
            model_response_format=dict(type="json_object" if self.is_json_mode else "text"),
            prompts=prepare_prompt_outputs.get("prompts"),
            **{
                key: self.inputs[key]
                for key in ["model", "openai_api_key", "patched_api_key", "google_api_key", "max_llm_calls"]
                if self.inputs.get(key) is not None
            },
        )
        call_llm_outputs = CallLLM(call_llm_inputs).run()

        if self.is_json_mode:
            json_response = [json_loads(response) for response in call_llm_outputs.get("openai_responses")]
            extract_model_response_outputs = dict(extracted_responses=json_response)
        else:
            extract_model_response_inputs = dict(
                openai_responses=call_llm_outputs.get("openai_responses"),
            )
            if self.inputs.get("response_partitions"):
                extract_model_response_inputs["response_partitions"] = self.inputs["response_partitions"]
            extract_model_response_outputs = ExtractModelResponse(extract_model_response_inputs).run()

        return exclude_none_dict(
            dict(
                prompt=prepare_prompt_outputs.get("prompts")[0],
                openai_response=call_llm_outputs.get("openai_responses")[0],
                extracted_response=extract_model_response_outputs.get("extracted_responses")[0],
            )
        )
