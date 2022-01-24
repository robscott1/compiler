from Expressions.Expression import Expression
from Factories.ExpressionFactory import ExpressionFactory
from LvalueId import LvalueId
from Statements.Statement import Statement
from l_value import Lvalue


class AssignmentStatement(Statement):
    def __init__(self, line: int, target: Lvalue, source: Expression):
        super(AssignmentStatement, self).__init__(line)
        self.target = target
        self.source = source

    @classmethod
    def generate(cls, stmt: dict):
        line = stmt.get("line")
        source_dict = stmt.get("source")
        source = ExpressionFactory.generate(source_dict)
        lvalue_id_dict = stmt.get("target")
        lvalue_id = LvalueId(**lvalue_id_dict)
        return AssignmentStatement(line, source, lvalue_id)

