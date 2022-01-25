from CompilerError import CompilerError
from Expressions.Expression import Expression


class NewExpression(Expression):

    def __init__(self, line: int, id: str):
        super(NewExpression, self).__init__(line)
        self.id = id

    @classmethod
    def generate(cls, exp: dict):
        exp.pop("exp")
        return NewExpression(**exp)

    def type_check(self, tc):
        if self.id not in tc.type_map:
            error_spec = {
                "line": self.line,
                "msg": "Undeclared type reference.",
                "expression": self,
                "code": "001"
            }
            raise CompilerError(**error_spec)
        return tc.type_map.get(self.id)

