import os

from openai import OpenAI

from patchwork.logger import logger
from patchwork.step import Step
from interpreter import interpreter

class CallOpenAI(Step):
    required_keys = {"openai_api_key"}

    def __init__(self, inputs: dict):
        logger.info(f"Run started {self.__class__.__name__}")

        # Set 'openai_key' from inputs or environment if not already set
        inputs.setdefault("openai_api_key", os.environ.get("OPENAI_API_KEY"))

        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.model = inputs["model"]
        self.model_args = {key[len("model_") :]: value for key, value in inputs.items() if key.startswith("model_")}
        self.client_args = {key[len("client_") :]: value for key, value in inputs.items() if key.startswith("client_")}

        self.openai_api_key = inputs["openai_api_key"]
        interpreter.llm.model = self.model
        interpreter.llm.api_key = self.openai_api_key

    def run(self) -> dict:
        
        interpreter.chat() 

        logger.info(f"Run completed {self.__class__.__name__}")
        return dict({})
