import json
import os
import sys
import tempfile
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

import tiktoken

from patchwork.logger import logger
from patchwork.step import Step

from ...common.utils import open_with_chardet
from .context_strategy.context_strategies import ContextStrategies

_ENCODING = tiktoken.get_encoding("cl100k_base")


def count_tokens(code: str):
    return len(_ENCODING.encode(code))


def get_source_code_context(
    uri: str, source_lines: list[str], start_line: int, end_line: int, context_token_length: int
) -> tuple[int | None, int | None]:
    context_strategies = ContextStrategies.get_context_strategies(*ContextStrategies.ALL)
    context_strategies = [strategy for strategy in context_strategies if strategy.is_file_supported(uri, source_lines)]
    for context_strategy in context_strategies:
        context_start, context_end = context_strategy.get_context_indexes(source_lines, start_line, end_line)
        if context_start is None or context_end is None:
            logger.info(f'Context Strategy: "{context_strategy.__class__.__name__}" failed to return context')
            continue

        logger.info(f'"{context_strategy.__class__.__name__}" Context Strategy used: {context_start}, {context_end}')
        context = "".join(source_lines[context_start:context_end])
        if count_tokens(context) <= context_token_length:
            return context_start, context_end

    return None, None


def parse_sarif_location(base_path: Path, location_str: str) -> Path | None:
    uri = urlparse(location_str)
    if uri.scheme != "file" and uri.scheme != "":
        logger.warn(f'Unsupported URI scheme "{uri.scheme}" for location: "{location_str}"')
        return None

    path = Path(uri.path)
    if path.is_relative_to(base_path):
        return path

    path = str(path).lstrip("/")
    if "/" not in path and "\\" in path and sys.platform != "win32":
        path = path.replace("\\", "/")
    if "\\" not in path and "/" in path and sys.platform == "win32":
        path = path.replace("/", "\\")

    location = Path(path)
    if not location.is_file():
        # find by wildcard
        location = next(Path(base_path).glob(f"**{os.sep}{path}"), None)
    else:
        location = location.resolve()
    if location is None:
        # cut the first repo path and try to find the file again
        path = path.lstrip(base_path.name)
        location = next(Path(base_path).glob(f"**{os.sep}{path}"), None)

    if location is None:
        # cut the first path part and try to find the file again
        _, _, path = path.partition(os.sep)
        location = next(Path(base_path).glob(f"**{os.sep}{path}"), None)

    return location


def resolve_artifact_location(
    base_path: Path, artifact_location: dict, artifact_locations: list[Path | None]
) -> Path | None:
    artifact_index = artifact_location.get("index")
    if artifact_index is not None:
        location = artifact_locations[artifact_index]
        if location is not None:
            return location

        logger.warn(f"Unable to find file for artifact index: {artifact_index}")

    uri = artifact_location.get("uri")
    if uri is not None:
        return parse_sarif_location(base_path, uri)

    return None


class ExtractCode(Step):
    required_keys = {"sarif_file_path"}

    def __init__(self, inputs: dict):
        logger.info(f"Run started {self.__class__.__name__}")

        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        # Validate and set the SARIF file path
        self.sarif_file_path = Path(inputs["sarif_file_path"])
        if not self.sarif_file_path.exists() or not self.sarif_file_path.is_file():
            raise ValueError(f'SARIF file path does not exist or is not a file: "{self.sarif_file_path}"')

        # Check and set number of lines to extract
        self.context_length = inputs.get("context_size", 1000)
        self.vulnerability_limit = inputs.get("vulnerability_limit", 10)

        # Prepare for data extraction
        self.extracted_data = []
        self.extracted_code_contexts = []

    def run(self) -> dict:
        # Load SARIF data
        with open_with_chardet(self.sarif_file_path, "r") as file:
            sarif_data = json.load(file)

        vulnerability_count = 0
        base_path = Path.cwd()
        # Process each result in SARIF data
        grouped_messages = defaultdict(list)
        for run_idx, run in enumerate(sarif_data.get("runs", [])):
            artifact_locations = [
                parse_sarif_location(base_path, artifact["location"]["uri"]) for artifact in run.get("artifacts", [])
            ]

            for result_idx, result in enumerate(run.get("results", [])):
                for location_idx, location in enumerate(result.get("locations", [])):
                    physical_location = location.get("physicalLocation", {})

                    artifact_location = physical_location.get("artifactLocation", {})
                    uri = resolve_artifact_location(base_path, artifact_location, artifact_locations)
                    if uri is None:
                        logger.warn(
                            f'Unable to find file for ".runs[{run_idx}].results[{result_idx}].locations[{location_idx}]"'
                        )
                        continue

                    region = physical_location.get("region", {})
                    start_line = region.get("startLine", 1)
                    end_line = region.get("endLine", start_line)
                    start_line = start_line - 1

                    # Generate file path assuming code is in the current working directory
                    file_path = str(uri.relative_to(base_path))

                    # Extract lines from the code file
                    logger.info(f"Extracting context for {file_path} at {start_line}:{end_line}")
                    try:
                        with open_with_chardet(file_path, "r") as file:
                            src = file.read()

                        source_lines = src.splitlines(keepends=True)
                        context_start, context_end = get_source_code_context(
                            file_path, source_lines, start_line, end_line, self.context_length
                        )

                        source_code_context = None
                        if context_start is not None and context_end is not None:
                            source_code_context = "".join(source_lines[context_start:context_end])

                    except FileNotFoundError:
                        context_start = None
                        context_end = None
                        source_code_context = None
                        logger.info(f"File not found in the current working directory: {file_path}")

                    if source_code_context is None:
                        logger.info(f"No context found for {file_path} at {start_line}:{end_line}")
                        continue

                    start = context_start if context_start is not None else start_line
                    end = context_end if context_end is not None else end_line
                    self.extracted_data.append(
                        {
                            "affectedCode": source_code_context,
                            "startLine": start,
                            "endLine": end,
                            "uri": file_path,
                            "messageText": result.get("message", {}).get("text", ""),
                        }
                    )

                    grouped_messages[(uri, start, end, source_code_context)].append(
                        result.get("message", {}).get("text", "")
                    )

                    vulnerability_count = vulnerability_count + 1
                    if 0 < self.vulnerability_limit <= vulnerability_count:
                        break

        self.extracted_code_contexts = [
            {
                "uri": str(file_path),
                "startLine": start,
                "endLine": end,
                "affectedCode": context,
                "messageText": "\n".join(msgs),
            }
            for (file_path, start, end, context), msgs in grouped_messages.items()
        ]

        # Save extracted data to JSON
        output_file = Path(tempfile.mktemp(".json"))
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(self.extracted_code_contexts, f, indent=2)

        logger.info(f"Run completed {self.__class__.__name__}")

        return dict(
            code_file=output_file,
            prompt_values=self.extracted_code_contexts,
        )
