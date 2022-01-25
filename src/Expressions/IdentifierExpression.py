from CompilerError import CompilerError
from Expressions.Expression import Expression
from StructType import StructType
from Type import Type


class IdentifierExpression(Expression):

    def __init__(self, line: int, id: str):
        super(IdentifierExpression, self).__init__(line)
        self.id = id

    """
    Checks IdentifierExpression
    
    @validations:
        - is a global variable or within function scope
    """

    def of_type(self, tc):
        if self.id in tc.global_map:
            glb = tc.global_map.get(self.id)
            return glb.type
        elif self.id in tc.current_scope:
            glb = tc.current_scope.get_id_type(self.id)
            return glb.type

        raise CompilerError(self.line, "Unexpected id.", code="006")


