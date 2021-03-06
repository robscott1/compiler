from Types.BoolType import BoolType
from Expressions.Expression import Expression


class FalseExpression(Expression):

    def __init__(self, line: int):
        super(FalseExpression, self).__init__(line)

    def of_type(self, tc):
        return BoolType()

    def to_value(self):
        return "false"