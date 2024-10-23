from patchwork.common.context_strategy.languages import CppLanguage
from patchwork.common.context_strategy.protocol import TreeSitterStrategy


class CppStrategy(TreeSitterStrategy):
    def __init__(self, query: str):
        """
        Initialize the Cpp searcher instance.

        Args:
        query (str): The search query string to be used for Java file search.
        """

        # exts from https://gcc.gnu.org/onlinedocs/gcc-4.4.1/gcc/Overall-Options.html#index-file-name-suffix-71
        exts = [
            ".ii",
            ".h",
            ".cc",
            ".cp",
            ".cxx",
            ".cpp",
            ".CPP",
            ".c++",
            ".C",
            ".hh",
            ".H",
            ".hp",
            ".hxx",
            ".hpp",
            ".HPP",
            ".h++",
            ".tcc",
        ]
        super().__init__("cpp", query, exts, CppLanguage())
        self.query = query


class CppClassStrategy(CppStrategy):
    def __init__(self):
        """
        Initialize the current class by calling the parent class's __init__ method.
        The specific class to be initialized should have a class_declaration marked by @node.
        """
        super().__init__(
            """
            (class_specifier) @node
            """.strip()
        )


class CppMethodStrategy(CppStrategy):
    def __init__(self):
        """
        Initialize the newly created object by inheriting properties and
        methods from the parent class.

        Parameters:
        - self: instance of the class

        Returns:
        - None
        """
        super().__init__(
            """
        [
            (comment) @comment
            (function_definition) @node
        ]
        """.strip()
        )


class CppBlockStrategy(CppStrategy):
    def __init__(self):
        """
        Initialize the class by calling the parent class's constructor.

        Parameters:
        - self: The object instance.
        """
        super().__init__(
            """
            (compound_statement) @node
        """.strip()
        )
