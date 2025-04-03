from patchwork.common.utils.progress_bar import PatchflowProgressBar
from patchwork.common.utils.step_typing import validate_steps_with_inputs
from patchwork.step import Step
from patchwork.steps import SlackAgent


class TestSlackAgent(Step):
    def __init__(self, inputs: dict):
        PatchflowProgressBar(self).register_steps(
            SlackAgent,
        )

        # Validate required inputs
        if "slack_bot_token" not in inputs:
            raise ValueError("slack_bot_token is required")
        if "user_prompt" not in inputs:
            raise ValueError("user_prompt is required")
        if "prompt_value" not in inputs:
            raise ValueError("prompt_value is required")

        # Validate step inputs
        validate_steps_with_inputs(
            set(inputs.keys()),
            SlackAgent,
        )

        self.inputs = inputs

    def run(self) -> dict:
        # Run the SlackAgent step
        outputs = SlackAgent(self.inputs).run()
        self.inputs.update(outputs)

        return self.inputs 