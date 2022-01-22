from Expressions.Expression import Expression


class DotExpression(Expression):

    def __init__(self, line: int, left: Expression, id: str):
        super(DotExpression, self).__init__(line)
        self.left = left
        self.id = id
