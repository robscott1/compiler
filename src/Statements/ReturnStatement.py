from Expressions.Expression import Expression
from Statements.Statement import Statement


class ReturnStatement(Statement, object):

    def __init__(self, line: int, expression: Expression):
        super(ReturnStatement, self).__init__(line)
        self.expression = expression
