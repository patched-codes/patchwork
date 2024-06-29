from __future__ import annotations

import os
import sys
from collections import defaultdict
from enum import IntEnum
from pathlib import Path
from urllib.parse import urlparse

from typing_extensions import Any

from patchwork.common.context_strategy.context_strategies import ContextStrategies
from patchwork.common.utils.utils import count_openai_tokens, open_with_chardet
from patchwork.logger import logger
from patchwork.step import Step

def get_source_code_context(
    uri: str, source_lines: list[str], start_line: int, end_line: int, context_token_length: int
) -> tuple[int | None, int | None]:
    context_strategies = ContextStrategies.get_context_strategies(*ContextStrategies.ALL)
    context_strategies = [strategy for strategy in context_strategies if strategy.is_file_supported(uri, source_lines)]
    for context_strategy in context_strategies:
        position = context_strategy.get_context_indexes(source_lines, start_line, end_line)
        if position is None:
            logger.debug(f'Context Strategy: "{context_strategy.__class__.__name__}" failed to return context')
            continue

        logger.debug(f'"{context_strategy.__class__.__name__}" Context Strategy used: {position.start}, {position.end}')
        context = "".join(source_lines[position.start : position.end])
        logger.debug(context)
        logger.debug(count_openai_tokens(context))
        logger.debug(context_token_length)
        if count_openai_tokens(context) > context_token_length:
            logger.warn("The selected context is larger than the context_token_length. Consider increasing the context_token_length to process larger contexts.")
            return None, None
        return position.start, position.end

    return None, None
...
