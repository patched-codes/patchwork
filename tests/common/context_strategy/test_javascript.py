import pytest

from patchwork.common.context_strategy.javascript import (
    JavascriptClassStrategy,
    JavascriptFunctionStrategy,
    JavascriptBlockStrategy,
    JsxClassStrategy,
    JsxFunctionStrategy,
    JsxBlockStrategy,
)


example_js_lines = [
    'import React from "react";\n',                                # 0
    'export default class App extends React.Component {\n',        # 1
    '  state = {\n',                                               # 2
    '    total: null,\n',                                          # 3
    '    next: null,\n',                                           # 4
    '    operation: null,\n',                                      # 5
    '  };\n',                                                      # 6
    '\n',                                                          # 7
    '  /** @param {string} buttonName */\n',                       # 8
    '  handleClick = buttonName => {\n',                           # 9
    '    this.setState(calculate(this.state, buttonName));\n',     # 10
    '  };\n',                                                      # 11
    '\n',                                                          # 12
    '  handleClick = function(buttonName) {\n',                    # 13
    '    this.setState(calculate(this.state, buttonName));\n',     # 14
    '  };\n',                                                      # 15
    '\n',                                                          # 16
    '  render() {\n',                                              # 17
    '    return (\n',                                              # 18
    '      <div className="component-app">\n',                     # 19
    '      </div>\n',                                              # 20
    '    );\n',                                                    # 21
    '  }\n',                                                       # 22
    '}\n',                                                         # 23
    'export function abc(a) {\n',                                  # 24
    '    return 1;\n',                                             # 25
    '}\n',                                                         # 26
    'function def(a) {\n',                                         # 27
    '    return 1;\n',                                             # 28
    '}\n',                                                         # 29
]


@pytest.mark.parametrize("strategy, expected_context_count, lines", [
    (JavascriptClassStrategy(), 1, example_js_lines),
    (JavascriptFunctionStrategy(), 4, example_js_lines),
    (JavascriptBlockStrategy(), 5, example_js_lines),
    (JsxClassStrategy(), 1, example_js_lines),
    (JsxFunctionStrategy(), 4, example_js_lines),
    (JsxBlockStrategy(), 5, example_js_lines),
])
def test_js_strategy_contexts(strategy, expected_context_count, lines):
    contexts = strategy.get_contexts(lines)
    assert len(contexts) == expected_context_count


@pytest.mark.parametrize("strategy, line_range, lines", [
    (JavascriptClassStrategy(), (0, 1), example_js_lines),
    (JavascriptFunctionStrategy(), (12, 13), example_js_lines),
    (JavascriptBlockStrategy(), (0, 1), example_js_lines),
    (JsxClassStrategy(), (0, 1), example_js_lines),
    (JsxFunctionStrategy(), (12, 13), example_js_lines),
    (JsxBlockStrategy(), (0, 1), example_js_lines),
])
def test_js_strategy_line_context_misses(strategy, line_range, lines):
    position = strategy.get_context_indexes(lines, line_range[0], line_range[1])
    assert position is None


@pytest.mark.parametrize("strategy, line_range, expected_range, lines", [
    (JavascriptClassStrategy(), (11, 12), (1, 24), example_js_lines),
    (JavascriptFunctionStrategy(), (11, 12), (9, 12), example_js_lines),
    (JavascriptBlockStrategy(), (11, 12), (9, 12), example_js_lines),
    (JsxClassStrategy(), (11, 12), (1, 24), example_js_lines),
    (JsxFunctionStrategy(), (11, 12), (9, 12), example_js_lines),
    (JsxBlockStrategy(), (11, 12), (9, 12), example_js_lines),
])
def test_js_strategy_line_context(strategy, line_range, expected_range, lines):
    expected_start, expected_end = expected_range
    position = strategy.get_context_indexes(lines, line_range[0], line_range[1])
    assert position.start == expected_start
    assert position.end == expected_end


