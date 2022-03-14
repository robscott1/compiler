from ErrorOut import error_out
from Expressions.Expression import Expression
from Factories.ExpressionFactory import ExpressionFactory
from Types.IntType import IntType
from Statements.Statement import Statement


class PrintStatement(Statement):

    def __init__(self, line: int, exp: Expression, endl: str):
        super(PrintStatement, self).__init__(line)
        self.expression = exp
        self.endl = endl

    @classmethod
    def generate(cls, stmt: dict):
        stmt["exp"] = ExpressionFactory.generate(stmt.get("exp"))
        stmt.pop("stmt")
        return PrintStatement(**stmt)

    def analyze(self, tc):
        if not isinstance(self.expression.of_type(tc), IntType):
            error_out(
                self.line, "Print statement must print an int"
            )

    def to_string(self):
        return "print"