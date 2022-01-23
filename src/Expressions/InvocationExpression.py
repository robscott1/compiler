from Expressions.Expression import Expression


class InvocationExpression(Expression):
    """
    @:param:
        - args (List<Expression>)
    """

    def __init__(self, line: int, id: str, args: list):
        super(InvocationExpression, self).__init__(line)
        self.id = id
        self.args = args

    @classmethod
    def generate(cls, fn, exp: dict):
        exp.pop("exp")
        exp["args"] = list(map(
            lambda x: fn(x), exp.get("args")))
        return InvocationExpression(**exp)
