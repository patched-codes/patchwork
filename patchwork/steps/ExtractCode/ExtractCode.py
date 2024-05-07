import json
import os
import sys
from collections import defaultdict
from enum import IntEnum
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from patchwork.common.utils import (
    count_openai_tokens,
    defered_temp_file,
    open_with_chardet,
)
from patchwork.logger import logger
from patchwork.step import Step
from patchwork.steps.ExtractCode.context_strategy.context_strategies import (
    ContextStrategies,
)


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
        if count_openai_tokens(context) <= context_token_length:
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


class Severity(IntEnum):
    CRITICAL = 5
    HIGH = 4
    ERROR = 4
    MEDIUM = 3
    LOW = 2
    WARNING = 2
    INFO = 1
    NOTE = 1
    UNKNOWN = 0

    @staticmethod
    def from_str(severity: str) -> "Severity":
        try:
            return Severity[severity.upper()]
        except KeyError:
            logger.error(f'Unknown severity: "{severity}"')
            return Severity.UNKNOWN


def get_rule_severity(rule: dict[str:Any]) -> Severity:
    properties = rule.get("properties", {})

    try:
        security_severity = float(properties.get("security-severity"))
    except (ValueError, TypeError):
        security_severity = None

    if security_severity is not None:
        if security_severity >= 9.0:
            return Severity.CRITICAL
        elif security_severity >= 7.0:
            return Severity.HIGH
        elif security_severity >= 4.0:
            return Severity.MEDIUM
        else:
            return Severity.LOW

    properties_severity = properties.get("severity") or properties.get("Severity")
    if properties_severity is not None:
        return Severity.from_str(properties_severity)

    return Severity.UNKNOWN


def get_severity(result, reporting_descriptors):
    properties = result.get("properties", {})
    properties_severity = properties.get("severity") or properties.get("Severity")
    if properties_severity is not None:
        return Severity.from_str(properties_severity)

    result_rule = result.get("rule", {})
    result_rule_idx = result.get("ruleIndex") or result_rule.get("index")
    result_rule_id = result.get("ruleId") or result_rule.get("id")
    rule = None
    if result_rule_idx is not None:
        rule = reporting_descriptors[result_rule_idx]
    elif result_rule_id is not None:
        for reporting_descriptor in reporting_descriptors:
            if reporting_descriptor.get("id") == result_rule_id:
                rule = reporting_descriptor
                break
    elif len(result_rule) > 0:
        rule = result_rule

    rule_severity = Severity.UNKNOWN
    if rule is not None:
        rule_severity = get_rule_severity(rule)

    if rule_severity != Severity.UNKNOWN:
        return rule_severity

    result_level = result.get("level")
    if result_level is not None:
        return Severity.from_str(result_level)

    default_level = rule.get("defaultConfiguration", {}).get("level")
    if default_level is not None:
        return Severity.from_str(default_level)

    return Severity.UNKNOWN


def transform_sarif_results(
    sarif_data: dict, base_path: Path, context_length: int, vulnerability_limit: int, severity_threshold: Severity
) -> dict[tuple[str, int, int, int], list[str]]:
    # Process each result in SARIF data
    grouped_messages = defaultdict(list)
    vulnerability_count = 0
    for run_idx, run in enumerate(sarif_data.get("runs", [])):
        artifact_locations = [
            parse_sarif_location(base_path, artifact["location"]["uri"]) for artifact in run.get("artifacts", [])
        ]

        tool = run.get("tool", {})
        reporting_descriptors = tool.get("driver", {}).get("rules", [])
        for tool_obj in tool.get("extensions", []):
            reporting_descriptors.extend(tool_obj.get("rules", []))

        for result_idx, result in enumerate(run.get("results", [])):
            severity = get_severity(result, reporting_descriptors)
            if severity < severity_threshold:
                continue

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
                        file_path, source_lines, start_line, end_line, context_length
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

                grouped_messages[(file_path, start, end, source_code_context)].append(
                    result.get("message", {}).get("text", "")
                )

                vulnerability_count = vulnerability_count + 1
                if 0 < vulnerability_limit <= vulnerability_count:
                    return grouped_messages

    return grouped_messages


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
        self.severity_threshold = Severity.from_str(inputs.get("severity", "UNKNOWN"))

        # Prepare for data extraction
        self.extracted_code_contexts = []

    def run(self) -> dict:
        # Load SARIF data
        with open_with_chardet(self.sarif_file_path, "r") as file:
            sarif_data = json.load(file)

        base_path = Path.cwd()

        grouped_messages = transform_sarif_results(
            sarif_data, base_path, self.context_length, self.vulnerability_limit, self.severity_threshold
        )

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
        with defered_temp_file("w", suffix=".json") as fp:
            json.dump(self.extracted_code_contexts, fp, indent=2)
            output_file = Path(fp.name)

        logger.info(f"Run completed {self.__class__.__name__}")

        return dict(
            code_file=output_file,
            prompt_values=self.extracted_code_contexts,
        )
