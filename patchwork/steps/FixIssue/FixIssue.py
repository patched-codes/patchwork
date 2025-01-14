import difflib
import re
from pathlib import Path
from typing import Any, Optional

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
        """Initialize the FixIssue step.
        
        Args:
            inputs: Dictionary containing input parameters including:
                - base_path: Optional path to the repository root
                - Other LLM-related parameters
        """
        super().__init__(inputs)
        base_path = inputs.get("base_path")
        # Handle base_path carefully to avoid type issues
        if base_path is not None:
            self.base_path = str(Path(str(base_path)).resolve())
        else:
            self.base_path = str(Path.cwd())

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
        """Execute the FixIssue step.
        
        This method:
        1. Executes the multi-turn LLM conversation to analyze and fix the issue
        2. Tracks file modifications made by the CodeEditTool
        3. Generates in-memory diffs for all modified files
        
        Returns:
            dict: Dictionary containing list of modified files with their diffs
        """
        self.multiturn_llm_call.execute(limit=100)
        for tool in self.multiturn_llm_call.tool_set.values():
            if isinstance(tool, CodeEditTool):
                cwd = Path.cwd()
                modified_files = [file_path.relative_to(cwd) for file_path in tool.tool_records["modified_files"]]
                # Generate diffs for modified files using in-memory comparison
                modified_files_with_diffs = []
                file_contents = {}  # Store original contents before modifications
                
                # First pass: store original contents
                for file in modified_files:
                    file_path = Path(file)
                    try:
                        if file_path.exists():
                            file_contents[str(file)] = file_path.read_text()
                        else:
                            file_contents[str(file)] = ""
                    except (OSError, IOError) as e:
                        print(f"Warning: Failed to read original content for {file}: {str(e)}")
                        file_contents[str(file)] = ""
                
                # Apply modifications through CodeEditTool (happens in the background)
                
                # Second pass: generate diffs
                for file in modified_files:
                    file_path = Path(file)
                    try:
                        # Get current content after modifications
                        current_content = file_path.read_text() if file_path.exists() else ""
                        original_content = file_contents.get(str(file), "")
                        
                        # Generate unified diff
                        fromfile = f"a/{file}"
                        tofile = f"b/{file}"
                        diff = "".join(difflib.unified_diff(
                            original_content.splitlines(keepends=True),
                            current_content.splitlines(keepends=True),
                            fromfile=fromfile,
                            tofile=tofile
                        ))
                        
                        if diff:  # Only add if there are actual changes
                            modified_file = {
                                "path": str(file),
                                "diff": diff
                            }
                            modified_files_with_diffs.append(modified_file)
                    except (OSError, IOError) as e:
                        print(f"Warning: Failed to generate diff for {file}: {str(e)}")
                        continue
                
                return dict(modified_files=modified_files_with_diffs)
        return dict()
