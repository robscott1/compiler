from Expressions.Expression import Expression


class FalseExpression(Expression):

    def __init__(self, line: int):
        super(FalseExpression, self).__init__(line)
