from pathlib import Path

import yaml

from patchwork.step import Step
from patchwork.steps import (
    CreateIssueComment,
    GenerateCodeRepositoryEmbeddings,
    QueryEmbeddings,
    ReadIssues,
)

_DEFAULT_INPUT_FILE = Path(__file__).parent / "defaults.yml"


class ResolveIssue(Step):
    def __init__(self, inputs: dict):
        final_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text())
        if final_inputs is None:
            final_inputs = {}
        final_inputs.update(inputs)

        self.inputs = final_inputs

    def run(self) -> dict:
        outputs = GenerateCodeRepositoryEmbeddings(self.inputs).run()
        self.inputs.update(outputs)

        outputs = ReadIssues(self.inputs).run()
        self.inputs.update(outputs)

        self.inputs["texts"] = self.inputs["issue_text"]

        outputs = QueryEmbeddings(self.inputs).run()
        self.inputs.update(outputs)

        issue_list_text = "* " + "\n* ".join([result["path"] for result in self.inputs["embedding_results"]])
        self.inputs[
            "issue_text"
        ] = f"""\
The following files in the repository may be relevant to the issue:

------

{issue_list_text}
"""

        outputs = CreateIssueComment(self.inputs).run()
        self.inputs.update(outputs)

        return self.inputs
