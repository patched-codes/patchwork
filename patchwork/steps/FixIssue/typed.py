from typing_extensions import Annotated, Dict, List, TypedDict

from patchwork.common.constants import TOKEN_URL
from patchwork.common.utils.step_typing import StepTypeConfig


class __FixIssueRequiredInputs(TypedDict):
    issue_description: str


class FixIssueInputs(__FixIssueRequiredInputs, total=False):
    base_path: Annotated[str, StepTypeConfig(is_path=True)]
    openai_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key", "anthropic_api_key"])
    ]
    anthropic_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key", "openai_api_key"])
    ]
    patched_api_key: Annotated[
        str,
        StepTypeConfig(
            is_config=True,
            or_op=["openai_api_key", "google_api_key", "anthropic_api_key"],
            msg=f"""\
Model API key not found.
Please login at: "{TOKEN_URL}"
Please go to the Integration's tab and generate an API key.
Please copy the access token that is generated, and add `--patched_api_key=<token>` to the command line.

If you are using a OpenAI API Key, please set `--openai_api_key=<token>`.""",
        ),
    ]
    google_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "openai_api_key", "anthropic_api_key"])
    ]


class ModifiedFile(TypedDict):
    """Represents a file that has been modified by the FixIssue step.
    
    Attributes:
        path: The relative path to the modified file from the repository root
        diff: A unified diff string showing the changes made to the file.
              The diff includes both staged and unstaged changes, and is
              generated using git diff commands with proper path sanitization.
    """
    path: str
    diff: str

class FixIssueOutputs(TypedDict):
    modified_files: List[ModifiedFile]
