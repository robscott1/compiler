from Expressions.Expression import Expression


class IntExpression(Expression):
    def __init__(self, line: int, value: str):
        super(IntExpression, self).__init__(line)
        self.value = value

    @classmethod
    def generate(cls, exp: dict):
        line = exp.get("line")
        value = exp.get("value")
        return IntExpression(line, value)

