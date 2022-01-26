from CompilerError import CompilerError
from ErrorOut import error_out
from Expressions.Expression import Expression
from Factories.ExpressionFactory import ExpressionFactory
from IntType import IntType
from Statements.Statement import Statement


class PrintStatement(Statement):

    def __init__(self, line: int, exp: Expression):
        super(PrintStatement, self).__init__(line)
        self.expression = exp

    @classmethod
    def generate(cls, stmt: dict):
        stmt["exp"] = ExpressionFactory.generate(stmt.get("exp"))
        stmt.pop("stmt")
        stmt.pop("endl")
        return PrintStatement(**stmt)

    def analyze(self, tc):
        if not isinstance(self.expression.of_type(tc), IntType):
            error_out(
                self.line, "Print statement must print an int"
            )