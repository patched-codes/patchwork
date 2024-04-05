# Creating a Patchflow

A patchflow is a collection of steps that are executed in a specific order. The steps are executed in a sequence and the output of one step is used as the input of the next step.

To create a patchflow "my patchflow", do the following:

1. Create `patchwork/patchflows/MyPatchflow/MyPatchflow.py`
   Any additional files required for the `MyPatchflow` should be placed in the same folder.

2. `MyPatchflow.py` implement the class `MyPatchflow` which inherits the `Step` from the `patchwork.step` module. The class `MyPatchflow` is expected to have two methods:
    - `__init__`: The constructor of the class. It should accept an `inputs` dictionary as an argument, which contains user specified inputs for the patchflow. In the absence of user specified inputs, default inputs should be specified where feasible. Validation and processing of the inputs should be done here.
    - `run`: The main method of the class. This method should contain the logic of the patchflow which executes a sequence of `Steps` in a specific order and returns a dictionary with the results. Each step's output should be updated in the `inputs` dictionary and passed to the next step.

3. Update `patchwork/patchflows/__init__.py` to include the new patchflow by importing the class `MyPatchflow` and adding it to `__all__`.

## Example

### Path: `patchwork/patchflows/MyPatchflow/MyPatchflow.py`

```python
from patchwork.step import Step
from patchwork.steps import

{
    Step1,
    Step2,
    Step3
}


class MyPatchflow(Step):
    def __init__(self, inputs):
        super().__init__(inputs)

        if 'input1' not in inputs:
            raise ValueError("Missing required input: input1")

        self.inputs = inputs

    def run(self) -> dict:
        out1 = Step1(self.inputs).run()
        self.inputs.update(out1)

        out2 = Step2(self.inputs).run()
        self.inputs.update(out2)

        out3 = Step3(self.inputs).run()
        self.inputs.update(out3)

        return self.inputs
```

### Path: `patchwork/patchflows/__init__.py`

```python
from .MyPatchflow.MyPatchflow import MyPatchflow

__all__ = [
    ...
    'MyPatchflow',
]
```
