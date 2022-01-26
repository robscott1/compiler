from BoolType import BoolType
from CompilerError import CompilerError
from Expressions.Expression import Expression
from Factories.ExpressionFactory import ExpressionFactory
from Statements.Statement import Statement


class ConditionalStatement(Statement):

    def __init__(self, line: int, guard: Expression,
                 then_block: Statement, else_block: Statement):
        super(ConditionalStatement, self).__init__(line)
        self.guard = guard
        self.then_block = then_block
        self.else_block = else_block

    @classmethod
    def generate(cls, func, stmt: dict):
        line = stmt.get("line")
        exp_dict = stmt.get("guard")
        guard = ExpressionFactory.generate(exp_dict)
        then_block = func(stmt.get("then"))
        # Assume there is not an else block
        else_block = None
        if "else" in stmt:
            else_block = func(stmt.get("else"))
        return ConditionalStatement(line, guard, then_block, else_block)

    """
    Analysis of conditional guard and statements after
    
    @validations:
        - guard Expression must evaluate to a booltype [x]
        - analyze then and else statements [x]
    """
    def analyze(self, tc):
        if not isinstance(self.guard.of_type(tc), BoolType):
            raise CompilerError(self.line, "Conditional needs boolean.", code="100")
        self.then_block.analyze(tc)
        if self.else_block is not None:
            self.else_block.analyze(tc)

