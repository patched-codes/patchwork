import logging
import os

import click
from typing_extensions import Callable

from patchwork.managed_files import HOME_FOLDER, LOG_FILE

# default noop logger
logger = logging.getLogger("patched")
_noop = logging.NullHandler()
logger.addHandler(_noop)


class ClickHandler(logging.Handler):
    def __init__(self, log_level: str):
        super().__init__()
        self.addFilter(self._get_filter(log_level))

    def emit(self, record: logging.LogRecord) -> None:
        kwargs = {}
        message = record.getMessage()

        if record.levelno == logging.ERROR:
            kwargs["err"] = True
        elif record.levelno == logging.WARNING:
            message = click.style(message, bold=True)

        click.echo(message, **kwargs)

    def _get_filter(self, log_level: str) -> Callable[[logging.LogRecord], bool]:
        log_level = logging.getLevelName(log_level)

        def inner(record: logging.LogRecord) -> bool:
            return record.levelno >= log_level

        return inner


def init_cli_logger(log_level: str) -> logging.Logger:
    global logger, _noop

    logger.removeHandler(_noop)
    logger.addHandler(ClickHandler(log_level.upper()))
    logger.setLevel(logging.DEBUG)
    if not os.path.exists(HOME_FOLDER):  # Check if HOME_FOLDER exists at this point
        os.makedirs(HOME_FOLDER)

    try:
        fh = logging.FileHandler(LOG_FILE, mode="w")
    except FileNotFoundError:
        logger.error(f"Unable to create log file: {LOG_FILE}")
        return logger

    formatter = logging.Formatter("%(asctime)s :: %(filename)s@%(funcName)s@%(lineno)d :: %(levelname)s :: %(msg)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger
