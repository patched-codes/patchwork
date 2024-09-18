from patchwork.common.utils.utils import exclude_none_dict
from patchwork.step import Step
from patchwork.steps.SimplifiedLLM.SimplifiedLLM import SimplifiedLLM
from patchwork.steps.SimplifiedLLMOnce.typed import SimplifiedLLMOnceInputs


class SimplifiedLLMOnce(Step):
    def __init__(self, inputs):
        super().__init__(inputs)
        self.inputs = inputs
        self.inputs = inputs
        missing_keys = SimplifiedLLMOnceInputs.__required_keys__.difference(set(inputs.keys()))
        if len(missing_keys) > 0:
            raise ValueError(f'Missing required data: "{missing_keys}"')

        self.prompt_value = inputs["prompt_value"]
        self.inputs = inputs

    def run(self) -> dict:
        if self.inputs.get("debug") is not None:
            self.debug(self.inputs)
            
        llm = SimplifiedLLM({**self.inputs, "prompt_values": [self.prompt_value]})
        llm_output = llm.run()

        return exclude_none_dict(
            dict(
                prompt=llm_output.get("prompts")[0],
                openai_response=llm_output.get("openai_responses")[0],
                extracted_response=llm_output.get("extracted_responses")[0],
                request_tokens=llm_output.get("request_tokens")[0],
                response_tokens=llm_output.get("response_tokens")[0],
            )
        )
