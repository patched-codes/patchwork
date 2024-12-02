from typing import Annotated
from sanitize import sanitize_input

class CallCommandInputs(__RequiredCallCommandInputs, total=False):
    command_args: str
    working_dir: Annotated[str, StepTypeConfig(is_path=True)]
    env: str

    def __post_init__(self):
        # Sanitize the 'env' string to prevent injection
        self.env = sanitize_input(self.env)
