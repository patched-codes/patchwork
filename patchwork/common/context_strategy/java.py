from patchwork.common.context_strategy.langugues import JavaLanguage
from patchwork.common.context_strategy.protocol import TreeSitterStrategy


class JavaStrategy(TreeSitterStrategy):
    def __init__(self, query: str):
        """
        Initialize the JavaSearcher instance.

        Args:
        query (str): The search query string to be used for Java file search.
        """
        super().__init__("java", query, [".java"], JavaLanguage())
        self.query = query


class JavaClassStrategy(JavaStrategy):
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


class JavaMethodStrategy(JavaStrategy):
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
            (block_comment) @comment
            (method_declaration) @node
        ]
        """.strip()
        )


class JavaBlockStrategy(JavaStrategy):
    def __init__(self):
        """
        Initialize the class by calling the parent class's constructor.

        Parameters:
        - self: The object instance.
        """
        super().__init__(
            """
            (block) @node
        """.strip()
        )
