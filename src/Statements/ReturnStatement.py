from CompilerError import CompilerError
from ErrorOut import error_out
from Expressions.Expression import Expression
from Expressions.NullExpression import NullExpression
from Factories.ExpressionFactory import ExpressionFactory
from Statements.Statement import Statement


class ReturnStatement(Statement, object):

    def __init__(self, line: int, expression: Expression):
        super(ReturnStatement, self).__init__(line)
        self.expression = expression

    @classmethod
    def generate(cls, stmt: dict):
        if "exp" not in stmt:
            stmt["exp"] = {"line": stmt.get("line"), "exp": "null"}
        expression = ExpressionFactory.generate(stmt.get("exp"))
        line = stmt.get("line")
        return ReturnStatement(line, expression)

    def analyze(self, tc):
        exp_return_type = tc.current_scope.return_type
        return_type = self.expression.of_type(tc)
        if not return_type.equals(exp_return_type):
            error_out(
                self.line, "Unexpected return type.", code="500"
            )

