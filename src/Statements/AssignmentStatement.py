from CompilerError import CompilerError
from ErrorOut import error_out
from Expressions.Expression import Expression
from Factories.ExpressionFactory import ExpressionFactory
from LvalueId import LvalueId
from Statements.Statement import Statement
from l_value import Lvalue


class AssignmentStatement(Statement):
    def __init__(self, line: int, target: Lvalue, source: Expression):
        super(AssignmentStatement, self).__init__(line)
        self.target = target
        self.source = source

    @classmethod
    def generate(cls, stmt: dict):
        line = stmt.get("line")
        source_dict = stmt.get("source")
        source = ExpressionFactory.generate(source_dict)
        lvalue_id_dict = stmt.get("target")
        lvalue_id = LvalueId(**lvalue_id_dict)
        return AssignmentStatement(line, lvalue_id, source)

    """
    Static analysis of target value and expression being assigned to it.
    
    @:param:
        - tc (TypeChecker): TypeChecker
    
    @validations:
        - value being assigned has been initialized [x]
        - is not a param of function [x]
        - type of initialized variable = type of expression [x]
    """
    def analyze(self, tc):
        target_id = self.target.id
        if target_id not in tc.global_map and not tc.current_scope.id_in_scope(target_id):
            error_out(self.line, "Bad assignment.", code="200")
        if tc.current_scope.id_is_param(self.target.id):
            error_out(self.line, "Bad assignment.", code="201")

        target_type = tc.get_id_type(self.target.id)
        src_type = self.source.of_type(tc)
        if not target_type.equals(src_type):
            error_out(self.line, "Bad assignment.", code="202")


