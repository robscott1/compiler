from ErrorOut import error_out
from Expressions.Expression import Expression


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
        elif tc.current_scope.id_in_scope(self.id):
            glb = tc.current_scope.get_id_type(self.id)
            return glb

        error_out(self.line, "Unexpected id.", code="006")


