from Expressions.Expression import Expression


class IntExpression(Expression):
    def __init__(self, line: int, value: str):
        super(IntExpression, self).__init__(line)
        self.value = value
