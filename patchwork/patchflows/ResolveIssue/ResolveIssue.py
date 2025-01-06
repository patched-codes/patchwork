from pathlib import Path

import yaml

from patchwork.common.utils.progress_bar import PatchflowProgressBar
from patchwork.common.utils.step_typing import validate_steps_with_inputs
from patchwork.step import Step
from patchwork.steps import PR, AgenticLLM, FixIssue, ReadIssues, SimplifiedLLMOnce

_DEFAULT_INPUT_FILE = Path(__file__).parent / "defaults.yml"


class ResolveIssue(Step):
    def __init__(self, inputs: dict):
        PatchflowProgressBar(self).register_steps(
            ReadIssues,
            FixIssue,
            PR,
        )
        final_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text()) or dict()
        final_inputs.update(inputs)

        final_inputs["pr_title"] = f"PatchWork {self.__class__.__name__}"
        final_inputs["branch_prefix"] = f"{self.__class__.__name__.lower()}-"

        validate_steps_with_inputs(
            {"issue_description"}.union(final_inputs.keys()),
            ReadIssues,
            FixIssue,
            PR,
        )

        # currently only support claude
        final_inputs["model"] = "claude-3-5-sonnet-latest"
        self.inputs = final_inputs

    def run(self) -> dict:
        outputs = ReadIssues(self.inputs).run()
        self.inputs["issue_description"] = outputs

        outputs = AgenticLLM(
            dict(
                **self.inputs,
                prompt_value=dict(
                    path=self.inputs.get("base_path", str(Path.cwd())),
                    issue=outputs["issue_description"],
                ),
                system_prompt="""\
You are a senior software engineer tasked to analyze a issue. 
Your analysis will be used to guide the junior engineer to resolve this issue. 
""",
                user_prompt="""\
<uploaded_files>
{{path}}
</uploaded_files>
I've uploaded a code repository in the current working directory.

Consider the following issue:

<issue_description>
{{issue}}
</issue_description>

Let's first explore and analyze the repository to understand where the issue is located.
Please analyze the repository structure and try to locate the specific files and code sections that need to be modified.

1. First explore the repo structure
2. Identify the relevant files that likely need changes
3. Once you've confirmed the error, identify the specific code sections that need to be modified

Provide your findings in this format:
<analysis>
    <files>List the relevant files that need changes</files>
    <changes_needed>Description of the specific changes needed</changes_needed>
</analysis>
            """,
                max_llm_calls=200,
            )
        ).run()
        outputs = SimplifiedLLMOnce(
            dict(
                **self.inputs,
                json_schema=dict(
                    files=["The files to be changed"], changes_needed="Description of the specific changes needed"
                ),
                user_prompt="""\
From the following conversation history extract the following information:
<analysis>
    <files>List the relevant files that need changes</files>
    <changes_needed>Description of the specific changes needed</changes_needed>
</analysis>

<conversation_history>
{{conversation_history}}
</conversation_history>
""",
                prompt_value=outputs,
            )
        ).run()

        outputs = AgenticLLM(
            dict(
                **self.inputs,
                prompt_value=dict(
                    path=self.inputs.get("base_path", str(Path.cwd())),
                    analysis_result=outputs,
                ),
                system_prompt="""\
You are a senior software engineer assigned to fix an issue. Your lead engineer have already analyzed the issue and provided his analysis for you for reference.
""",
                user_prompt="""\
<uploaded_files>
{{path}}
</uploaded_files>
I've uploaded a code repository in the current working directory.

Based on our analysis:

<lead_analysis>
    <files_to_be_changed>
        {{analysis_result.files}}
    </files_to_be_changed>
    <change_description>
        {{analysis_result.changes_needed}}
    </change_description>
</lead_analysis>

Let's implement the necessary changes:

1. Edit the sourcecode of the repo to resolve the issue
2. Think about edge cases and make sure your fix handles them as well

I've already taken care of all changes to any of the test files described in the PR. 
This means you DON'T have to modify the testing logic or any of the tests in any way!
""",
                max_llm_calls=200,
            )
        ).run()
        self.inputs["modified_files"] = outputs["tool_records"]

        outputs = PR(self.inputs).run()
        self.inputs.update(outputs)

        return self.inputs
