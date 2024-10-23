from patchwork.common.context_strategy.languages import JavaLanguage
from patchwork.common.context_strategy.protocol import TreeSitterStrategy


class KotlinStrategy(TreeSitterStrategy):
    def __init__(self, query: str):
        """
        Initialize the kotlin searcher instance.

        Args:
        query (str): The search query string to be used for Java file search.
        """
        super().__init__("kotlin", query, ["kt"], JavaLanguage())
        self.query = query


class KotlinClassStrategy(KotlinStrategy):
    def __init__(self):
        """
        Initialize the current class by calling the parent class's __init__ method.
        The specific class to be initialized should have a class_declaration marked by @node.
        """
        super().__init__(
            """
            (class_declaration) @node
            """.strip()
        )


class KotlinMethodStrategy(KotlinStrategy):
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
            (multiline_comment) @comment
            (function_declaration) @node
        ]
        """.strip()
        )
