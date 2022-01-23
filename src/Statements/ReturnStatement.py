from Expressions.Expression import Expression
from Factories.ExpressionFactory import ExpressionFactory
from Statements.Statement import Statement


class ReturnStatement(Statement, object):

    def __init__(self, line: int, expression: Expression):
        super(ReturnStatement, self).__init__(line)
        self.expression = expression

    @classmethod
    def generate(cls, stmt: dict):
        expression = ExpressionFactory.generate(stmt.get("exp"))
        line = stmt.get("line")
        return ReturnStatement(line, expression)
