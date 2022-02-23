from Expressions.Expression import Expression
from NullType import NullType


class NullExpression(Expression):

    def __init__(self, line: int):
        super(NullExpression, self).__init__(line)

    def of_type(self, tc):
        return NullType()

    def to_value(self):
        return "null"
