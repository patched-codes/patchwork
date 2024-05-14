from typing_extensions import Protocol


class Step(Protocol):
    """
    Protocol for a Step.
    Steps do not have to inherit from this class, but they must implement the run method.
    The __init__ method should have a single argument, inputs, which is a dictionary of inputs.
    This is the only opportunity to set the inputs as a class property to be used in `run`.
    """

    def run(self) -> dict:
        """
        Runs the step.
        :return: a dictionary of outputs
        """
        ...
