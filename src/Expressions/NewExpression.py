from Expressions.Expression import Expression


class NewExpression(Expression):

    def __init__(self, line: int, id: str):
        super(NewExpression, self).__init__(line)
        self.id = id

    @classmethod
    def generate(cls, exp: dict):
        exp.pop("exp")
        return NewExpression(**exp)
