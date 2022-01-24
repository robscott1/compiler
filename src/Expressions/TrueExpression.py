from Expressions.Expression import Expression


class TrueExpression(Expression):

    def __init__(self, line: int):
        super(TrueExpression, self).__init__(line)

    def type_check(self, tc):
        pass
