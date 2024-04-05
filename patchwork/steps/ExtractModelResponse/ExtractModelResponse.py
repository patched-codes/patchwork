from collections import defaultdict

from patchwork.logger import logger
from patchwork.step import Step


class ExtractModelResponse(Step):
    required_keys = {"openai_responses"}

    def __init__(self, inputs: dict):
        logger.info(f"Run started {self.__class__.__name__}")

        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.openai_responses = inputs["openai_responses"]
        self.partitions = inputs.get("response_partitions", defaultdict(list))

    def run(self) -> dict:
        if len(self.partitions) <= 0:
            logger.error("No partitions specified for model response. Exiting.")
            return dict(extracted_responses=[])

        outputs = []
        for openai_response in self.openai_responses:
            output = {}
            for key, partitions in self.partitions.items():
                if len(partitions) < 1:
                    output[key] = openai_response
                    continue

                extracted_response = openai_response
                for partition in partitions[:-1]:
                    _, _, extracted_response = extracted_response.partition(partition)

                if partitions[-1] != "":
                    extracted_response, _, _ = extracted_response.partition(partitions[-1])

                if extracted_response == "":
                    continue

                output[key] = extracted_response
            outputs.append(output)

        logger.info(f"Run completed {self.__class__.__name__}")
        return dict(extracted_responses=outputs)
