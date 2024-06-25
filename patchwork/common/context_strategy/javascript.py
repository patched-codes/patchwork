from patchwork.common.context_strategy.langugues import JavascriptLanguage
from patchwork.common.context_strategy.protocol import TreeSitterStrategy

_javascript_language = "typescript"
_jsx_language = "tsx"

_class_query = """
    [
        (class_declaration)
        (interface_declaration)
        (enum_declaration)
    ] @node
""".strip()
_function_query = """
    [
      (comment) @comment
      [
        ( function )
        ( function_declaration )
        ( generator_function_declaration )
        ( arrow_function )
      ] @node
    ]
    """.strip()
_block_query = """
        (statement_block) @node
    """.strip()

_javascript_exts = [".js", ".ts"]
_jsx_exts = [".jsx", ".tsx"]


class JavascriptClassStrategy(TreeSitterStrategy):
    def __init__(self):
        """
        Initializes the parent class with predefined attributes for handling JavaScript files.

        Attributes:
            _javascript_language (str): Language specification for JavaScript.
            _class_query (str): Query string used for class searches within JavaScript files.
            _javascript_exts (tuple): A tuple containing the file extensions for JavaScript files.
        """
        super().__init__(_javascript_language, _class_query, _javascript_exts, JavascriptLanguage())


class JavascriptFunctionStrategy(TreeSitterStrategy):
    def __init__(self):
        """
        Initialize the current class instance as a subclass, passing specific parameters related to JavaScript handling to the superclass constructor.

        Parameters:
        - _javascript_language (str): The language being used for JavaScript.
        - _function_query (str): The query for functions in JavaScript.
        - _javascript_exts (list): List of extensions related to JavaScript.

        Returns:
        - None
        """
        super().__init__(_javascript_language, _function_query, _javascript_exts, JavascriptLanguage())


class JavascriptBlockStrategy(TreeSitterStrategy):
    def __init__(self):
        """
        Initialize the object by calling the superclass constructor with specific arguments.

        Parameters:
        - _javascript_language (str): The language used for JavaScript.
        - _block_query (str): The query to block JavaScript functionalities.
        - _javascript_exts (list): List of JavaScript file extensions.
        """
        super().__init__(_javascript_language, _block_query, _javascript_exts, JavascriptLanguage())


class JsxClassStrategy(TreeSitterStrategy):
    def __init__(self):
        """
        Initialize the object by calling the superclass's initializer with specific parameters.

        Parameters:
        - _jsx_language (str): The JSX language parameter.
        - _class_query (str): The class query parameter.
        - _jsx_exts (str): The JSX extensions parameter.
        """
        super().__init__(_jsx_language, _class_query, _jsx_exts, JavascriptLanguage())


class JsxFunctionStrategy(TreeSitterStrategy):
    def __init__(self):
        """
        Initialize the instance by calling the parent class's constructor with predefined arguments.

        Parameters:
        - _jsx_language (str): The language for JSX.
        - _function_query (str): The query for functions.
        - _jsx_exts (str): The file extension for JSX files.
        """
        super().__init__(_jsx_language, _function_query, _jsx_exts, JavascriptLanguage())


class JsxBlockStrategy(TreeSitterStrategy):
    def __init__(self):
        """
        Initializes the object by calling the superclass initializer with the
        provided language, block query, and file extensions for JSX processing.

        Parameters:
        - self: the object itself

        Returns:
        - None
        """
        super().__init__(_jsx_language, _block_query, _jsx_exts, JavascriptLanguage())
