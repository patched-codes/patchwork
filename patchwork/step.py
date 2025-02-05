import abc
import os
import sys

# modules required for keyboard input
if os.name == "nt":  # in case of windows
    import msvcrt
else:  # for unix based systems
    import termios
    import tty

from enum import Enum

from typing_extensions import (
    Any,
    Collection,
    Dict,
    List,
    Optional,
    Type,
    Union,
    is_typeddict,
)

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
        missing_keys = self.find_missing_inputs(inputs)
        if len(missing_keys) > 0:
            raise ValueError(f"Missing required data: {list(missing_keys)}")

        # store the inputs
        self.inputs = inputs

        # record step name for later use
        self.__step_name = self.__class__.__name__

        # initialize the status of the step
        self.__status = StepStatus.COMPLETED
        self.__status_msg = None

        # abit of a hack to wrap the implemented run method
        self.original_run = self.run
        self.run = self.__managed_run

    def __init_subclass__(cls, input_class: Optional[Type] = None, output_class: Optional[Type] = None, **kwargs):
        input_class = input_class or getattr(cls, "input_class", None)
        if input_class is not None and not is_typeddict(input_class):
            input_class = None

        output_class = output_class or getattr(cls, "output_class", None)
        if output_class is not None and not is_typeddict(output_class):
            output_class = None

        cls._input_class = input_class
        cls._output_class = output_class

    @classmethod
    def find_missing_inputs(cls, inputs: DataPoint) -> Collection:
        if getattr(cls, "_input_class", None) is None:
            return []
        return cls._input_class.__required_keys__.difference(inputs.keys())

    def __managed_run(self, *args, **kwargs) -> Any:
        self.debug(self.inputs)
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
        self.__status = status
        self.__status_msg = msg
        if status.priority >= self.__status.priority:
            self.__status = status
            self.__status_msg = msg

    def get_key(self):
        if os.name == "nt":  # Windows
            return msvcrt.getch().decode("utf-8")
        else:  # Linux / macOS
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                key = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return key

    def debug(self, inputs):
        if inputs.get("debug") is None or inputs.get("debug") is False:
            return
        logger.info("\nInputs:")
        MAX_LENGTH = 1000  # Max limit to print inputs
        printed_chars = 0
        for key, value in inputs.items():
            if "api_key" in key.lower():
                value = "<masked api key>"
            input_val = f"{key}: {value}"
            if printed_chars + len(input_val) > MAX_LENGTH:
                continue
            else:
                printed_chars += len(input_val)
                logger.info(input_val)
        logger.info("\n")
        logger.info("Press enter to continue, any other key to exit...\n")
        key = self.get_key()
        if key == "\n" or key == "\r":
            logger.info("Continuing...\n")
        else:
            logger.info("Exiting...\n")
            exit()

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
