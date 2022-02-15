from BoolType import BoolType
from Expressions.Expression import Expression


class TrueExpression(Expression):

    def __init__(self, line: int):
        super(TrueExpression, self).__init__(line)

    def of_type(self, tc):
        return BoolType();

    def to_value(self):
        return "true"