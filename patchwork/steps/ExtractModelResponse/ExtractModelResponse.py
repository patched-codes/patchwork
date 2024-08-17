from collections import defaultdict

from patchwork.logger import logger
from patchwork.step import Step, StepStatus


class _GetOverriddenDefaultDict(defaultdict):
    def __init__(self, default_factory):
        super().__init__(default_factory)

    def get(self, key, default=None):
        return self.__missing__(key) if key not in self else self[key]


class ExtractModelResponse(Step):
    required_keys = {"openai_responses"}

    def __init__(self, inputs: dict):
        super().__init__(inputs)
        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.openai_responses = inputs["openai_responses"]
        self.partitions = inputs.get("response_partitions", defaultdict(list))

    def run(self) -> dict:
        if len(self.openai_responses) == 0:
            self.set_status(StepStatus.SKIPPED, "No OpenAI responses to extract from.")
            return dict(extracted_responses=[])

        extracted_response_func = self.response_partitioned_dict
        if len(self.partitions) == 0:
            logger.warn("No partitions specified for model response, will default to using the entire response.")
            extracted_response_func = self.auto_pass_dict

        outputs = []
        for openai_response in self.openai_responses:
            output = extracted_response_func(openai_response)
            outputs.append(output)

        return dict(extracted_responses=outputs)

    def auto_pass_dict(self, openai_response: str) -> dict:
        def default_factory(_=None):
            return openai_response

        return _GetOverriddenDefaultDict(default_factory)

    def response_partitioned_dict(self, openai_response: str) -> dict:
        output = {}
        for key, partition in self.partitions.items():
            if len(partition) < 1:
                output[key] = openai_response
                continue

            extracted_response = openai_response
            for part in partition[:-1]:
                _, _, extracted_response = extracted_response.partition(part)

            if partition[-1] != "":
                extracted_response, _, _ = extracted_response.partition(partition[-1])

            if extracted_response == "":
                continue

            output[key] = extracted_response
        return output
