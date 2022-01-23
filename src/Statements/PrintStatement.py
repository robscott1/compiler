from Expressions.Expression import Expression
from Factories.ExpressionFactory import ExpressionFactory
from Statements.Statement import Statement


class PrintStatement(Statement):

    def __init__(self, line: int, exp: Expression):
        super(PrintStatement, self).__init__(line)
        self.expression = exp

    @classmethod
    def generate(cls, stmt: dict):
        stmt["exp"] = ExpressionFactory.generate(stmt.get("exp"))
        stmt.pop("stmt")
        return PrintStatement(**stmt)

