from Expressions.Expression import Expression


class DotExpression(Expression):

    def __init__(self, line: int, left: Expression, id: str):
        super(DotExpression, self).__init__(line)
        self.left = left
        self.id = id

    @classmethod
    def generate(cls, fn, exp: dict):
        exp.pop("exp")
        exp["left"] = fn(exp.get("left"))
        return DotExpression(**exp)

