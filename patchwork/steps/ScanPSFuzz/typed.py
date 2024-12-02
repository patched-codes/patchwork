import os
from typing import TypedDict
from typing_extensions import Annotated

class StepTypeConfig:
    def __init__(self, is_path=False, is_config=False):
        self.is_path = is_path
        self.is_config = is_config

class __RequiredScanPSFuzzInputs(TypedDict):
    prompt_file_path: Annotated[str, StepTypeConfig(is_path=True)]
    openai_api_key: Annotated[str, StepTypeConfig(is_config=False)]

    @staticmethod
    def get_openai_api_key() -> str:
        return os.getenv('OPENAI_API_KEY')
    stdout_output: str
