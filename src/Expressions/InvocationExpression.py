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

    def type_check(self, tc):
        param = {
            "line": self.line,
            "msg": "Bad function invocation.",
            "expression": self,
            "code": "002"
        }
        # closures ?
        if self.id not in tc.fn_map:
            raise CompilerError(**param)

        for exp, act in list(
                zip_longest(tc.fn_map.get(self.id).parameters,
                            self.args, fillvalue=None)):
            # if there is a mismatch # of arguments
            if exp == None or act == None:
                raise CompilerError(**param)

            # type check each expression
            act.type_check(tc)



            # variable is within scope or in global map
            if not isinstance(act, IntExpression):
                if act.id not in tc.global_map:
                    raise CompilerError(**param)
                if not tc.current_scope.id_in_scope(act.id):
                    raise CompilerError(**param)
