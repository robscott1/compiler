from Expressions.BinaryExpression import BinaryExpression
from Expressions.IntExpression import IntExpression


class ExpressionFactory:

    @classmethod
    def generate(cls, exp: dict):
        e = exp["exp"]
        if e == "num":
            return IntExpression.generate(exp)
        elif e == "binary":
            return BinaryExpression.generate(exp)
