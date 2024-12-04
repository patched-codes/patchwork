import re
from pathlib import Path
from typing import Any

from git import Repo
from openai.types.chat import ChatCompletionMessageParam

from patchwork.common.client.llm.aio import AioLlmClient
from patchwork.common.client.llm.protocol import LlmClient
from patchwork.common.constants import TOKEN_URL
from patchwork.step import Step
from patchwork.steps.ResolveIssue.multiturn_strategy.analyze_implement import (
    STAGE,
    AnalyzeImplementStrategy,
)
from patchwork.steps.ResolveIssue.tools.code_edit_tools import CodeEditTool
from patchwork.steps.ResolveIssue.tools.tool import Tool
from patchwork.steps.ResolveIssue.typed import ResolveIssueInputs, ResolveIssueOutputs


class _ResolveIssue(AnalyzeImplementStrategy):
    def __init__(self, repo_path: str, llm_client: LlmClient, issue_description: Any, **kwargs):
        self.tool_set = Tool.get_tools(repo_path=repo_path)
        super().__init__(
            llm_client=llm_client,
            initial_template_data=dict(issue=issue_description),
            analysis_prompt_template="""<uploaded_files>
.
</uploaded_files>
I've uploaded a code repository in the current working directory (not in /tmp/inputs).

Consider the following issue:

<issue_description>
{{issue}}
</issue_description>

Let's first explore and analyze the repository to understand where the issue is located.
Please analyze the repository structure and try to locate the specific files and code sections that need to be modified.

1. First explore the repo structure
2. Identify the relevant files that likely need changes
3. Create and run a script to reproduce the error
4. Once you've confirmed the error, identify the specific code sections that need to be modified

Provide your findings in this format:
<analysis>
<files>List the relevant files that need changes</files>
<error_reproduction>The error reproduction script and its output</error_reproduction>
<changes_needed>Description of the specific changes needed</changes_needed>
</analysis>""",
            implementation_prompt_template="""<uploaded_files>
.
</uploaded_files>
I've uploaded a code repository in the current working directory (not in /tmp/inputs).

Based on our previous analysis:

<previous_analysis>
{{analysis_results}}
</previous_analysis>

Let's implement the necessary changes:

1. Edit the sourcecode of the repo to resolve the issue
2. Rerun the reproduction script to confirm the error is fixed
3. Think about edge cases and make sure your fix handles them as well

I've already taken care of all changes to any of the test files described in the PR. 
This means you DON'T have to modify the testing logic or any of the tests in any way!

Let me know when you're done by outputting </DONE>.""",
            tool_set=self.tool_set,
            **kwargs,
        )

    def extract_analysis_message(self, message: ChatCompletionMessageParam) -> dict[str, str]:
        analysis_match = re.search(r"<analysis>(.*?)</analysis>", message.get("content"), re.DOTALL)
        if not analysis_match:
            return dict()

        content = analysis_match.group(1)
        sections = dict()
        for section in ["files", "error_reproduction", "changes_needed"]:
            section_match = re.search(f"<{section}>(.*?)</{section}>", content, re.DOTALL)
            sections[section] = section_match.group(1).strip() if section_match else ""
        return sections

    def is_stop(self, messages: list[ChatCompletionMessageParam]) -> bool:
        if self._stage != STAGE.IMPLEMENT:
            return False
        last_message = messages[-1]
        return "</DONE>" in last_message.get("content")


class ResolveIssue(Step, input_class=ResolveIssueInputs, output_class=ResolveIssueOutputs):
    def __init__(self, inputs):
        super().__init__(inputs)
        self.base_path = inputs.get("base_path")
        if self.base_path is None:
            repo = Repo(Path.cwd(), search_parent_directories=True)
            self.base_path = repo.working_tree_dir

        llm_client = AioLlmClient.create_aio_client(inputs)
        if llm_client is None:
            raise ValueError(
                f"Model API key not found.\n"
                f'Please login at: "{TOKEN_URL}",\n'
                "Please go to the Integration's tab and generate an API key.\n"
                "Please copy the access token that is generated, "
                "and add `--patched_api_key=<token>` to the command line.\n"
                "\n"
                "If you are using an OpenAI API Key, please set `--openai_api_key=<token>`.\n"
            )
        issue_description = inputs.get("issue_description")

        self.multiturn_llm_call = _ResolveIssue(
            repo_path=self.base_path,
            llm_client=llm_client,
            issue_description=issue_description,
        )

    def run(self):
        self.multiturn_llm_call.execute(limit=100)
        for tool in self.multiturn_llm_call.tool_set.values():
            if isinstance(tool, CodeEditTool):
                return tool.tool_records
        return dict()
