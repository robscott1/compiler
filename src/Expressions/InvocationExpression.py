from CompilerError import CompilerError
from Expressions.Expression import Expression
from itertools import zip_longest

from Expressions.IntExpression import IntExpression


class InvocationExpression(Expression):
    """
    @:param:
        - args (List<Expression>)
    """

    def __init__(self, line: int, id: str, args: list):
        super(InvocationExpression, self).__init__(line)
        self.id = id
        self.args = args

    """
    @:param
        - fn: ExpressionFactory.generate() to turn all args to Exp.
    """

    @classmethod
    def generate(cls, fn, exp: dict):
        exp.pop("exp")
        exp["args"] = list(map(
            lambda x: fn(x), exp.get("args"))) \
            if exp["args"] != [] else []
        return InvocationExpression(**exp)

    """
    Type checks invocation.
    
    @validates:
        - args list are valid, existing variables
        - function being invoked is an available function
        - # args and respective arg-type match the function being invoked
    """

    def of_type(self, tc):
        return tc.fn_map.get(self.id).return_type
