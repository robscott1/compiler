from Expressions.Expression import Expression
from Types.IntType import IntType


class ReadExpression(Expression):

    def __init__(self, line):
        super(ReadExpression, self).__init__(line)

    def of_type(self, tc):
        return IntType()
