from Expressions.Expression import Expression
from Statements.Statement import Statement
from l_value import Lvalue


class AssignmentStatement(Statement):
    def __init__(self, line: int, target: Lvalue, source: Expression):
        super(AssignmentStatement, self).__init__(line)
        self.target = target
        self.source = source
