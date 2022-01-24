from CompilerError import CompilerError
from Expressions.Expression import Expression


class IdentifierExpression(Expression):

    def __init__(self, line: int, id: str):
        super(IdentifierExpression, self).__init__(line)
        self.id = id

    """
    Checks IdentifierExpression
    
    @validations:
        - id is part of the larger structure
    """

    def type_check(self, tc):
        pass
