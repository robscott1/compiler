from Expressions.Expression import Expression
from Statements.Statement import Statement


class InvocationStatement(Statement):
    def __init__(self, line: int, exp: Expression):
        super(InvocationStatement, self).__init__(line)
        self.exp = exp
