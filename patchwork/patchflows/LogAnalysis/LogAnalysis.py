import json
import os
from pathlib import Path

import yaml

from patchwork.common.utils.progress_bar import PatchflowProgressBar
from patchwork.common.utils.step_typing import validate_steps_with_inputs
from patchwork.logger import logger
from patchwork.step import Step
from patchwork.steps import AgenticLLMV2

_DEFAULT_INPUT_FILE = Path(__file__).parent / "defaults.yml"


class LogAnalysis(Step):
    def __init__(self, inputs: dict):
        PatchflowProgressBar(self).register_steps(
            AgenticLLMV2,
        )
        final_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text()) or dict()
        final_inputs.update(inputs)

        validate_steps_with_inputs(
            set(final_inputs.keys()).union({""}),
            AgenticLLMV2,
        )

        self.inputs = final_inputs

    def run(self) -> dict:
        for i in range(self.inputs.get("analysis_limit") or 5):
            # for i in range(self.inputs.get("log_finding_limit") or sys.maxsize):
            logs_detection_output = AgenticLLMV2(
                dict(
                    max_agent_calls=5,
                    agent_system_prompt="""\
You are a Senior software engineer trying to debug a issue. 
You are provided with the relevant logs in files in the current directory.
Explore the logs and reply with the relevant logs position, the file path and line number.  
""",
                    user_prompt=f"""\
Logs are uploaded to the current working directory at {os.getcwd()}.

{self.inputs.get('query')}
""",
                    example_json="""
{
  "logs":[
    {
        "file_path": "path to log file", 
        "line_number": 10
    }
  ]
}
""",
                    **self.inputs,
                )
            ).run()

            analysis_output = AgenticLLMV2(
                dict(
                    max_agent_calls=5,
                    prompt_value=logs_detection_output,
                    agent_system_prompt="""\
You are a senior software engineer trying to debug a issue. 
You are provided with file paths and their line number.
Review the logs and analyze if the logs are relevant or enough to debug the issue.
If the provided logs are enough set 'is_log_analysis_done' to true.
""",
                    user_prompt="""\
Should we reevaluate the logs:
{{logs}}
""",
                    example_json="""\
{
  "message": "Message about missing or irrelevant logs to analyze or a success message", 
  "is_log_analysis_done": true
}
""",
                    **self.inputs,
                )
            ).run()

            if analysis_output.get("is_log_analysis_done", False):
                break

        logger.info("Log Analysis Complete")
        logger.info("Message:")
        logger.info(json.dumps(analysis_output.get("message")))
        return dict()
