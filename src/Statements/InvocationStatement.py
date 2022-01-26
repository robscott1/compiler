from CompilerError import CompilerError
from ErrorOut import error_out
from Expressions.Expression import Expression
from Expressions.InvocationExpression import InvocationExpression
from Factories.ExpressionFactory import ExpressionFactory
from Statements.Statement import Statement


class InvocationStatement(Statement):
    def __init__(self, line: int, exp: Expression):
        super(InvocationStatement, self).__init__(line)
        self.exp = exp

    @classmethod
    def generate(cls, stmt: dict):
        exp_args = {
            "line": stmt.get("line"),
            "exp": stmt.get("invocation"),
            "id": stmt.get("id"),
            "args": stmt.get("args")
        }
        exp = InvocationExpression.generate(ExpressionFactory.generate, exp_args)
        return InvocationStatement(stmt.get("line"), exp)

    """
    Static analysis of InvocationStatement
    
    @validations:
        - Make sure each arg to the invocation expression is as prescribed
    """
    def analyze(self, tc):
        inv_args = self.exp.args
        inv_id = self.exp.id
        if inv_id not in tc.fn_map:
            error_out(self.line, f"Undeclared function: {inv_id}", code=300)
        fn_params = tc.fn_map.get(inv_id).parameters
        if len(inv_args) != len(fn_params):
            error_out(self.line,
                                f"Unexpected number of arguments: {inv_args}", code=301)
        params = tc.fn_map.get(inv_id).parameters
        for arg, param in list(zip(inv_args, params)):
            arg_type = arg.of_type(tc)
            param_type = param.type
            if not arg_type.equals(param_type):
                error_out(
                    self.line, f"Mismatching types for arguments", code=302
                )


