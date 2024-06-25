from __future__ import annotations

import contextlib
import functools
import warnings
from collections import Counter

import click
from tqdm import tqdm
from typing_extensions import Type

from patchwork.step import Step


class PatchflowProgressBar:
    __MAX_PROGRESS = 100.00

    def __init__(self, patchflow: Step):
        self.__step_counter = Counter()
        self.__current_progress = 0.00
        self.__callbacks = []
        self.__patchflow_name = patchflow.__class__.__name__

        patchflow_run_func = patchflow.run

        def inner_run():
            try:
                self.__outer_tqdm.reset()
                return patchflow_run_func()
            finally:
                self.__outer_tqdm.set_description(f"Finished {self.__patchflow_name}")
                self.__outer_tqdm.close()
                self.__do_callbacks()

        patchflow.run = inner_run

    def register_callbacks(self, *callbacks):
        self.__callbacks.extend(callbacks)

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
        return self.__outer_tqdm.total - self.__current_progress

    @property
    def __increment_progress(self):
        max_counter = max(self.__step_counter.most_common()[0][1], 1)
        max_section = len(self.__step_counter) * max_counter
        return round(self.__remaining_progress / max_section, 2)

    @functools.cached_property
    def __outer_tqdm(self):
        self.__suppress_warnings()
        self.__intercept_click_echo()
        return tqdm(
            total=self.__MAX_PROGRESS,
            desc=f"Running {self.__patchflow_name}",
            smoothing=0,
            miniters=1,
            unit_scale=True,
        )

    @contextlib.contextmanager
    def __update(self, step: type):
        self.__outer_tqdm.set_description(f"Running {step.__name__}")
        self.__outer_tqdm.update(self.__increment_progress)
        self.__step_counter[step] += 1
        yield
        return

    def __suppress_warnings(self):
        warnings.simplefilter("ignore")
        self.__callbacks.append(warnings.resetwarnings)

    def __intercept_click_echo(self):
        true_click_echo = click.echo

        def intercepted_click_echo(*args, **kwargs):
            self.__callbacks.append(lambda: true_click_echo(*args, **kwargs))
            return

        def restore_click_echo():
            click.echo = true_click_echo

        self.__callbacks.append(restore_click_echo)
        click.echo = intercepted_click_echo

    def __do_callbacks(self):
        for callbacks in self.__callbacks:
            callbacks()
