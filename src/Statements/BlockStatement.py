from Statements.Statement import Statement


class BlockStatement(Statement):
    """
    @:param:
        - line (int): line number
        - statements (List<Statement>): list of statements in block
    """

    def __init__(self, line: int, statements: list):
        super(BlockStatement, self).__init__(line)
        self.statements = statements

    @classmethod
    def empty_block(cls):
        return BlockStatement(-1, [])

    @classmethod
    def generate(cls, func, stmt: dict):
        statements = list(map(
            lambda x: func(x), stmt.get("list"))
        ) if len(stmt.get("list")) != 0 \
            else cls.empty_block()
        return BlockStatement(-1, statements)
