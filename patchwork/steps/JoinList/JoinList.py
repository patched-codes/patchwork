import json

from patchwork.step import Step, StepStatus
from patchwork.steps.JoinList.typed import JoinListInputs, JoinListOutputs


class JoinList(Step, input_class=JoinListInputs, output_class=JoinListOutputs):
    def __init__(self, inputs):
        super().__init__(inputs)

        self.list = inputs["list"]
        self.delimiter = inputs["delimiter"]
        self.possible_keys = ["body", "text"]
        if inputs.get("key") is not None:
            self.possible_keys.insert(0, inputs.get("key"))

    def run(self):
        if len(self.list) == 0:
            self.set_status(StepStatus.SKIPPED, "List is empty")
            return dict()

        items = []
        for item in self.list:
            if isinstance(item, str):
                items.append(item)
            elif isinstance(item, dict):
                is_added = False
                for possible_key in self.possible_keys:
                    if possible_key in item.keys():
                        items.append(item.get(possible_key))
                        is_added = True
                        break
                if not is_added:
                    items.append(json.dumps(item))
            else:
                items.append(str(item))

        return dict(text=self.delimiter.join(items))
