from Expressions.Expression import Expression
from Statements.Statement import Statement


class CompilerError:

    def __init__(self, line: int, msg: str,
                 statement: Statement = None, expression: Expression = None
                 ):
        self.line = line
        self.msg = msg
        self.statement = statement
        self.expression = expression

    def __repr__(self):
        return f"Error: {self.line}: {self.msg}"
