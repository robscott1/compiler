from Expressions.BinaryExpression import BinaryExpression
from Expressions.DotExpression import DotExpression
from Expressions.FalseExpression import FalseExpression
from Expressions.IdentifierExpression import IdentifierExpression
from Expressions.IntExpression import IntExpression
from Expressions.InvocationExpression import InvocationExpression
from Expressions.NewExpression import NewExpression
from Expressions.NullExpression import NullExpression
from Expressions.TrueExpression import TrueExpression


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
        elif e == "new":
            return NewExpression.generate(exp)
        elif e == "dot":
            return DotExpression.generate(cls.generate, exp)
        elif e == "true":
            return TrueExpression(exp.get("line"))
        elif e == "false":
            return FalseExpression(exp.get("line"))
        elif e == "id":
            return IdentifierExpression(exp.get("line"), exp.get("id"))
        elif e == "null":
            return NullExpression(exp.get("line"))

        else:
            raise Exception("Invalid Expression.")
