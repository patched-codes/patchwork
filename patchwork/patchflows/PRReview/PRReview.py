from pathlib import Path

import yaml

from patchwork.common.utils.progress_bar import PatchflowProgressBar
from patchwork.common.utils.step_typing import validate_steps_with_inputs
from patchwork.step import Step
from patchwork.steps import CreatePRComment, ReadPRDiffs, SimplifiedLLMOnce

_DEFAULT_PROMPT_JSON = Path(__file__).parent / "pr_review_prompt.json"
_DEFAULT_INPUT_FILE = Path(__file__).parent / "defaults.yml"


class PRReview(Step):
    def __init__(self, inputs: dict):
        PatchflowProgressBar(self).register_steps(
            ReadPRDiffs,
            SimplifiedLLMOnce,
            CreatePRComment,
        )
        final_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text())
        final_inputs.update(inputs)

        validate_steps_with_inputs(
            set(final_inputs.keys()).union(
                {
                    "user_prompt",
                    "prompt_value",
                    "json_schema",
                    "pr_comment",
                }
            ),
            ReadPRDiffs,
            SimplifiedLLMOnce,
            CreatePRComment,
        )

        self.inputs = final_inputs

    def run(self) -> dict:
        pr_diffs_outputs = ReadPRDiffs(self.inputs).run()

        reviews = []
        for diffs in iter(pr_diffs_outputs["diffs"]):
            llm1_outputs = SimplifiedLLMOnce(
                dict(
                    prompt_value=diffs,
                    user_prompt="""\
Analyze the following code diff against the provided rules:

<CODE_DIFF>
{{diff}}
</CODE_DIFF>

<RULES>
- Do not ignore potential bugs in the code.
- Do not overlook possible security vulnerabilities introduced by code modifications.
- Do not deviate from the original coding standards established in the pull request.
</RULES>

For each rule, determine if there\'s a violation. Use the following chain of thought process:

1. Understand the rule
2. Examine the diff line by line
3. Identify any potential violations
4. Determine the specific line numbers of violations
5. Summarize your findings

Rule 1:
1. Rule understanding: [Briefly explain the rule]
2. Diff examination: [Describe how you\'re examining the diff]
3. Potential violations: [List any potential violations you\'ve identified]
4. Line numbers: [If violations exist, list the specific line numbers]
5. Summary: [Summarize your findings for this rule]

Rule 2:
[Repeat the above structure for each rule]

Now, carefully review your reasoning in the section above. Ensure that your conclusions are consistent with the analysis you\'ve done for each rule.

Your review should have the following markdown format:

<REVIEW_FORMAT>
## File Changed: `{{path}}`

Details: [If rule violation include brief prescriptive explanation]

Affected Code Snippet: 
[Original code enclosed in a code block from the file that is affected by this violation. If no violation, write "N/A"]

Start Line: [Starting Line number of the affected code. If no violation, write "N/A"]

End Line: [Ending Line number of the affected code. If no violation, write "N/A"]

-------------

Details: [If rule violation include brief prescriptive explanation]

Affected Code Snippet: 
[Original code enclosed in a code block from the file that is affected by this violation. If no violation, write "N/A"]

Start Line: [Starting Line number of the affected code. If no violation, write "N/A"]

End Line: [Ending Line number of the affected code. If no violation, write "N/A"]

-------------

... (continue for all rules)
</REVIEW_FORMAT>

Ensure that you include all rules in your response, even if there\'s no violation. The output should directly reflect the reasoning in your thinking section.
""",
                    json_schema={"review": "The markdown text of the reviews"},
                    **self.inputs,
                )
            ).run()

            llm2_outputs = SimplifiedLLMOnce(
                dict(
                    prompt_value=llm1_outputs,
                    user_prompt="""\
You are a software manager compiling code reviews from all teams. You are given a list of code reviews. You have to remove code reviews that is either not actionable or useful. Do not change the accepted reviews, return the original review for the response. Do not remove the path from the review.

<code_reviews>
{{review}}
<code_reviews>

You should return an empty response if there are no code reviews that is actionable or useful.
""",
                    json_schema={"review": "The reviews curated"},
                    **self.inputs,
                )
            ).run()

            review = llm2_outputs.get("review")
            if review is not None and len(str(review)) > 0:
                reviews.append(review)

        if len(reviews) > 0:
            reviews_str = "\n".join(reviews)
        else:
            reviews_str = "No issues found."

        return CreatePRComment(dict(pr_comment=reviews_str, **self.inputs)).run()
