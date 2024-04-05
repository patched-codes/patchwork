# Creating a Step in Patchwork

A step's name is ideally expected to be a verb with two words, e.g. "Run Example".

To create a step to to "Run example":

1. Create a file `patchwork/steps/RunExample/RunExample.py`.
    Any additional files required for the `RunExample` should be placed in the same folder.

2.  In `RunExample.py`, implement the class `RunExample` which inherits the `Step` from the `patchwork.step` module. The class `RunExample` is expected to have two methods:
    - `__init__`: The constructor of the class. It should accept an `inputs` dictionary as an argument. This dictionary contains the input data for the step. Checking of the presence and validity of the input data should be done here.
    - `run`: The main method of the class. This method should contain the logic of the step and return a dictionary with the results.

3. Update `patchwork/steps/__init__.py` to include the new step in the list of available steps.

## Example

### Path: `patchwork/steps/RunExample/RunExample.py`

```python
from patchwork.step import Step


class RunExample(Step):
    required_keys = ['input1', 'input2']

    def __init__(self, inputs):
        super().__init__(inputs)
        for key in self.required_keys:
            if key not in inputs:
                raise ValueError(f"Missing required input: {key}")

        self.input1 = inputs['input1']
        self.input2 = inputs['input2']

    def run(self) -> dict:
        return {
            'output1': "example output",
        }
```

### Path: `patchwork/steps/__init__.py`

```python
from .RunExample.RunExample import RunExample

__all__ = [
    ...
    'RunExample',
]
```
