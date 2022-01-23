from Expressions.Expression import Expression


class NullExpression(Expression):

    def __init__(self, line: int):
        super(NullExpression, self).__init__(line)