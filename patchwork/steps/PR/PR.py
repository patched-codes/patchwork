from patchwork.step import Step
from patchwork.steps.CommitChanges.CommitChanges import CommitChanges
from patchwork.steps.CommitChanges.typed import CommitChangesInputs
from patchwork.steps.CreatePR.CreatePR import CreatePR
from patchwork.steps.CreatePR.typed import CreatePRInputs
from patchwork.steps.PreparePR.PreparePR import PreparePR
from patchwork.steps.PreparePR.typed import PreparePRInputs


class PR(Step):
    required_keys = (
        CreatePRInputs.__required_keys__ |
        CommitChangesInputs.__required_keys__ |
        PreparePRInputs.__required_keys__
    )

    def __init__(self, inputs):
        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.inputs = inputs
        return

    def run(self):
        commit_changes_output = CommitChanges(dict(
            modified_code_files=self.inputs.get("modified_code_files"),
            disable_branch=self.inputs.get("disable_branch"),
            force_branch_creation=self.inputs.get("force_branch_creation"),
            branch_prefix=self.inputs.get("branch_prefix"),
            branch_suffix=self.inputs.get("branch_suffix"),
        )).run()
        prepare_pr_output = PreparePR(dict(
            modified_code_files=self.inputs.get("modified_code_files"),
            pr_header=self.inputs.get("pr_header"),
        )).run()
        create_pr_outputs = CreatePR(dict(
            base_branch=commit_changes_output.get("base_branch"),
            target_branch=commit_changes_output.get("target_branch"),
            pr_body=prepare_pr_output.get("pr_body"),
            pr_title=self.inputs.get("pr_title"),
            force_pr_creation=self.inputs.get("force_pr_creation"),
            disable_pr=self.inputs.get("disable_pr"),
            scm_url=self.inputs.get("scm_url"),
            gitlab_api_key=self.inputs.get("gitlab_api_key"),
            github_api_key=self.inputs.get("github_api_key"),
        )).run()

        return dict(
            base_branch=commit_changes_output.get("base_branch"),
            target_branch=commit_changes_output.get("target_branch"),
            pr_url=create_pr_outputs.get("pr_url"),
            pr_number=create_pr_outputs.get("pr_number"),
            pr_title=prepare_pr_output.get("pr_title"),
            pr_body=prepare_pr_output.get("pr_body")
        )
