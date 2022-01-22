from enum import Enum

from Expressions.Expression import Expression
from Operator import Operator


class BinaryExpression(Expression):
    def __init__(self, line: int, operator: Operator,
                 left: Expression, right: Expression):
        super(BinaryExpression, self).__init__(line)
        self.operator = operator
        self.left = left
        self.right = right

    @classmethod
    def generate(cls, line: int, operator: str, left: Expression,
                 right: Expression
                 ):
        op_map = {
            "*": Operator.TIMES,
            "/": Operator.DIVIDE,
            "+": Operator.PLUS,
            "-": Operator.MINUS,
            "<": Operator.LT,
            "<=": Operator.LE,
            ">": Operator.GT,
            ">=": Operator.GE,
            "==": Operator.EQ,
            "!=": Operator.NE,
            "&&": Operator.AND,
            "||": Operator.OR
        }
        return BinaryExpression(line, op_map.get(operator),
                                left, right)
