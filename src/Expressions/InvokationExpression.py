from Expressions.Expression import Expression


class InvocationExpression(Expression):

    def __init__(self, line: int, id: str, args: list):
        super(InvocationExpression, self).__init__(line)
        self.id = id
        self.args = args
