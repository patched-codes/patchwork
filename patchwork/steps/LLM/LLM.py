from patchwork.common.utils.utils import exclude_none_dict
from patchwork.step import Step
from patchwork.steps.CallLLM.CallLLM import CallLLM
from patchwork.steps.ExtractModelResponse.ExtractModelResponse import (
    ExtractModelResponse,
)
from patchwork.steps.LLM.typed import LLMInputs
from patchwork.steps.PreparePrompt.PreparePrompt import PreparePrompt


class LLM(Step):
    def __init__(self, inputs):
        missing_keys = LLMInputs.__required_keys__.difference(set(inputs.keys()))
        if len(missing_keys) > 0:
            raise ValueError(f'Missing required data: "{missing_keys}"')

        self.inputs = inputs

    def run(self) -> dict:
        prepare_prompt_outputs = PreparePrompt(self.inputs).run()
        call_llm_outputs = CallLLM(
            dict(
                prompts=prepare_prompt_outputs.get("prompts"),
                **self.inputs,
            )
        ).run()
        extract_model_response_outputs = ExtractModelResponse(
            dict(
                openai_responses=call_llm_outputs.get("openai_responses"),
                **self.inputs,
            )
        ).run()
        return exclude_none_dict(dict(
            prompts=prepare_prompt_outputs.get("prompts"),
            openai_responses=call_llm_outputs.get("openai_responses"),
            extracted_responses=extract_model_response_outputs.get("extracted_responses"),
        ))
