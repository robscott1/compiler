from Expressions.IntExpression import IntExpression


class ExpressionFactory:

    @classmethod
    def generate(cls, exp: dict):
        if exp["exp"] == "num":
            return IntExpression.generate(exp)
