import abc
from enum import Flag, auto

from patchwork.logger import logger


class StepStatus(Flag):
    COMPLETED = auto()
    FAILED = auto()
    SKIPPED = auto()

    def __str__(self):
        return self.name.lower()


class Step(abc.ABC):
    def __init__(self, inputs: dict):
        """
        Initializes the step.
        :param inputs: a dictionary of inputs
        """
        self.__status = StepStatus.COMPLETED
        self.__status_msg = None
        self.__step_name = self.__class__.__name__
        # abit of a hack to wrap the implemented run method
        self.original_run = self.run
        self.run = self.__managed_run

    def __managed_run(self, *args, **kwargs):
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

    @abc.abstractmethod
    def run(self) -> dict:
        """
        Runs the step.
        :return: a dictionary of outputs
        """
        ...
