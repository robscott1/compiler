from Expressions.Expression import Expression
from TypeChecker import TypeChecker


class FalseExpression(Expression):

    def __init__(self, line: int):
        super(FalseExpression, self).__init__(line)

    def type_check(self, tc: TypeChecker):
        pass
