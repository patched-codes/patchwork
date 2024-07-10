from patchwork.step import Step


class JoinList(Step):
    required_keys = {"list", "delimiter"}

    def __init__(self, inputs):
        diff_keys = self.required_keys.difference(inputs.keys())
        if len(diff_keys) > 0:
            raise ValueError(f'Missing required data: {diff_keys}')

        self.list = inputs['list']
        self.delimiter = inputs['delimiter']

    def run(self):
        return dict(text=self.delimiter.join(self.list))