from Expressions.IdentifierExpression import IdentifierExpression
from Statements.Statement import Statement


class DeleteStatement(Statement):

    def __init__(self, line, exp):
        super(DeleteStatement, self).__init__(line)
        self.expression = exp

    @classmethod
    def generate(cls, stmt: dict):
        exp = cls._generate_id_expression(stmt.get("exp"))
        exp_args = {
            "line": stmt.get("line"),
            "exp": exp,
        }

        return DeleteStatement(**exp_args)

    @classmethod
    def _generate_id_expression(cls, exp_dict):
        exp_dict.pop("exp")
        return IdentifierExpression(**exp_dict)

    def analyze(self, tc):
        pass

