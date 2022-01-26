from CompilerError import CompilerError
from Expressions.Expression import Expression
from StructType import StructType
from TypeDeclaration import TypeDeclaration


class DotExpression(Expression):

    def __init__(self, line: int, left: Expression, id: str):
        super(DotExpression, self).__init__(line)
        self.left = left
        self.id = id

    @classmethod
    def generate(cls, fn, exp: dict):
        exp.pop("exp")
        exp["left"] = fn(exp.get("left"))
        return DotExpression(**exp)

    def of_type(self, tc):
        lft_type = self.left.of_type(tc)
        if not isinstance(lft_type, StructType):
            raise CompilerError(self.line, f"Type {lft_type} has no fields.")
        if lft_type.id not in tc.type_map:
            raise CompilerError(self.line, f"Type {lft_type} undeclared.")
        target_struct: TypeDeclaration = tc.type_map.get(lft_type.id)
        return target_struct.get_field_type(self.id)


