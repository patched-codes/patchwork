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
        commit_changes_output = CommitChanges(
            dict(
                modified_code_files=self.inputs.get("modified_code_files"),
                disable_branch=self.inputs.get("disable_branch"),
                force_branch_creation=self.inputs.get("force_branch_creation"),
                branch_prefix=self.inputs.get("branch_prefix"),
                branch_suffix=self.inputs.get("branch_suffix"),
            )
        ).run()
        prepare_pr_output = PreparePR(
            dict(
                modified_code_files=self.inputs.get("modified_code_files"),
                pr_header=self.inputs.get("pr_header"),
            )
        ).run()
        create_pr_outputs = CreatePR(
            dict(
                base_branch=commit_changes_output.get("base_branch"),
                target_branch=commit_changes_output.get("target_branch"),
                pr_body=prepare_pr_output.get("pr_body"),
                pr_title=self.inputs.get("pr_title"),
                force_pr_creation=self.inputs.get("force_pr_creation"),
                disable_pr=self.inputs.get("disable_pr"),
                scm_url=self.inputs.get("scm_url"),
                gitlab_api_key=self.inputs.get("gitlab_api_key"),
                github_api_key=self.inputs.get("github_api_key"),
            )
        ).run()

        return dict(
            base_branch=commit_changes_output.get("base_branch"),
            target_branch=commit_changes_output.get("target_branch"),
            pr_url=create_pr_outputs.get("pr_url"),
            pr_number=create_pr_outputs.get("pr_number"),
            pr_title=prepare_pr_output.get("pr_title"),
            pr_body=prepare_pr_output.get("pr_body"),
        )
