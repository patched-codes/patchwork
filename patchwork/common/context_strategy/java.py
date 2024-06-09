from patchwork.common.context_strategy.protocol import TreeSitterStrategy


class JavaStrategy(TreeSitterStrategy):
    def __init__(self, query: str):
        super().__init__("java", query, [".java"])
        self.query = query


class JavaClassStrategy(JavaStrategy):
    def __init__(self):
        super().__init__(
            """
            (class_declaration) @node
        """.strip()
        )


class JavaMethodStrategy(JavaStrategy):
    def __init__(self):
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
        super().__init__(
            """
            (block) @node
        """.strip()
        )
