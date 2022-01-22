from Expressions.Expression import Expression


class IdentifierExpression(Expression):

    def __init__(self, line: int, id: str):
        super(IdentifierExpression, self).__init__(line)
        self.id = id
