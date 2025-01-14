import re
import shlex
from pathlib import Path
from typing import Any, Optional

from git import Repo
from git.exc import GitCommandError
from openai.types.chat import ChatCompletionMessageParam

from patchwork.common.client.llm.aio import AioLlmClient
from patchwork.common.client.llm.protocol import LlmClient
from patchwork.common.constants import TOKEN_URL
from patchwork.common.multiturn_strategy.analyze_implement import (
    STAGE,
    AnalyzeImplementStrategy,
)
from patchwork.common.tools import CodeEditTool, Tool
from patchwork.step import Step
from patchwork.steps.FixIssue.typed import FixIssueInputs, FixIssueOutputs


class _ResolveIssue(AnalyzeImplementStrategy):
    def __init__(self, repo_path: str, llm_client: LlmClient, issue_description: Any, **kwargs):
        path = Path(repo_path).resolve()
        self.tool_set = Tool.get_tools(path=path)
        super().__init__(
            llm_client=llm_client,
            initial_template_data=dict(issue=issue_description),
            analysis_prompt_template=f"""\
<uploaded_files>
{path}
</uploaded_files>
I've uploaded a code repository in the current working directory.

Consider the following issue:

<issue_description>
{{{{issue}}}}
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
            implementation_prompt_template=f"""\
<uploaded_files>
{path}
</uploaded_files>
I've uploaded a code repository in the current working directory (not in /tmp/inputs).

Based on our previous analysis:

<previous_analysis>
{{{{analysis_results}}}}
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

    def extract_analysis_message(self, message: ChatCompletionMessageParam) -> Optional[dict[str, str]]:
        analysis_match = re.search(r"<analysis>(.*?)</analysis>", message.get("content"), re.DOTALL)
        if not analysis_match:
            return None

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


class FixIssue(Step, input_class=FixIssueInputs, output_class=FixIssueOutputs):
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

        self.multiturn_llm_call = _ResolveIssue(
            repo_path=self.base_path,
            llm_client=llm_client,
            issue_description=inputs["issue_description"],
        )

    def run(self):
        self.multiturn_llm_call.execute(limit=100)
        for tool in self.multiturn_llm_call.tool_set.values():
            if isinstance(tool, CodeEditTool):
                cwd = Path.cwd()
                modified_files = [file_path.relative_to(cwd) for file_path in tool.tool_records["modified_files"]]
                # Get the diff for each modified file using git
                modified_files_with_diffs = []
                repo = Repo(cwd, search_parent_directories=True)
                for file in modified_files:
                    # Sanitize the file path to prevent command injection
                    safe_file = shlex.quote(str(file))
                    try:
                        # Check if file is tracked by git, even if deleted
                        is_tracked = str(file) in repo.git.ls_files('--', safe_file).splitlines()
                        is_staged = str(file) in repo.git.diff('--cached', '--name-only', safe_file).splitlines()
                        is_unstaged = str(file) in repo.git.diff('--name-only', safe_file).splitlines()
                        
                        if is_tracked or is_staged or is_unstaged:
                            # Get both staged and unstaged changes
                            staged_diff = repo.git.diff('--cached', safe_file) if is_staged else ""
                            unstaged_diff = repo.git.diff(safe_file) if is_unstaged else ""
                            
                            # Combine both diffs
                            combined_diff = staged_diff + ('\n' + unstaged_diff if unstaged_diff else '')
                            
                            if combined_diff.strip():
                                # Validate dictionary structure before adding
                                modified_file = {
                                    "path": str(file),
                                    "diff": combined_diff
                                }
                                # Ensure all required fields are present with correct types
                                if not isinstance(modified_file["path"], str):
                                    raise TypeError(f"path must be str, got {type(modified_file['path'])}")
                                if not isinstance(modified_file["diff"], str):
                                    raise TypeError(f"diff must be str, got {type(modified_file['diff'])}")
                                modified_files_with_diffs.append(modified_file)
                    except GitCommandError as e:
                        # Log the error but continue processing other files
                        print(f"Warning: Failed to generate diff for {safe_file}: {str(e)}")
                        continue
                        
                return dict(modified_files=modified_files_with_diffs)
        return dict()
