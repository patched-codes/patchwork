import itertools

from patchwork.step import Step, StepStatus
from patchwork.steps.JoinList.typed import JoinListInputs


class Combine(Step):
    def __init__(self, inputs):
        super().__init__(inputs)
        missing_keys = JoinListInputs.__required_keys__.difference(inputs.keys())
        if len(missing_keys) > 0:
            raise ValueError(f"Missing required data: {missing_keys}")

        self.json_1 = inputs["json_1"]
        self.json_2 = inputs["json_2"]

    def run(self):
        is_json_1_list = isinstance(self.json_1, list)
        is_json_2_list = isinstance(self.json_2, list)
        if not is_json_1_list and not is_json_2_list:
            return dict(result_json={**self.json_1, **self.json_2})

        if is_json_1_list and is_json_2_list:
            final_output = []
            for item_1, item_2 in itertools.zip_longest(self.json_1, self.json_2):
                if item_1 is None:
                    final_output.append(item_2)
                elif item_2 is None:
                    final_output.append(item_1)
                else:
                    final_output.append({**item_1, **item_2})
            return dict(result_json=final_output)

        if is_json_1_list:
            list_json = self.json_1
            additional_json = self.json_2
        else:
            list_json = self.json_2
            additional_json = self.json_1

        return dict(result_json=[{**item, **additional_json} for item in list_json])

