from CompilerError import CompilerError
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
        if "list" not in stmt:
            print("found")

        statements = []
        if len(stmt.get("list")) != 0:
            try:
                for s in stmt.get("list"):
                    statements.append(func(s))
            except CompilerError as e:
                print(e.msg)
                exit()

        # statements = list(map(
        #     lambda x: func(x), stmt.get("list"))
        # ) if len(stmt.get("list")) != 0 \
        #     else cls.empty_block()
        return BlockStatement(-1, statements)

    def analyze(self, tc):
        for s in self.statements:
            s.analyze(tc)
