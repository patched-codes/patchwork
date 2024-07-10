from patchwork.step import Step
from patchwork.steps.JoinList.typed import JoinListInputs


class JoinList(Step):
    def __init__(self, inputs):
        missing_keys = JoinListInputs.__required_keys__.difference(inputs.keys())
        if len(missing_keys) > 0:
            raise ValueError(f'Missing required data: {missing_keys}')

        self.list = inputs['list']
        self.delimiter = inputs['delimiter']

    def run(self):
        return dict(text=self.delimiter.join(self.list))