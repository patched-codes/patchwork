from enum import Enum

from .generic import FullFileStrategy, NoopStrategy
from .java import JavaBlockStrategy, JavaClassStrategy, JavaMethodStrategy
from .javascript import (
    JavascriptBlockStrategy,
    JavascriptClassStrategy,
    JavascriptFunctionStrategy,
    JsxBlockStrategy,
    JsxClassStrategy,
    JsxFunctionStrategy,
)
from .protocol import ContextStrategyProtocol
from .python import PythonBlockStrategy, PythonFunctionStrategy


class ContextStrategies:
    FULL_FILE = "FULL_FILE"
    NOOP = "NOOP"
    # Python strategies
    PYTHON_FUNCTION = "PYTHON_FUNCTION"
    PYTHON_BLOCK = "PYTHON_BLOCK"
    # Java strategies
    JAVA_CLASS = "JAVA_CLASS"
    JAVA_METHOD = "JAVA_METHOD"
    JAVA_BLOCK = "JAVA_BLOCK"
    # JavaScript strategies
    JAVASCRIPT_CLASS = "JAVASCRIPT_CLASS"
    JAVASCRIPT_FUNCTION = "JAVASCRIPT_FUNCTION"
    JAVASCRIPT_BLOCK = "JAVASCRIPT_BLOCK"
    # JSX strategies
    JSX_CLASS = "JSX_CLASS"
    JSX_FUNCTION = "JSX_FUNCTION"
    JSX_BLOCK = "JSX_BLOCK"

    PYTHON_PARTIAL_STRATEGIES = [PYTHON_FUNCTION, PYTHON_BLOCK]
    JAVA_PARTIAL_STRATEGIES = [JAVA_CLASS, JAVA_METHOD, JAVA_BLOCK]
    JAVASCRIPT_PARTIAL_STRATEGIES = [JAVASCRIPT_CLASS, JAVASCRIPT_FUNCTION, JAVASCRIPT_BLOCK]
    JSX_PARTIAL_STRATEGIES = [JSX_CLASS, JSX_FUNCTION, JSX_BLOCK]

    ALL = [
        FULL_FILE,
        *PYTHON_PARTIAL_STRATEGIES,
        *JAVA_PARTIAL_STRATEGIES,
        *JAVASCRIPT_PARTIAL_STRATEGIES,
        *JSX_PARTIAL_STRATEGIES,
        NOOP,
    ]

    FUNCTION = [
        PYTHON_FUNCTION,
        JAVA_METHOD,
        JAVASCRIPT_FUNCTION,
        JSX_FUNCTION
    ]

    __MAPPING: dict[str, ContextStrategyProtocol] = {
        FULL_FILE: FullFileStrategy(),
        NOOP: NoopStrategy(),
        PYTHON_FUNCTION: PythonFunctionStrategy(),
        PYTHON_BLOCK: PythonBlockStrategy(),
        JAVA_CLASS: JavaClassStrategy(),
        JAVA_METHOD: JavaMethodStrategy(),
        JAVA_BLOCK: JavaBlockStrategy(),
        JAVASCRIPT_CLASS: JavascriptClassStrategy(),
        JAVASCRIPT_FUNCTION: JavascriptFunctionStrategy(),
        JAVASCRIPT_BLOCK: JavascriptBlockStrategy(),
        JSX_CLASS: JsxClassStrategy(),
        JSX_FUNCTION: JsxFunctionStrategy(),
        JSX_BLOCK: JsxBlockStrategy(),
    }

    @staticmethod
    def get_context_strategy(name: str) -> ContextStrategyProtocol | None:
        return ContextStrategies.__MAPPING.get(name, None)

    @staticmethod
    def get_context_strategies(name: str, *args) -> list[ContextStrategyProtocol]:
        rv = []
        for arg in [name, *args]:
            element = ContextStrategies.get_context_strategy(arg)
            if element is None:
                continue

            rv.append(element)
        return rv
