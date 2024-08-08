from __future__ import annotations

import contextlib
import functools
from collections import Counter

from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn
from typing_extensions import Type

from patchwork.logger import console, logger
from patchwork.step import Step


class PatchflowProgressBar:
    __MAX_PROGRESS = 100.00

    def __init__(self, patchflow: Step):
        self.__step_counter = Counter()
        self.__current_progress = 0.00
        self.__patchflow_name = patchflow.__class__.__name__

        patchflow_run_func = patchflow.run

        def inner_run():
            try:
                return patchflow_run_func()
            finally:
                self.__progress_bar_update(
                    description=f"[bold green]Finished {self.__patchflow_name}", completed=self.__MAX_PROGRESS
                )

        patchflow.run = inner_run

    def register_steps(self, *steps: Type[Step]):
        for step in steps:
            self.register_step(step)

    def register_step(self, step: Type[Step]):
        step_run_func = step.run

        def inner_run(*args, **kwargs):
            with self.__update(step):
                return step_run_func(*args, **kwargs)

        step.run = inner_run
        self.__step_counter[step] = 0

    @property
    def __remaining_progress(self):
        return self.__MAX_PROGRESS - self.__current_progress

    @property
    def __increment_progress(self):
        max_counter = max(self.__step_counter.most_common()[0][1], 1)
        max_section = len(self.__step_counter) * max_counter
        increment = round(self.__remaining_progress / max_section, 2)
        self.__current_progress += increment
        return increment

    @functools.cached_property
    def __progress_bar(self):
        return Progress(SpinnerColumn(), *Progress.get_default_columns(), TimeElapsedColumn(), console=console)

    @functools.cached_property
    def __progress_bar_update(self):
        progress = self.__progress_bar
        logger.register_progress_bar(progress)
        task_id = progress.add_task(
            description=f"[bold green]Running {self.__patchflow_name}",
            total=self.__MAX_PROGRESS,
        )
        return functools.partial(progress.update, task_id, refresh=True)

    @contextlib.contextmanager
    def __update(self, step: type):
        self.__progress_bar_update(
            description=f"[bold green]Running {step.__name__}",
            advance=self.__increment_progress,
        )
        self.__step_counter[step] += 1
        yield
        return
