from patchwork.step import Step
from patchwork.steps.CallLLM.CallLLM import CallLLM
from patchwork.steps.CallLLM.typed import CallLLMInputs
from patchwork.steps.ExtractModelResponse.ExtractModelResponse import (
    ExtractModelResponse,
)
from patchwork.steps.ExtractModelResponse.typed import ExtractModelResponseInputs
from patchwork.steps.PreparePrompt.PreparePrompt import PreparePrompt
from patchwork.steps.PreparePrompt.typed import PreparePromptInputs


class LLM(Step):
    required_keys = (
        PreparePromptInputs.__required_keys__
        | CallLLMInputs.__required_keys__
        | ExtractModelResponseInputs.__required_keys__
    )

    def __init__(self, inputs):
        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.inputs = inputs

    def run(self) -> dict:
        prepare_prompt_outputs = PreparePrompt(
            dict(
                prompt_template_file=self.inputs.get("prompt_template_file"),
                prompt_id=self.inputs.get("prompt_id"),
                prompt_value_file=self.inputs.get("prompt_value_file"),
                prompt_values=self.inputs.get("prompt_values"),
            )
        ).run()
        call_llm_outputs = CallLLM(
            dict(
                prompts=prepare_prompt_outputs.get("prompts"),
                model=self.inputs.get("model"),
                allow_truncated=self.inputs.get("allow_truncated"),
                model_args=self.inputs.get("model_args"),
                client_args=self.inputs.get("client_args"),
                openai_api_key=self.inputs.get("openai_api_key"),
                patched_api_key=self.inputs.get("patched_api_key"),
                google_api_key=self.inputs.get("google_api_key"),
            )
        ).run()
        extract_model_response_outputs = ExtractModelResponse(
            dict(
                openai_responses=call_llm_outputs.get("openai_responses"),
                response_partitions=self.inputs.get("response_partitions"),
            )
        ).run()
        return dict(
            prompts=prepare_prompt_outputs.get("prompts"),
            openai_responses=call_llm_outputs.get("openai_responses"),
            extracted_responses=extract_model_response_outputs.get("extracted_responses"),
        )
