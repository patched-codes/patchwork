from patchwork.step import Step, StepStatus
from patchwork.steps.JoinList.typed import JoinListInputs


class JoinList(Step):
    def __init__(self, inputs):
        super().__init__(inputs)
        missing_keys = JoinListInputs.__required_keys__.difference(inputs.keys())
        if len(missing_keys) > 0:
            raise ValueError(f"Missing required data: {missing_keys}")

        self.list = inputs["list"]
        self.delimiter = inputs["delimiter"]

    def run(self):
        if self.inputs.get("debug") is not None:
            self.debug(self.inputs)
            
        if len(self.list) == 0:
            self.set_status(StepStatus.SKIPPED, "List is empty")
            return dict()

        items = []
        for item in self.list:
            if isinstance(item, str):
                items.append(item)
            elif isinstance(item, dict):
                if "body" in item.keys() or len(item.keys()) < 1:
                    items.append(item.get("body"))
                elif "text" in item.keys():
                    items.append(item.get("text"))
                else:
                    items.append(str(item))
            else:
                items.append(str(item))

        return dict(text=self.delimiter.join(items))
