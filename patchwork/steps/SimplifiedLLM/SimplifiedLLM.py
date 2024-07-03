import json
import tempfile

from patchwork.step import Step
from patchwork.steps.CallLLM.CallLLM import CallLLM
from patchwork.steps.ExtractModelResponse.ExtractModelResponse import (
    ExtractModelResponse,
)
from patchwork.steps.SimplifiedLLM.typed import SimplifiedLLMInputs
from patchwork.steps.PreparePrompt.PreparePrompt import PreparePrompt


class SimplifiedLLM(Step):
    def __init__(self, inputs):
        missing_keys = SimplifiedLLMInputs.__required_keys__.difference(set(inputs.keys()))
        if len(missing_keys) > 0:
            raise ValueError(f'Missing required data: "{missing_keys}"')

        self.user = inputs["prompt_user"]
        self.system = inputs.get("prompt_system")
        self.prompt_values = inputs["prompt_values"]
        self.inputs = inputs

    def run(self) -> dict:
        with tempfile.TemporaryFile("w") as fp:
            prompt_id = "prompt_id"
            prompts = [dict(role="user", content=self.user)]
            if self.system:
                prompts.insert(0, dict(role="system", content=self.system))
            json.dump([dict(id=prompt_id, prompts=prompts)], fp)
            prepare_prompt_outputs = PreparePrompt(dict(
                prompt_template_file=fp.name,
                prompt_id=prompt_id,
                prompt_values=self.prompt_values,
            )).run()

        call_llm_outputs = CallLLM(dict(
                prompts=prepare_prompt_outputs.get("prompts"),
                **self.inputs,
        )).run()

        extract_model_response_outputs = ExtractModelResponse(dict(
                openai_responses=call_llm_outputs.get("openai_responses"),
                **self.inputs,
        )).run()
        return dict(
            prompts=prepare_prompt_outputs.get("prompts"),
            openai_responses=call_llm_outputs.get("openai_responses"),
            extracted_responses=extract_model_response_outputs.get("extracted_responses"),
        )
