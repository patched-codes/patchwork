import json

from patchwork.common.client.llm.utils import example_json_to_schema
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
        return json.loads(s, strict=False)
    except json.JSONDecodeError:
        return dict()


class SimplifiedLLM(Step):
    def __init__(self, inputs):
        super().__init__(inputs)
        missing_keys = SimplifiedLLMInputs.__required_keys__.difference(set(inputs.keys()))
        if len(missing_keys) > 0:
            raise ValueError(f'Missing required data: "{missing_keys}"')

        self.user = inputs["prompt_user"]
        self.system = inputs.get("prompt_system")
        self.prompt_values = inputs["prompt_values"]
        self.is_json_mode = inputs.get("json", False)
        self.json_example = inputs.get("json_example")
        self.inputs = inputs

    def run(self) -> dict:
        prompts = [dict(role="user", content=self.user)]
        if self.system:
            prompts.insert(0, dict(role="system", content=self.system))
        prepare_prompt_inputs = dict(
            prompt_template=prompts,
            prompt_values=self.prompt_values,
        )
        prepare_prompt_outputs = PreparePrompt(prepare_prompt_inputs).run()

        model_keys = [key for key in self.inputs.keys() if key.startswith("model_")]
        response_format = dict(type="json_object" if self.is_json_mode else "text")
        if self.json_example is not None:
            response_format = example_json_to_schema(self.json_example)
        call_llm_inputs = {
            "prompts": prepare_prompt_outputs.get("prompts"),
            **{
                key: self.inputs[key]
                for key in [
                    "model",
                    "openai_api_key",
                    "patched_api_key",
                    "google_api_key",
                    "anthropic_api_key",
                    "max_llm_calls",
                    *model_keys,
                ]
                if self.inputs.get(key) is not None
            },
            "model_response_format": response_format,
        }
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
                prompts=prepare_prompt_outputs.get("prompts"),
                openai_responses=call_llm_outputs.get("openai_responses"),
                extracted_responses=extract_model_response_outputs.get("extracted_responses"),
                request_tokens=call_llm_outputs.get("request_tokens"),
                response_tokens=call_llm_outputs.get("response_tokens"),
            )
        )
