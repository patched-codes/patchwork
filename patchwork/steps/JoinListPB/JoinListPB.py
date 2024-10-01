from patchwork.step import Step
from patchwork.steps import JoinList
from patchwork.steps.JoinListPB.typed import JoinListPBInputs, JoinListPBOutputs


class JoinListPB(Step, input_class=JoinListPBInputs, output_class=JoinListPBOutputs):
    def __init__(self, inputs):
        super().__init__(inputs)
        self.inputs = inputs

        self.key = inputs["key"]
        self.list = inputs["list"]
        self.inputs = inputs

    def run(self):
        join_list = JoinList(
            {
                **self.inputs,
                "list": [item.get(self.key) for item in self.list if item.get(self.key) is not None],
            }
        )
        join_list_output = join_list.run()

        return dict(text=join_list_output.get("text"))
