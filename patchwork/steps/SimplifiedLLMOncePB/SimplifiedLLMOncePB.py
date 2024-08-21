import json
from typing import Any, Dict

from patchwork.step import Step
from patchwork.steps.SimplifiedLLM.SimplifiedLLM import SimplifiedLLM
from patchwork.steps.SimplifiedLLMOncePB.typed import SimplifiedLLMOncePBInputs


class SimplifiedLLMOncePB(Step, input_class=SimplifiedLLMOncePBInputs):
    """A step that uses SimplifiedLLM with a JSON schema suffix."""

    def __init__(self, inputs: Dict[str, Any]):
        """Initialize the SimplifiedLLMOncePB step."""
        super().__init__(inputs)

        self.user = inputs["prompt_user"]
        self.system = inputs.get("prompt_system")
        self.prompt_value = inputs["prompt_value"]
        self.json_schema = inputs["json_schema"]
        self.inputs = inputs

    def __json_schema_as_suffix(self, prompt: str) -> str:
        """Add JSON schema as a suffix to the prompt."""
        return f"""\
{prompt}
Respond with the following json format but minified:
{json.dumps(self.json_schema, indent=2)}
"""

    def run(self) -> Dict[str, Any]:
        """Run the SimplifiedLLMOncePB step."""
        if self.system is not None:
            prompt_dict = {
                "prompt_system": self.__json_schema_as_suffix(self.system),
                "prompt_user": self.user,
            }
        else:
            prompt_dict = {
                "prompt_user": self.__json_schema_as_suffix(self.user),
            }

        llm = SimplifiedLLM(
            {
                **self.inputs,
                **prompt_dict,
                "prompt_values": [self.prompt_value],
                "json": True,
            }
        )
        llm_output = llm.run()

        return {
            **llm_output.get("extracted_responses")[0],
        }