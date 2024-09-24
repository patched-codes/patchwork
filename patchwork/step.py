import abc
from enum import auto, IntFlag, Enum

from typing_extensions import Any, Dict, List, Union, is_typeddict, Optional

from patchwork.logger import logger

DataPoint = Dict[str, Union[str, int, float, bool, "OneOrMore"]]
OneOrMoreDataPoint = Union[DataPoint, List[DataPoint]]


class StepStatus(Enum):
    COMPLETED = (1, logger.info)
    SKIPPED = (2, logger.warning)
    WARNING = (3, logger.warning)
    FAILED = (4, logger.error)

    def __init__(self, priority: int, logger_func):
        self.priority = priority
        self._logger = logger_func

    def __str__(self):
        return self.name.lower()

    @classmethod
    def values(cls):
        return list(StepStatus.__members__.values())


class Step(abc.ABC):
    def __init__(self, inputs: DataPoint):
        """
        Initializes the step.
        :param inputs: a dictionary of inputs
        """

        # check if the inputs have the required keys
        if self.__input_class is not None:
            missing_keys = self.__input_class.__required_keys__.difference(inputs.keys())
            if len(missing_keys) > 0:
                raise ValueError(f"Missing required data: {list(missing_keys)}")

        # record step name for later use
        self.__step_name = self.__class__.__name__

        # initialize the status of the step
        self.__status = StepStatus.COMPLETED
        self.__status_msg = None

        # abit of a hack to wrap the implemented run method
        self.original_run = self.run
        self.run = self.__managed_run

    def __init_subclass__(cls, **kwargs):
        input_class = kwargs.get("input_class", None) or getattr(cls, "input_class", None)
        output_class = kwargs.get("output_class", None) or getattr(cls, "output_class", None)

        if input_class is not None and is_typeddict(input_class):
            cls.__input_class = input_class
        else:
            cls.__input_class = None

        if output_class is not None and is_typeddict(output_class):
            cls.__output_class = output_class
        else:
            cls.__output_class = None

    def __managed_run(self, *args, **kwargs) -> Any:
        logger.info(f"Run started {self.__step_name}")

        exc = None
        try:
            output = self.original_run(*args, **kwargs)
        except Exception as e:
            exc = e

        if self.__status_msg is not None:
            self.__status._logger(f"Step {self.__step_name} message: {self.__status_msg}")

        if exc is not None:
            logger.error(f"Step {self.__step_name} failed")
            raise exc

        if self.__status == StepStatus.FAILED:
            raise ValueError(f"Step {self.__step_name} failed")

        logger.info(f"Run {self.__status} {self.__step_name}")
        return output

    def set_status(self, status: StepStatus, msg: Optional[str] = None):
        if status not in StepStatus.values():
            raise ValueError(f"Invalid status: {status}")

        if status.priority >= self.__status.priority:
            self.__status = status
            self.__status_msg = msg

    @property
    def status(self) -> StepStatus:
        return self.__status

    @property
    def status_message(self) -> Optional[str]:
        return self.__status_msg

    @abc.abstractmethod
    def run(self) -> DataPoint:
        """
        Runs the step.
        :return: a dictionary of outputs
        """
        ...
