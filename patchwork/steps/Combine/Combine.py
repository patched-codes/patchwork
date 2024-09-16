import itertools

from patchwork.step import Step
from patchwork.steps.Combine.typed import CombineInputs


class Combine(Step):
    def __init__(self, inputs):
        """Initialize the CombineInputs object.
        
        Args:
            inputs (dict): A dictionary containing the required input data.
        
        Returns:
            None
        
        Raises:
            """Merges two JSON objects or lists of JSON objects.
            
            Args:
                self: The instance of the class containing base and update attributes.
            
            Returns:
                dict or list: The merged result. If both inputs are dictionaries, returns a merged dictionary.
                If both inputs are lists, returns a list of merged dictionaries. If one input is a list and 
                the other is a dictionary, returns a list where each element of the list is merged with the dictionary.
            """
            ValueError: If any required keys are missing from the inputs dictionary.
        """
        super().__init__(inputs)
        missing_keys = CombineInputs.__required_keys__.difference(inputs.keys())
        if len(missing_keys) > 0:
            raise ValueError(f"Missing required data: {missing_keys}")

        self.base = inputs["base_json"]
        self.update = inputs["update_json"]

    def run(self):
        base_list = isinstance(self.base, list)
        update_list = isinstance(self.update, list)
        if not base_list and not update_list:
            return {**self.base, **self.update}

        if base_list and update_list:
            final_output = []
            for item_1, item_2 in itertools.zip_longest(self.base, self.update):
                if item_1 is None:
                    final_output.append(item_2)
                elif item_2 is None:
                    final_output.append(item_1)
                else:
                    final_output.append({**item_1, **item_2})
            return dict(result_json=final_output)

        if base_list:
            list_json = self.base
            additional_json = self.update
            combiner = lambda base, update: {**base, **update}
        else:
            list_json = self.update
            additional_json = self.base
            combiner = lambda update, base: {**base, **update}

        return dict(result_json=[combiner(item, additional_json) for item in list_json])
