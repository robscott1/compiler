from BoolType import BoolType
from CompilerError import CompilerError
from ErrorOut import error_out
from Expressions.Expression import Expression
from Factories.ExpressionFactory import ExpressionFactory
from Statements.Statement import Statement


class WhileStatement(Statement):

    """
    @:param:
        - guard (Expression): conditional for loop continue
        - body: (List<Statement>): statements to execute
    """
    def __init__(self, line: int, guard: Expression, body: list):
        super(WhileStatement, self).__init__(line)
        self.guard = guard
        self.body = body

    @classmethod
    def generate(cls, fn, stmt: dict):
        stmt.pop("stmt")
        body_statements = stmt.get("body").get("list")
        stmt["body"] = list(map(lambda x: fn(x), body_statements))
        stmt["guard"] = ExpressionFactory.generate(stmt.get("guard"))
        return WhileStatement(**stmt)

    def analyze(self, tc):
        if not isinstance(self.guard.of_type(tc), BoolType):
            error_out(
                self.line, "While guard must evaluate to a bool.", code="600"
            )
        for s in self.body:
            s.analyze(tc)

    def to_string(self):
        return "while {cond}"


