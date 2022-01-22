from Expressions.Expression import Expression
from Statements.Statement import Statement


class ConditionalStatement(Statement):

    def __init__(self, line: int, guard: Expression,
                 then_block: Statement, else_block: Statement):
        super(ConditionalStatement, self).__init__(line)
        self.guard = guard
        self.then_block = then_block
        self.else_block = else_block
