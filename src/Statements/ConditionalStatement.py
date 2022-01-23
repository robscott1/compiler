from Expressions.Expression import Expression
from Factories.ExpressionFactory import ExpressionFactory
from Statements.Statement import Statement


class ConditionalStatement(Statement):

    def __init__(self, line: int, guard: Expression,
                 then_block: Statement, else_block: Statement):
        super(ConditionalStatement, self).__init__(line)
        self.guard = guard
        self.then_block = then_block
        self.else_block = else_block

    @classmethod
    def generate(cls, stmt: dict):
        line = stmt.get("line")
        exp_dict = stmt.get("guard")
        guard = ExpressionFactory.generate(exp_dict)
        then_block = stmt.get("then")
        else_block = stmt.get("else")
        return ConditionalStatement(line, guard, then_block, else_block)


