from patchwork.common.utils.utils import exclude_none_dict
from patchwork.step import Step
from patchwork.steps.CommitChanges.CommitChanges import CommitChanges
from patchwork.steps.CreatePR.CreatePR import CreatePR
from patchwork.steps.PR.typed import PRInputs
from patchwork.steps.PreparePR.PreparePR import PreparePR


class PR(Step):
    required_keys = PRInputs.__required_keys__

    def __init__(self, inputs):
        missing_keys = self.required_keys.difference(set(inputs.keys()))
        if len(missing_keys) > 0:
            raise ValueError(f'Missing required data: "{missing_keys}"')

        self.inputs = inputs
        return

    def run(self):
        commit_changes_output = CommitChanges(self.inputs).run()
        prepare_pr_output = PreparePR(self.inputs).run()
        create_pr_outputs = CreatePR(
            dict(
                base_branch=commit_changes_output.get("base_branch"),
                target_branch=commit_changes_output.get("target_branch"),
                pr_body=prepare_pr_output.get("pr_body"),
                **self.inputs,
            )
        ).run()

        return exclude_none_dict(dict(
            base_branch=commit_changes_output.get("base_branch"),
            target_branch=commit_changes_output.get("target_branch"),
            pr_url=create_pr_outputs.get("pr_url"),
            pr_number=create_pr_outputs.get("pr_number"),
            pr_title=prepare_pr_output.get("pr_title"),
            pr_body=prepare_pr_output.get("pr_body"),
        ))
