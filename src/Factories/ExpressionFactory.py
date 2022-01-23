from Expressions.BinaryExpression import BinaryExpression
from Expressions.IntExpression import IntExpression
from Expressions.InvocationExpression import InvocationExpression
from Expressions.NullExpression import NullExpression


class ExpressionFactory:

    @classmethod
    def generate(cls, exp: dict):
        e = exp["exp"]
        if e == "num":
            return IntExpression.generate(exp)
        elif e == "binary":
            return BinaryExpression.generate(cls.generate, exp)
        elif e == "invocation":
            return InvocationExpression.generate(cls.generate, exp)

        else:
            return NullExpression(exp.get("line"))
