import json
from functools import partial

from json_repair import repair_json

from patchwork.common.client.llm.utils import example_json_to_schema
from patchwork.common.utils.utils import RetryData, exclude_none_dict, retry
from patchwork.logger import logger
from patchwork.step import Step, StepStatus
from patchwork.steps.CallLLM.CallLLM import CallLLM
from patchwork.steps.ExtractModelResponse.ExtractModelResponse import (
    ExtractModelResponse,
)
from patchwork.steps.PreparePrompt.PreparePrompt import PreparePrompt
from patchwork.steps.SimplifiedLLM.typed import SimplifiedLLMInputs


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

    def __record_status_or_raise(self, retry_data: RetryData, step: Step):
        if retry_data.retry_count == retry_data.retry_limit or step.status != StepStatus.FAILED:
            self.set_status(step.status, step.status_message)
        else:
            raise ValueError(step.status_message)

    @staticmethod
    def __json_loads(json_str: str) -> dict:
        try:
            return json.loads(json_str, strict=False)
        except json.JSONDecodeError as e:
            logger.debug(f"Json to decode: \n{json_str}\nError: \n{e}")

        try:
            json_str = repair_json(json_str, skip_json_loads=True)
            return json.loads(json_str, strict=False)
        except json.JSONDecodeError as e:
            logger.debug(f"Json to decode: \n{json_str}\nError: \n{e}")
            raise e

    def __retry_unit(self, prepare_prompt_outputs, call_llm_inputs, retry_data: RetryData):
        call_llm = CallLLM(call_llm_inputs)
        call_llm_outputs = call_llm.run()
        self.__record_status_or_raise(retry_data, call_llm)

        if self.is_json_mode:
            json_responses = []
            for response in call_llm_outputs.get("openai_responses"):
                try:
                    json_response = self.__json_loads(response)
                    json_responses.append(json_response)
                except json.JSONDecodeError as e:
                    logger.error(f"Json to decode: \n{response}\nError: \n{e}")
                    call_llm.set_status(StepStatus.FAILED, "Failed to decode JSON response")
                    self.__record_status_or_raise(retry_data, call_llm)
                    continue

            extract_model_response_outputs = dict(extracted_responses=json_responses)
        else:
            extract_model_response_inputs = dict(
                openai_responses=call_llm_outputs.get("openai_responses"),
            )
            if self.inputs.get("response_partitions"):
                extract_model_response_inputs["response_partitions"] = self.inputs["response_partitions"]
            extract_model_response = ExtractModelResponse(extract_model_response_inputs)
            extract_model_response_outputs = extract_model_response.run()
            self.__record_status_or_raise(retry_data, extract_model_response)

        return exclude_none_dict(
            dict(
                prompts=prepare_prompt_outputs.get("prompts"),
                openai_responses=call_llm_outputs.get("openai_responses"),
                extracted_responses=extract_model_response_outputs.get("extracted_responses"),
                request_tokens=call_llm_outputs.get("request_tokens"),
                response_tokens=call_llm_outputs.get("response_tokens"),
            )
        )

    def run(self) -> dict:
        prompts = [dict(role="user", content=self.user)]
        if self.system:
            prompts.insert(0, dict(role="system", content=self.system))
        prepare_prompt_inputs = dict(
            prompt_template=prompts,
            prompt_values=self.prompt_values,
        )
        prepare_prompt = PreparePrompt(prepare_prompt_inputs)
        prepare_prompt_outputs = prepare_prompt.run()
        self.set_status(prepare_prompt.status, prepare_prompt.status_message)

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
        retry_unit = partial(self.__retry_unit, prepare_prompt_outputs, call_llm_inputs)
        return retry(retry_unit, retry_limit=3)
