import json

from patchwork.step import Step
from patchwork.steps.SimplifiedLLM.SimplifiedLLM import SimplifiedLLM
from patchwork.steps.SimplifiedLLMOncePB.typed import SimplifiedLLMOncePBInputs


class SimplifiedLLMOncePB(Step, input_class=SimplifiedLLMOncePBInputs):
    def __init__(self, inputs):
        super().__init__(inputs)

        self.user = inputs["user_prompt"]
        self.system = inputs.get("system_prompt")
        self.prompt_value = inputs["prompt_value"]
        self.json_schema = inputs["json_schema"]
        self.inputs = inputs

    def __json_schema_as_suffix(self, prompt: str):
        return f"""\
{prompt}
Respond only with the following json format, do not include any additional information:
{json.dumps(self.json_schema)}
"""

    def run(self) -> dict:
        if self.system is not None:
            prompt_dict = dict(
                prompt_system=self.__json_schema_as_suffix(self.system),
                prompt_user=self.user,
            )
        else:
            prompt_dict = dict(
                prompt_user=self.__json_schema_as_suffix(self.user),
            )

        llm = SimplifiedLLM(
            {
                **self.inputs,
                **prompt_dict,
                "prompt_values": [self.prompt_value],
                "json": True,
            }
        )
        llm_output = llm.run()

        return dict(
            **llm_output.get("extracted_responses")[0],
        )
