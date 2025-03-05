from __future__ import annotations

import contextlib
import logging
import os
import warnings
from functools import partial

import click
from rich.console import Console, Group
from rich.live import Live
from rich.logging import RichHandler
from rich.markup import escape
from rich.panel import Panel
from rich.progress import Progress
from typing_extensions import Callable

from patchwork.managed_files import HOME_FOLDER, LOG_FILE

# Create a global console object
console = Console()

# Add TRACE level to logging
logging.TRACE = logging.DEBUG - 1
logging.addLevelName(logging.TRACE, "TRACE")
logger = logging.getLogger("patched")
logger.trace = partial(logger.log, logging.TRACE)

# default noop logger
__noop = logging.NullHandler()
logger.addHandler(__noop)


def evict_null_handler():
    global logger, __noop

    warnings.simplefilter("ignore")
    logger.removeHandler(__noop)


class TerminalHandler(RichHandler):
    def __init__(self, log_level: str):
        super().__init__(
            console=console,
            rich_tracebacks=True,
            tracebacks_suppress=[click],
            show_time=False,
            show_path=False,
            show_level=False,
        )
        self.addFilter(self.__get_filter(log_level))
        self.__live = None
        self.__panel = None
        self.__panel_lines = []
        self.__panel_title = None
        self.__progress_bar = None

    @contextlib.contextmanager
    def freeze(self):
        if self.__live is not None:
            current_render = self.__live.renderable
            self.__live.update("")
            self.__live.stop()
            try:
                yield
            finally:
                if self.__live is not None:
                    self.__live.update(current_render)
                    self.__live.start()
        else:
            yield

    def __reset_live(self):
        if self.__live is not None:
            self.__live.stop()

        self.__live = None
        self.__panel = None
        self.__panel_lines = []
        self.__panel_title = None
        self.__progress_bar = None

    def register_progress_bar(self, progress_bar: Progress):
        self.__progress_bar = progress_bar
        if self.__live is not None:
            self.__live.update(Group(self.__panel, progress_bar))
            self.__live.refresh()

    def deregister_progress_bar(self):
        self.__progress_bar = None
        if self.__live is not None:
            self.__live.update(Group(self.__panel))
            self.__live.refresh()

    @contextlib.contextmanager
    def panel(self, title: str):
        global console
        self.__panel_lines = []
        self.__panel_title = title
        self.__panel = Panel("", title=title)
        renderables = [self.__panel]
        if self.__progress_bar is not None:
            renderables.append(self.__progress_bar)

        self.__live = Live(Group(*renderables), console=console, vertical_overflow="visible")
        try:
            self.__live.start()
            yield
        except Exception as e:
            raise e
        finally:
            self.__reset_live()
            self.console.print("\n")

    def emit(self, record: logging.LogRecord) -> None:
        markup = getattr(record, "markup", None)
        if not markup:
            message = escape(record.getMessage())
            if record.levelno == logging.ERROR:
                record.msg = f"[red]{message}[/]"
            elif record.levelno == logging.WARNING:
                record.msg = f"[yellow bold]{message}[/]"
            elif record.levelno == logging.INFO:
                record.msg = f"[green]{message}[/]"

        if self.__panel is not None:
            self.__emit_panel(record)
        else:
            setattr(record, "markup", True)
            super().emit(record)

    def __emit_panel(self, record: logging.LogRecord) -> None:
        self.__panel_lines.append(record.getMessage())
        self.__panel.renderable = "\n".join(self.__panel_lines)
        self.__live.refresh()

    def __get_filter(self, log_level: str) -> Callable[[logging.LogRecord], bool]:
        log_level = logging.TRACE if log_level == "TRACE" else logging.getLevelName(log_level)

        def inner(record: logging.LogRecord) -> bool:
            return record.levelno >= log_level

        return inner


def init_cli_logger(log_level: str) -> logging.Logger:
    global logger

    evict_null_handler()

    if not os.path.exists(HOME_FOLDER):  # Check if HOME_FOLDER exists at this point
        os.makedirs(HOME_FOLDER)
    try:
        fh = logging.FileHandler(LOG_FILE, mode="w")
        formatter = logging.Formatter("%(asctime)s :: %(filename)s@%(funcName)s@%(lineno)d :: %(levelname)s :: %(msg)s")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    except FileNotFoundError:
        logger.error(f"Unable to create log file: {LOG_FILE}")

    th = TerminalHandler(log_level.upper())
    logger.addHandler(th)
    setattr(logger, "panel", th.panel)
    setattr(logger, "register_progress_bar", th.register_progress_bar)
    setattr(logger, "deregister_progress_bar", th.deregister_progress_bar)
    setattr(logger, "freeze", th.freeze)
    logger.setLevel(logging.TRACE)
    return logger
