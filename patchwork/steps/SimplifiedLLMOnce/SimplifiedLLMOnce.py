from patchwork.step import Step
from patchwork.steps.SimplifiedLLM.SimplifiedLLM import SimplifiedLLM
from patchwork.steps.SimplifiedLLMOnce.typed import (
    SimplifiedLLMOnceInputs,
    SimplifiedLLMOnceOutputs,
)


class SimplifiedLLMOnce(Step, input_class=SimplifiedLLMOnceInputs, output_class=SimplifiedLLMOnceOutputs):
    def __init__(self, inputs):
        super().__init__(inputs)

        self.user = inputs["user_prompt"]
        self.system = inputs.get("system_prompt")
        self.prompt_value = inputs["prompt_value"]
        self.json_example = inputs["json_schema"]
        self.inputs = inputs

    def run(self) -> dict:
        if self.system is not None:
            prompt_dict = dict(
                prompt_system=self.system,
                prompt_user=self.user,
            )
        else:
            prompt_dict = dict(
                prompt_user=self.user,
            )

        llm = SimplifiedLLM(
            {
                **self.inputs,
                **prompt_dict,
                "prompt_values": [self.prompt_value],
                "json": True,
                "json_example": self.json_example,
            }
        )
        llm_output = llm.run()
        self.set_status(llm.status, llm.status_message)

        return {
            **llm_output.get("extracted_responses")[0],
            "request_tokens": llm_output.get("request_tokens")[0],
            "response_tokens": llm_output.get("response_tokens")[0],
        }
