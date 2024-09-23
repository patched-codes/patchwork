import abc
from enum import Flag, auto
import sys
import os

# modules required for keyboard input
if os.name == 'nt':  # in case of windows
    import msvcrt
else: # for unix based systems
    import termios
    import tty

from typing_extensions import Any, Dict, List, Union, is_typeddict

from patchwork.logger import logger

DataPoint = Dict[str, Union[str, int, float, bool, "OneOrMore"]]
OneOrMoreDataPoint = Union[DataPoint, List[DataPoint]]


class StepStatus(Flag):
    COMPLETED = auto()
    FAILED = auto()
    SKIPPED = auto()

    def __str__(self):
        return self.name.lower()


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

        is_fail = self.__status == StepStatus.FAILED or exc is not None
        if self.__status_msg is not None:
            message_logger = logger.error if is_fail else logger.info
            message_logger(f"Step {self.__step_name} message: {self.__status_msg}")

        if exc is not None:
            logger.error(f"Step {self.__step_name} failed")
            raise exc

        if is_fail:
            raise ValueError(f"Step {self.__step_name} failed")

        logger.info(f"Run {self.__status} {self.__step_name}")
        return output

    def set_status(self, status: StepStatus, msg: str = None):
        if status not in StepStatus:
            raise ValueError(f"Invalid status: {status}")
        self.__status = status
        self.__status_msg = msg
    
    def get_key(self):
        if os.name == 'nt':  # Windows
            return msvcrt.getch().decode('utf-8')
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
        logger.info("\nInputs:")
        MAX_LENGTH = 1000 # Max limit to print inputs
        printed_chars = 0
        for key, value in inputs.items():
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
        

    @property
    def status(self) -> StepStatus:
        return self.__status

    @abc.abstractmethod
    def run(self) -> OneOrMoreDataPoint:
        """
        Runs the step.
        :return: a dictionary of outputs
        """
        ...
