from CompilerError import CompilerError
from Expressions.Expression import Expression
from StructType import StructType


class NewExpression(Expression):

    def __init__(self, line: int, id: str):
        super(NewExpression, self).__init__(line)
        self.id = id

    @classmethod
    def generate(cls, exp: dict):
        exp.pop("exp")
        return NewExpression(**exp)

    def of_type(self, tc):
        if self.id not in tc.type_map:
            error_out(
                self.line, "Undeclared type reference", code="400"
            )
        return StructType(self.id)

