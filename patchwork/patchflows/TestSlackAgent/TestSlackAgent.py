from patchwork.common.utils.progress_bar import PatchflowProgressBar
from patchwork.common.utils.step_typing import validate_steps_with_inputs
from patchwork.step import Step
from patchwork.steps import SlackAgent
import json


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

        # Convert prompt_value to dictionary if it's a string
        if isinstance(inputs["prompt_value"], str):
            try:
                inputs["prompt_value"] = json.loads(inputs["prompt_value"])
            except json.JSONDecodeError:
                raise ValueError("prompt_value must be a valid JSON string or dictionary")

        # If using Google API, specify a supported model
        if "google_api_key" in inputs and "model" not in inputs:
            inputs["model"] = "gemini-pro"  # Use a supported Google model
            
        # Add example_json for reading channel messages if the prompt is about reading messages
        if "Read" in inputs.get("user_prompt", "") and "messages" in inputs.get("user_prompt", "").lower():
            inputs["example_json"] = {
                "make_api_request": {
                    "url": "https://slack.com/api/conversations.history",
                    "method": "GET",
                    "params": {
                        "channel": inputs["prompt_value"].get("channel", "")
                    }
                }
            }

        # Validate step inputs
        validate_steps_with_inputs(
            set(inputs.keys()),
            SlackAgent,
        )

        self.inputs = inputs

    def run(self) -> dict:
        try:
            # Run the SlackAgent step
            outputs = SlackAgent(self.inputs).run()
            self.inputs.update(outputs)
            
            # Check if we have a slack_response indicating success despite API error
            if "slack_response" in outputs and outputs["slack_response"].get("ok", False):
                print("Message sent successfully to Slack!")
            
            return self.inputs
        except Exception as e:
            # If the error contains information about a successful Slack API call
            print(e)